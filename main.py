from selenium import webdriver

sites = [
    {
        'name': 'stripe',
        'url': 'https://stripe.com'},
    {
        'name': 'romansorin',
        'url': 'https://romansorin.com'
    },
    {
        'name': 'status-romansorin',
        'url': 'https://status.romansorin.com'
    }
]

geckodriver = './geckodriver'

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path=geckodriver, options=options)

for site in sites:
    print(site['name'])
    path = f"./screenshots/{site['name']}.png"
    driver.get(site['url'])
    el = driver.find_element_by_tag_name('body')
    el.screenshot(path)

driver.quit()
