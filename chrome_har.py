from browsermobproxy import Server
from selenium import webdriver
import os
import json
import urllib.parse as urlparse

server = Server("C:\\Users\\Desktop\\Desktop\\DoH\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()

chromedriver = "C:\\Users\\Desktop\\Desktop\\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
url = urlparse.urlparse (proxy.proxy).path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={0}".format(url))
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("""--enable-features="dns-over-https<DoHTrial" --force-fieldtrials="DoHTrial/Group1" --force-fieldtrial-params="DoHTrial.Group1:server/https%3A%2F%2F1.1.1.1%2Fdns-query/method/POST""")
driver = webdriver.Chrome(chromedriver,options =chrome_options)
proxy.new_har("https://1.1.1.1/help", options={'captureHeaders': True})
driver.get("https://1.1.1.1/help")
result = json.dumps(proxy.har, ensure_ascii=False)
with open("HAR.txt", "w") as harfile:
    harfile.write(json.dumps(proxy.har))
print (result)
#driver.quit()