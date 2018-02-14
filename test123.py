import urllib.request

request = urllib.request.Request("http://www.paperbackswap.com/mobile/index.php?ti=python")
response = urllib.request.urlopen(request)
the_page = response.read()
theText = the_page.decode()
