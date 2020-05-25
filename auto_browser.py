from browsermobproxy import Server
from selenium import webdriver
import os
import json
import urllib.parse as urlparse
#import dohproxy
import time

# path to chrome web driver
chrome_driver_path = "C:\\Users\\Desktop\\Desktop\\DoH\\chromedriver.exe"
browsermob_proxy_path = "C:\\Users\\Desktop\\Desktop\\DoH\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"

def chrome_browser(proxy):
    """Chrome Web Driver"""
    chrome_driver = chrome_driver_path
    url = urlparse.urlparse(proxy.proxy).path
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={0}".format(url))
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    return driver


def firefox_browser(proxy):
    """Firefox Web Driver"""
    profile = webdriver.FirefoxProfile()
    selenium_proxy = proxy.selenium_proxy()
    profile.set_proxy(selenium_proxy)
    driver = webdriver.Firefox(firefox_profile=profile)
    return driver


def configure_server(proxy, browsers, websites):
    harfile = open("HAR.txt", "w")
    for browser in browsers:
        print("=====> Configuring Server - Please Wait... <=====")
        if browser == "chrome":
            driver = chrome_browser(proxy)
            print("=====> Using Google Chrome <=====")
        if browser == "firefox":
            driver = firefox_browser(proxy)
            print("=====> Using Firefox <=====")
        for website in websites:
            print("===========================================================",website)
            print("Creating HAR for Website: https://{}".format(website))
            proxy.new_har("https://{}".format(website), options={'captureHeaders': True})
            driver.get("https://{}".format(website))
            result = json.dumps(proxy.har)
            harfile.write(result)

            print(result)
        driver.quit()


def create_server(browser, websites):
    print("=====> Creating New Server - Please Wait... <=====")
    server = Server(browsermob_proxy_path)
    server.start()
    proxy = server.create_proxy()
    configure_server(proxy, browser, websites)
    close_server(proxy, server)


def close_server(proxy, server):
    proxy.close()
    server.stop()


def main():
    browser = ["chrome", "firefox"]
   # websites = ["google.com"]# open("websites.txt", "r")
    webs =  open("websites.txt", "r")
    websites = webs.read().split('\n')
    webs.close()
    print(websites)
    create_server(browser, websites)


if __name__ == "__main__":
    main()