from collections import deque

sites = (
    "google.com",
    "yahoo.com",
    "bing.com"
)

pages = deque(maxlen=3)
print('max size', pages.maxlen)


for site in sites:
    pages.appendleft(site)

print(pages)


pages.appendleft("facebook.com")
print(pages)


pages.appendleft("twitter.com")
print(pages)
