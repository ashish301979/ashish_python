from HTMLParser import HTMLParser
import urllib2


#query="https://docs.python.org/2/howto/webservers.html"
query="http://code.google.com/feeds/issues/p/chromium/issues/full/2"

def get_issue_report(query):
    request = urllib2.Request(query)
    response = urllib2.urlopen(request)
    response_headers = response.info()
    return response.read()

s = get_issue_report(query)

p = HTMLParser()

print p.unescape(s)
