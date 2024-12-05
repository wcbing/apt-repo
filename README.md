# wcbing（APT）软件源/仓库

供 Debian 系发行版用户使用的软件源，收集一些国内常用软件的二进制包。

本仓库对于下载不受限的软件不提供文件托管服务，仅提供链接重定向功能，致力于在不改动 APT 的情况下实现类似 WinGet、Homebrew Cask 等仅提供仓库索引的效果。

收录的软件说明：
- 官方打包发布的文件 ~~，不接受第三方自行打包~~。
- 不收录打包的 wine 应用、Android 应用。
- 不收录图标、主题、字体等包，以后可能单独建一个相关仓库。
- 有固定的更新地址，如官网、官方仓库或 Github Releases。
- 现主要服务 x86_64 用户，同时实验性支持 arm64，如有需要请参考最后一节自行建立仓库。

## 使用现有仓库

添加本仓库：
```sh
curl -fsSL https://packages.wcbing.top/deb/add.sh | sudo sh
```

移除本仓库：
```sh
curl -fsSL https://packages.wcbing.top/deb/del.sh | sudo sh
```

## 已收录软件

### 自行收集

| 软件名 | 包名 | amd64 | arm64 |
| ----- | ---- | ----- | ----- |
| [QQ](https://im.qq.com/linuxqq/) | linuxqq | ✅ | ✅ |
| [QQ音乐](https://y.qq.com/download/download.html) | qqmusic | ✅ | |
| [腾讯会议](https://meeting.tencent.com/download/) | wemeet | ✅ | ✅ |
| [WPS Office](https://linux.wps.cn/) | wps-office | ✅ | |
| [百度网盘](https://pan.baidu.com/download) | baidunetdisk | ✅ | |
| [钉钉](https://www.dingtalk.com/download/) | com.alibabainc.dingtalk | ✅ | |
| [飞书](https://www.feishu.cn/download) | bytedance-feishu-stable | ✅ | |
| [Xmind](https://xmind.cn/download/) | xmind-vana | ✅ | |
| [uTools](https://u.tools/download/) | utools | ✅ | |
| [360安全浏览器](https://browser.360.net/gc/) | browser360-cn-stable | ✅ | |
| [滴答清单](https://dida365.com/download) | dida | ✅ | ✅ |
| [向日葵](https://sunlogin.oray.com/download/linux) | sunloginclient<br />提取自 Debian 12 的依赖：<br />gconf2-common<br />libgconf-2-4 | ✅ | |
| [ToDesk](https://www.todesk.com/linux.html) | todesk | ✅ | |
| [微信](https://linux.weixin.qq.com/) | wechat | ✅ | |


> 临时收录软件会在仓库首页通知。

### Github Releses

| 软件名 | 包名 | amd64 | arm64 |
| ----- | ---- | ----- | ----- |
| [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases) | clash-verge | ✅ | ✅ |
| [FlClash](https://github.com/chen08209/FlClash/releases) | flclash | ✅ | |
| [mihomo](https://github.com/MetaCubeX/mihomo/releases) | mihomo | ✅ | ✅ |
| [hugo](https://github.com/gohugoio/hugo/releases) | hugo | ✅ | ✅ |
| [RustDesk](https://github.com/rustdesk/rustdesk/releases) | rustdesk | ✅ | ✅ |
| [Obsidian](https://github.com/obsidianmd/obsidian-releases/releases) | obsidian | ✅ | |
| [draw.io](https://github.com/jgraph/drawio-desktop/releases) | draw.io | ✅ | ✅ |
| [Tabby](https://github.com/Eugeny/tabby/releases) | tabby-terminal | ✅ | ✅ |
| [Pandoc](https://github.com/jgm/pandoc/releases) | pandoc | ✅ | ✅ |
| [TinyGo](https://github.com/tinygo-org/tinygo/releases) | tinygo | ✅ | ✅ |
| [LocalSend](https://github.com/localsend/localsend/releases) | localsend | ✅ | ✅ |
| [Motrix](https://github.com/agalwood/Motrix/releases) | motrix | ✅ | ✅ |
| [PeaZip](https://github.com/peazip/PeaZip/releases) | peazip | ✅ | |
| [Neovim/Nvim](https://github.com/neovim/neovim-releases/releases) | neovim | ✅ | |
| [思源笔记](https://github.com/siyuan-note/siyuan/releases) | siyuan | ✅ | ✅ |
| [Hiddify](https://github.com/hiddify/hiddify-app/releases) | hiddify | ✅ | |

### 合并自官方 repo

| 软件仓库 | 包名 | amd64 | arm64 |
| ------ | ---- | ----- | ----- |
|Mozilla Firefox|firefox<br />firefox_beta<br />firefox_devedition<br />firefox_esr<br />firefox_nightly<br />mozillavpn| ✅ | ✅<br />官方仅提供<br />firefox_nightly |
|Google Chrome|google-chrome-stable<br />google-chrome-beta<br />google-chrome-unstable| ✅ | |
|Microsoft Edge|microsoft-edge-stable<br />microsoft-edge-beta<br />microsoft-edge-dev| ✅ | |
|Visual Studio Code|code<br />code-insiders<br />code-exploration| ✅ | ✅ |
|termius|termius-app<br />termius-beta| ✅ | |
|Sublime Text<br />Sublime Merge|sublime-text<br />sublime-merge| ✅ | ✅ |
|Steam|steam-launcher<br />steam-libs-amd64| ✅ | |
|Tailscale|tailscale<br />tailscale-nginx-auth| ✅ | ✅ |
|[black-desk 打包](https://github.com/black-desk/debs)|app.typst.typst<br />dev.neovide.neovide<br />dev.zed.zed<br />dev.zed.zed-pre<br />io.github.black-desk.debian-tweak<br />io.neovim.neovim<br />io.neovim.neovim-nightly<br />one.metacubex.clash-meta<br />org.pimalaya.himalaya| ✅ | |
|Typora|typora| ✅ | ✅ |
|Zotero|zotero<br />zotero-beta<br />zotero6| ✅ | |
|Github CLI|gh| ✅ | ✅ |
|[ttyd: wcbing 打包](https://github.com/wcbing/ttyd-debs)|ttyd| ✅ | ✅ |

## 自建仓库

[参见 Wiki](https://github.com/wcbing/wcbing-apt-repo/wiki/self-hosting)
