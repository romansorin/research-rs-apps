from selenium import webdriver
import platform

VERBOSE = True

# Path to geckodriver (firefox) executable
if platform.system() == 'Windows':
    geckodriver = "./drivers/geckodriver.exe"
else:
    geckodriver = "./drivers/geckodriver"

profile = webdriver.FirefoxProfile("./profile")

options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("--width=2560")
options.add_argument("--height=1440")

driver = webdriver.Firefox(
    executable_path=geckodriver, options=options, firefox_profile=profile
)
driver.implicitly_wait(60)
