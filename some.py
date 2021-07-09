chromrdriver = "C:/Users/samun/Desktop/test/chromedriver"
os.environ["webdriver.chrome.driver"] = chromrdriver
driver = webdriver.Chrome(chromrdriver)
driver.get("https://medium.com/search?q=data%20science")

ScrollNumber = 10
for i in range(1,ScrollNumber):
    driver.execute_script("window.scrollTo(1,50000)")
    time.sleep(3)

# file = open('DS.html', 'w')
# file.write(driver.page_source)
# file.close()
with open("DS.html","w",encoding="utf-8") as f:
    f.write(driver.page_source)
f.close()

driver.close()