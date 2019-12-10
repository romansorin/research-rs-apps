from config import driver
from sites import sites


driver.implicitly_wait(90)

for site in sites:
    driver.get(site['url'])
    page = driver.find_element_by_tag_name('body')

    path = f"./screenshots/{site['name']}.png"
    page.screenshot(path)


driver.quit()
