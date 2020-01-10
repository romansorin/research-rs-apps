from sites import sites
from config import driver
import time
from datetime import datetime
startTime = datetime.now()

SCROLL_PAUSE_TIME = 5.0

# Get scroll height

for site in sites:
    print("Beginning site: ", site["name"])
    driver.get(site["url"])
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        print("Scrolling to height")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(last_height)
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    filename = site["name"]
    path = f"./screenshots/{filename}.png"
    driver.set_window_size(2560, driver.execute_script("return document.body.scrollHeight"))
    driver.find_element_by_tag_name("body").screenshot(path)
    print("Finished site")

print(datetime.now() - startTime)

driver.quit()
