from selenium import webdriver

def get_driver():
  x= webdriver.ChromeOptions()
  x.add_argument("disable-infobars")
  x.add_argument("start-maximized")
  x.add_argument("disable-dev-shm-usage")
  x.add_argument("no-sandbox")
  x.add_experimental_option("excludeSwitches",["enable-automation"])
  x.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=x)
  driver.get("http://automated.pythonanywhere.com")
  return driver

def main():
  driver=get_driver()
  element=driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())

