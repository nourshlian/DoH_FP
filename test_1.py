from selenium import webdriver

''' Chrome web driver interface
'''
hyperlink = "http://moomoo.co.il"
chromedriver = "C:\\Users\\Desktop\\Desktop\\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("""--enable-features="dns-over-https<DoHTrial" --force-fieldtrials="DoHTrial/Group1" --force-fieldtrial-params="DoHTrial.Group1:server/https%3A%2F%2F1.1.1.1%2Fdns-query/method/POST""")
driver = webdriver.Chrome(chromedriver,options =chrome_options)
driver.get(hyperlink)

''' Use Navigation Timing  API to calculate the timings that matter the most '''

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

dns_lookup_start = driver.execute_script("return window.performance.timing.domainLookupStart")
dns_lookup_end = driver.execute_script("return window.performance.timing.domainLookupEnd")
''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
print("DNS lookup time: %s " %(dns_lookup_end - dns_lookup_start))
print("Back End: %s" % backendPerformance_calc)
print("Front End: %s" % frontendPerformance_calc)

#driver.quit()