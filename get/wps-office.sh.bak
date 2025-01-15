decrypt() {
    url=$1
    pathname="/$(echo $url | cut -d '/' -f 4-)"
    secrity_key="7f8faaaa468174dc1c9cd62e5f218a5b"
    timestamp10=$(date '+%s')
    md5hash=$(echo -n "${secrity_key}${pathname}${timestamp10}" | md5sum | cut -d " " -f 1 )
    url="$url?t=${timestamp10}&k=${md5hash}"
    echo $url

    # # js
    # function downLoad(url) {
    #   var urlObj=new URL(url);
    #   var uri=urlObj.pathname;
    #   var secrityKey="7f8faaaa468174dc1c9cd62e5f218a5b";
    #   var timestamp10=Math.floor(new Date().getTime() / 1000);
    #   var md5hash=CryptoJS.MD5(secrityKey + uri + timestamp10);
    #   url += '?t=' + timestamp10 + '&k=' + md5hash
    #   console.log(url);
    # }
}

WEB_CONTENT=$(curl -fs https://linux.wps.cn/)
VERSION=$(echo $WEB_CONTENT | grep -o "<p class=\"banner_txt\">[0-9.]*</p>" | sed 's/<p class=\"banner_txt\">\(.*\)<\/p>/\1/')
X64_ORI_URL=$(echo $WEB_CONTENT | grep -o "https://[0-9a-zA-Z_\/\.\-]*amd64\.deb" | head -n 1)
X64_URL=$(decrypt $X64_ORI_URL)

./check_downloader.py wps-office $VERSION $X64_URL