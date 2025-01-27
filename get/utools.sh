WEB_CONTENT=$(curl -s "https://www.u-tools.cn/download/")

X64_URL=$(echo $WEB_CONTENT | grep -o "https://[^ ]*amd64\.deb")

# https://open.u-tools.cn/download/utools_5.2.1_amd64.deb
VERSION=$(echo $X64_URL | cut -d '_' -f 2)

./check_downloader.py utools $VERSION $X64_URL
