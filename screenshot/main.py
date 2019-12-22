from sites import sites
from config import driver

for site in sites:
    print("Beginning site: ", site["name"])
    driver.get(site["url"])
    page = driver.find_element_by_tag_name("body")
    filename = site["name"]
    path = f"./screenshots/{filename}.png"
    page.screenshot(path)
    print("Finished site")

driver.quit()
