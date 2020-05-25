

#"""Insert the Geckodriver into your python dir C:\Users\Desktop\AppData\Local\Programs\Python\Python38"""



from browsermobproxy import Server
from selenium import webdriver
import os
import json
import urllib.parse as urlparse
import psutil


server = Server("C:\\Users\\Desktop\\Desktop\\DoH\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()



profile = webdriver.FirefoxProfile()#"C:\\Users\\Desktop\\Desktop\\DoH\\geckodriver.exe"
selenium_proxy = proxy.selenium_proxy()
profile.set_proxy(selenium_proxy)
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har("https://1.1.1.1/help", options={'captureHeaders': True})
driver.get("https://1.1.1.1/help")
result = json.dumps(proxy.har, ensure_ascii=False)
with open("HAR.txt", "w") as harfile:
    harfile.write(json.dumps(proxy.har))

print (result)