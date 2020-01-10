from selenium import webdriver

# Path to geckodriver (firefox) executable
geckodriver = "./drivers/geckodriver"

# Configure Firefox driver settings
profile = webdriver.FirefoxProfile("./profile")
options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("--width=2560")
options.add_argument("--height=1440")

driver = webdriver.Firefox(
    executable_path=geckodriver, options=options, firefox_profile=profile
)
driver.implicitly_wait(60)
