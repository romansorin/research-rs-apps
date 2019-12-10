from selenium import webdriver

# Path to geckodriver (firefox) executable
geckodriver = './geckodriver'

# Configure Firefox driver settings
profile = webdriver.FirefoxProfile('./profile')
options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(executable_path=geckodriver,
                           options=options, firefox_profile=profile)

# Set an implicit wait that applies for entire driver life; hacky way to handle some sites that have lots of AJAX resource requests
driver.implicitly_wait(60)
