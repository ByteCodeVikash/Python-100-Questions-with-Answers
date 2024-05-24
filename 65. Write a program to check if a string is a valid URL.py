import re
from urllib.parse import urlparse

def valid_url(url):
    regex=re.compile(
        r'^(https?|ftp)://'  # http:// or https:// or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4 address
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6 address
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # resource path
    if re.match(regex,url) is None:
        return False
    
    parsed=urlparse(url)
    return bool(parsed.scheme and parsed.netloc)

test_url=(
       "http://example.com",
    "https://www.example.com/path/to/page?name=ferret&color=purple",
    "ftp://example.com/resource.txt",
    "http://localhost:8000",
    "http://192.168.0.1",
    "invalid_url",
    "http://example",
    "http://.com"
)

for i in test_url:
    print(i,"is valid",valid_url(i))