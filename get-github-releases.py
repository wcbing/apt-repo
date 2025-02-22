#!/usr/bin/env python3
import argparse
import requests
import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, wait
from check_downloader import check_download

github_info_list = {}

CONFIG = {"data_dir": "data", "proxy": "", "thread": 5}


# 读取命令行参数
def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", default="data", help="从 <DATA> 读取仓库配置")
    parser.add_argument(
        "-p", "--proxy", default="", help="Github 代理，<PROXY> 必须以 / 结尾"
    )
    parser.add_argument(
        "-t", "--thread", type=int, default=5, help="并发下载线程数量，默认为 5"
    )
    args = parser.parse_args()
    CONFIG.update({"data_dir": args.data, "proxy": args.proxy, "thread": args.thread})


if __name__ == "__main__":
    read_args()

    # read all repo info 读取所有仓库配置
    with open(os.path.join(CONFIG["data_dir"], "github.json"), "r") as f:
        github_info_list = json.load(f)

    tasks = []
    with ThreadPoolExecutor(max_workers=CONFIG["thread"]) as executor:
        for name, repo in github_info_list.items():
            release_url = (
                f'{CONFIG["proxy"]}https://github.com/{repo["repo"]}/releases'
            )
            # get latest version tag 获取最新版本标签
            location = requests.head(release_url + "/latest").headers.get("Location", "")
            match = re.search(r".*releases/tag/([^/]+)", location)
            if not match:
                continue
            version_tag = match.group(1)
            version = version_tag[1:] if version_tag[0].lower() == "v" else version_tag

            for arch, file_name in repo["file_list"].items():
                release_file = file_name.format(
                    version_tag=version_tag, stripped_version=version
                )
                file_url = f"{release_url}/download/{version_tag}/{release_file}"
                # 提交任务到线程池
                tasks.append(
                    executor.submit(check_download, name, version, file_url, arch)
                )
        # 等待所有任务完成
        wait(tasks)
