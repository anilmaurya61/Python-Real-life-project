import pyshorteners

url = input("Enter URL :\n")

s = pyshorteners.Shortener()

print("URL after Shorting : ", s.tinyurl.short(url))