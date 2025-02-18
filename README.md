# wcbing APT 软件源/仓库

适用于 Debian-based 发行版（Debian/Ubuntu/Mint/...）的 APT 软件源/仓库，收集一些国内常用软件的二进制包。

本仓库仅提供链接重定向功能，致力于在不改动 APT 的情况下实现类似 WinGet、Homebrew Cask 等仅提供仓库索引的效果。


## 使用现有仓库

请于[现有仓库实例](https://packages.wcbing.top/deb/)查看使用方法。


## 收录的软件说明
- 现主要服务 x86_64 用户，同时实验性支持 arm64。  
如有需要请参考最后一节自行建立仓库。
- 主要收录官方打包发布的文件，不接受第三方自行打包的商业软件。
- 有固定的更新地址，如官网、官方仓库或 Github Releases。
- 不收录打包的 wine 应用、Android 应用。
- 不收录图标、主题、字体等包，以后可能单独建一个相关仓库。


## 已收录软件

### 自行收集

| 软件名 | 包名 | amd64 | arm64 |
| ----- | ---- | ----- | ----- |
| [QQ](https://im.qq.com/linuxqq/) | linuxqq | ✅ | ✅ |
| [QQ音乐](https://y.qq.com/download/download.html) | qqmusic | ✅ | |
| [腾讯会议](https://meeting.tencent.com/download/) | wemeet | ✅ | ✅ |
| [百度网盘](https://pan.baidu.com/download) | baidunetdisk | ✅ | |
| [钉钉](https://www.dingtalk.com/download/) | com.alibabainc.dingtalk | ✅ | |
| [飞书](https://www.feishu.cn/download) | bytedance-feishu-stable | ✅ | |
| [Xmind](https://xmind.cn/download/) | xmind-vana | ✅ | |
| [uTools](https://u.tools/download/) | utools | ✅ | |
| [360安全浏览器](https://browser.360.net/gc/) | browser360-cn-stable | ✅ | |
| [滴答清单](https://dida365.com/download) | dida | ✅ | ✅ |
| [向日葵](https://sunlogin.oray.com/download/linux) | sunloginclient<br />提取自 Debian 12 的依赖：<br />gconf2-common<br />libgconf-2-4 | ✅ | |
| [ToDesk](https://www.todesk.com/linux.html) | todesk | ✅ | |
| [微信](https://linux.weixin.qq.com/) | wechat | ✅ | ✅ |


### Github Releses

> 因服务器资源有限，本仓库可能无法收录部分大文件。  
> 有收录需求也可投稿至星火商店的 [Github Releases 更新配置仓库](https://gitee.com/spark-building-service/github)，其和本部分内容是同源的。

| 软件名 | 包名 | amd64 | arm64 |
| ----- | ---- | ----- | ----- |
| [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases) | clash-verge | ✅ | ✅ |
| [FlClash](https://github.com/chen08209/FlClash/releases) | flclash | ✅ | |
| [mihomo](https://github.com/MetaCubeX/mihomo/releases) | mihomo | ✅ | ✅ |
| [hugo](https://github.com/gohugoio/hugo/releases) | hugo | ✅ | ✅ |
| [RustDesk](https://github.com/rustdesk/rustdesk/releases) | rustdesk | ✅ | ✅ |
| [Obsidian](https://github.com/obsidianmd/obsidian-releases/releases) | obsidian | ✅ | |
| [Foliate](https://github.com/johnfactotum/foliate/releases) | foliate |  ✅ | ✅ |
| [Tabby](https://github.com/Eugeny/tabby/releases) | tabby-terminal | ✅ | ✅ |
| [Pandoc](https://github.com/jgm/pandoc/releases) | pandoc | ✅ | ✅ |
| [LocalSend](https://github.com/localsend/localsend/releases) | localsend | ✅ | ✅ |
| [Motrix](https://github.com/agalwood/Motrix/releases) | motrix | ✅ | ✅ |
| [PeaZip](https://github.com/peazip/PeaZip/releases) | peazip | ✅ | |
| [Neovim/Nvim](https://github.com/neovim/neovim-releases/releases) | neovim | ✅ | |
| [Hiddify](https://github.com/hiddify/hiddify-app/releases) | hiddify | ✅ | |
| [Cloudflare Tunnel](https://github.com/cloudflare/cloudflared/releases) | cloudflared | ✅ | ✅ |
| [Caddy](https://github.com/caddyserver/caddy/releases) | caddy | ✅ | ✅ |

### 合并自官方 repo

| 软件仓库 | 包名 | amd64 | arm64 |
| ------ | ---- | ----- | ----- |
|Mozilla Firefox|firefox<br />firefox_beta<br />firefox_devedition<br />firefox_esr<br />firefox_nightly<br />mozillavpn| ✅ | ✅<br />官方仅提供<br />firefox_nightly |
|Google Chrome|google-chrome-stable<br />google-chrome-beta<br />google-chrome-unstable| ✅ | |
|Google Earth|google-earth-pro-stable<br />google-earth-ec-stable| ✅ | |
|Microsoft Edge|microsoft-edge-stable<br />microsoft-edge-beta<br />microsoft-edge-dev| ✅ | |
|Opera|opera-stable<br />opera-beta<br />opera-developer| ✅ | |
|Visual Studio Code|code<br />code-insiders<br />code-exploration| ✅ | ✅ |
|termius|termius-app<br />termius-beta| ✅ | |
|Sublime Text<br />Sublime Merge|sublime-text<br />sublime-merge| ✅ | ✅ |
|Steam|steam-launcher<br />steam-libs-amd64| ✅ | |
|Tailscale|tailscale<br />tailscale-nginx-auth| ✅ | ✅ |
|[black-desk 打包](https://github.com/black-desk/debs)|app.typst.typst<br />dev.neovide.neovide<br />dev.zed.zed<br />dev.zed.zed-pre<br />~~io.github.black-desk.debian-tweak<br />io.neovim.neovim<br />io.neovim.neovim-nightly<br />one.metacubex.clash-meta~~<br />org.pimalaya.himalaya| ✅ | |
|Typora|typora| ✅ | ✅ |
|Zotero|zotero<br />zotero-beta<br />zotero6| ✅ | |
|Github CLI|gh| ✅ | ✅ |
|[dufs: wcbing 打包](https://github.com/wcbing-build/dufs-debs)|dufs| ✅ | ✅ |
|[frp: wcbing 打包](https://github.com/wcbing-build/frp-debs)|frps<br />frpc| ✅ | ✅ |
|[lazydocker: wcbing 打包](https://github.com/wcbing-build/lazydocker-debs)|lazydocker| ✅ | ✅ |
|[lazygit: wcbing 打包](https://github.com/wcbing-build/lazygit-debs)|lazygit| ✅ | ✅ |
|[NextTrace](https://github.com/nxtrace/nexttrace-debs)|nexttrace| ✅ | ✅ |
|Debian 中文社区软件源|anydesk<br />marktext<br />wps-office<br />[更多](https://github.com/debiancn/repo)| ✅ | |

## 自建仓库

[参见 Wiki](https://github.com/wcbing/wcbing-apt-repo/wiki/self-hosting)
