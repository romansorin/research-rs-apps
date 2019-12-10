from selenium import webdriver

geckodriver = './geckodriver'

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path=geckodriver, options=options)
