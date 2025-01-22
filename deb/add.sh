rm -f /etc/apt/keyrings/wcbing.gpg
rm -f /etc/apt/sources.list.d/wcbing.list

echo 'Types: deb
URIs: https://packages.wcbing.top/deb/$(ARCH)
Suites: /
Signed-By:
 -----BEGIN PGP PUBLIC KEY BLOCK-----
 .
 mDMEZqEmIxYJKwYBBAHaRw8BAQdAb3OvpKmsYtS3WBIz8GdS1TO6YgD2IuNcWGZu
 YuR3uU20FXdjYmluZyA8aUB3Y2JpbmcudG9wPoiTBBMWCgA7AhsDBQsJCAcCAiIC
 BhUKCQgLAgQWAgMBAh4HAheAFiEEHRei1xNvFmQQGtkXJiZVFo+zu6AFAmeRTlwA
 CgkQJiZVFo+zu6D2rgD/YNUyByUir6QZ7gszdL4gAI+iO3pG0ENaNC1T5uTa5hEB
 AP0+rqCx74ZLh8fwbVsxeU+yAfTTD1Aw4WbqtvE8uO8NuDgEZqEmIxIKKwYBBAGX
 VQEFAQEHQI5rbm+T72MiH3nHGRd8HZw2sHGFFurYIdbGq36GRbttAwEIB4h4BBgW
 CgAgAhsMFiEEHRei1xNvFmQQGtkXJiZVFo+zu6AFAmeRTw4ACgkQJiZVFo+zu6D6
 nwEApGVKLs8TzittX+yKKCKObcaBaXb4GjyyIi0QEzwW704A/0wRm+/W4poIZU7I
 SM5NncjbTIxHZ+s27b8CqZcpajYJ
 =QD/L
 -----END PGP PUBLIC KEY BLOCK-----
' > /etc/apt/sources.list.d/wcbing.sources

apt update
