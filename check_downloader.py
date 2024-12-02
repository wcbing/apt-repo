#!/usr/bin/env python3
import subprocess
import os
import sqlite3


def download(url, file_type):
    file_dir = os.path.join(file_type, "/".join(url.split("/")[:-1]))
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = os.path.join(file_type, url.split("?")[0])
    # 用 curl 模拟 apt 下载文件，User-Agent 来自 Debian 12
    subprocess.run(["curl", "-H", "User-Agent: Debian APT-HTTP/1.3 (2.6.1)", "-fsLo", file_path, url])


def check_download(name, version, url, arch, file_type="deb"):
    conn = sqlite3.connect(file_type + ".db")
    cur = conn.cursor()

    res = cur.execute(
        "SELECT version, url FROM " + arch + " WHERE name = ?", (name,)
    ).fetchall()
    if len(res):
        db_version = res[0][0]
        db_url = res[0][1]
        print(name + ": " + db_version)
        if db_version != version:
            print("└  Update: " + db_version + " -> " + version)
            download(url, file_type)
            # wirte to db
            cur.execute(
                "UPDATE " + arch + " SET version = ?, url = ? WHERE name = ?",
                (version, url, name),
            )
            # remove old version
            old_file_path = os.path.join(file_type, db_url.split("?")[0])
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
    else:
        print(name + "\n└  Add: " + version)
        download(url, file_type)
        # wirte to db
        cur.execute(
            "INSERT INTO " + arch + "(name, version, url) VALUES (?, ?, ?)",
            (name, version, url),
        )

    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    args = os.sys.argv
    if len(args) == 5:
        check_download(args[1], args[2], args[3], args[4])
    elif len(args) == 4:
        check_download(args[1], args[2], args[3], "x86_64")
    else:
        print("Usage: check.py <name> <version> <url> [arch]\n")
        print("arch: x86_64, arm64. default is x86_64")
