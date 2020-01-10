from sites import sites
from config import driver
import time
from datetime import datetime

SCROLL_PAUSE_TIME = 0.5

# Get scroll height

for site in sites:
    startTime = datetime.now()
    print("Beginning site: ", site["name"])
    driver.set_window_size(2560, 1440)
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

    current_scroll = 0
    while current_scroll < last_height:
        print(f"Rescrolling page to {current_scroll}")
        driver.execute_script(f"window.scrollTo(0, {current_scroll})")
        time.sleep(SCROLL_PAUSE_TIME)
        current_scroll += 200

    filename = site["name"]
    path = f"./screenshots/{filename}.png"
    print(driver.get_window_size())
    driver.set_window_size(2560, last_height + 150)
    driver.set_window_position(0, 0)
    print(driver.get_window_size())
    driver.find_element_by_tag_name("body").screenshot(path)
    time_elapsed = datetime.now() - startTime
    print(f"Finished site in {time_elapsed}")

driver.quit()
