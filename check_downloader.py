#!/usr/bin/env python3
import subprocess
import os
import sqlite3
import sys
import logging
import threading

version_lock = threading.Lock()

base_dir = "deb"
logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    level=logging.INFO,
)


def download(url):
    file_dir = os.path.join(base_dir, os.path.dirname(url))
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = os.path.join(base_dir, url.split("?")[0])
    # 用 curl 模拟 apt 下载文件，User-Agent 来自 Debian 12
    subprocess.run(
        [
            "curl",
            "-H",
            "User-Agent: Debian APT-HTTP/1.3 (2.6.1)",
            "-fsLo",
            file_path,
            url,
        ]
    )


def check_download(name, version, url, arch):
    logging.info("%s:%s = %s", name, arch, version)

    db_path = os.path.join("data", f"{base_dir}.db")
    # get local version
    with version_lock:
        with sqlite3.connect(db_path) as conn:
            res = (
                conn.cursor()
                .execute(f"SELECT version, url FROM '{arch}' WHERE name = ?", (name,))
                .fetchone()
            )
    if res:
        local_version, local_url = res
        if local_version != version:
            print(f"Update: {name}:{arch} ({local_version} -> {version})")
            download(url)
            # update database
            with version_lock:
                with sqlite3.connect(db_path) as conn:
                    conn.cursor().execute(
                        f"UPDATE '{arch}' SET version = ?, url = ? WHERE name = ?",
                        (version, url, name),
                    )
                    # remove old version
                    if local_url != url:  # 防止固定下载链接
                        old_file_path = os.path.join(base_dir, local_url.split("?")[0])
                        if os.path.exists(old_file_path):
                            os.remove(old_file_path)
                    conn.commit()
    else:
        print(f"AddNew: {name}:{arch} ({version})")
        download(url)
        # update database
        with version_lock:
            with sqlite3.connect(db_path) as conn:
                conn.cursor().execute(
                    f"INSERT INTO '{arch}'(name, version, url) VALUES (?, ?, ?)",
                    (name, version, url),
                )
                conn.commit()


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 5:
        check_download(args[1], args[2], args[3], args[4])
    elif len(args) == 4:
        check_download(args[1], args[2], args[3], "amd64")
    elif len(args) > 1:
        logging.error(f"Unknown Args: {args[1:]}")
    else:
        print(f"Usage: {args[0]} <package_name> <version> <url> [arch]")
        print("options:")
        print("    arch: amd64, arm64, all. default is amd64")
