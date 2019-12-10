from selenium import webdriver

geckodriver = './geckodriver'

profile = webdriver.FirefoxProfile('./profile')

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path=geckodriver,
                           options=options, firefox_profile=profile)
