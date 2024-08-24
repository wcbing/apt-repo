# wcbing（APT）软件源/仓库

供 Debian 系发行版用户使用的软件源，收集一些国内常用软件的二进制包。

收录的软件说明：
- 发布的是已打包的文件，不接受源码和自行打包。
- 有固定的更新地址，如官网和 Github Releases。
- 现只收录了 x86_64，如有需要请参考最后一节自行建立仓库。

## 使用现有仓库

```sh
sudo curl -o /etc/apt/keyrings/wcbing.gpg https://packages.wcbing.top/wcbing.gpg

echo "deb [signed-by=/etc/apt/keyrings/wcbing.gpg] https://packages.wcbing.top/deb /" | sudo tee /etc/apt/sources.list.d/wcbing.list
```

接下来执行 `sudo apt update` 更新即可。


## 现有软件

可在 [这里](https://packages.wcbing.top/deb/status.txt) 查看具体版本。

|软件名|包名|渠道|
|-|-|-|
|QQ|linuxqq|[官网](https://im.qq.com/linuxqq/)|
|QQ音乐|qqmusic|[官网](https://y.qq.com/download/download.html)|
|腾讯会议|wemeet|[官网](https://meeting.tencent.com/download/)|
|Clash Verge Rev|clash-verge|[Github Releses](https://github.com/clash-verge-rev/clash-verge-rev/releases)|
|mihomo|mihomo|[Github Releases](https://github.com/MetaCubeX/mihomo/releases)|
|hugo|hugo|[Github Releases](https://github.com/gohugoio/hugo/releases)|
|RustDesk|rustdesk|[Github Releases](https://github.com/rustdesk/rustdesk/releases)|
|Visual Studio Code|code|[官网](https://code.visualstudio.com)|
|Microsoft Edge|microsoft-edge-stable|[官网](https://www.microsoft.com/en-us/edge/download)|
|Google Chrome|google-chrome-stable|[官网](https://www.google.com/chrome/)|
|Obsidian|obsidian|[Github Releases](https://github.com/obsidianmd/obsidian-releases/releases)|
|WPS Office|wps-office|[官网](https://linux.wps.cn/)|


## 自行建立仓库

### 建立仓库

1. clone 本仓库，进入仓库目录。
2. 确认系统安装有 `Requests` Python 库，Debian 系应该自带。
2. 运行 `init_deb.py` 初始化。  
默认只新建 x86_64，需要其他架构请修改其中的SQL语句。
3. 创建一个**无密码**的 GPG 密钥对，导出 GPG 公钥文件待用。
4. 创建定时任务，定时运行 `update_gen.sh`  
crontab 样例：0 11,15,19 * * * cd [THIS_DIR] && ./update_gen.sh > ./deb/status.txt

### 发布与使用

这个仓库使用了[扁平仓库格式（Flat Repository Format）](https://wiki.debian.org/DebianRepository/Format#Flat_Repository_Format)。建立好后使用 Web 服务器将 `deb` 目录暴露出去即可。

使用时可参考前面已有的配置，先将第3部提到的 GPG 公钥导入，再新建软件源配置文件。
