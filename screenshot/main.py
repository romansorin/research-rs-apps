from sites import sites
from config import driver

for site in sites:
    driver.get(site["url"])
    page = driver.find_element_by_tag_name("body")
    filename = site["name"]
    path = f"./screenshots/{filename}.png"
    page.screenshot(path)

driver.quit()
