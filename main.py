from selenium import webdriver

url = 'https://romansorin.com'
path = './scrape.png'

driver = webdriver.Firefox(executable_path=r'./geckodriver')
driver.get(url)
el = driver.find_element_by_tag_name('body')
el.screenshot(path)
driver.quit()