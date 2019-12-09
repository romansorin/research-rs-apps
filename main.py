from selenium import webdriver

url = 'https://stripe.com'
path = './scrape.png'

geckodriver = './geckodriver'

options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(executable_path=geckodriver, options=options)
driver.get(url)
el = driver.find_element_by_tag_name('body')
el.screenshot(path)
driver.quit()