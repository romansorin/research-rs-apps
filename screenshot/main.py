from sites import sites
from config import driver, VERBOSE
import time
from datetime import datetime

SCROLL_PAUSE_TIME = 5
RESCROLL_PAUSE_TIME = 0.5


def now():
    return datetime.now()


def scroll(height):
    while True:
        print(f"Scrolling to height {height}")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == height:
            break
        height = new_height
    return height


def rescroll(height):
    current_scroll = 0
    while current_scroll < height:
        print(f"Rescrolling page to {current_scroll}")
        driver.execute_script(f"window.scrollTo(0, {current_scroll})")
        time.sleep(RESCROLL_PAUSE_TIME)
        current_scroll += 200


def screenshot():
    filename = site["name"]
    path = f"./screenshots/{filename}.png"
    print(driver.get_window_size())
    driver.set_window_size(2560, last_height + 150)
    driver.set_window_position(0, 0)
    driver.execute_script("window.scrollTo(0, 0)")
    print(driver.get_window_size())
    driver.find_element_by_tag_name("body").screenshot(path)
    print(f"Finished site in {time_elapsed(start_time, datetime.now())}")


def setup(name, url):
    if VERBOSE: print(f"Beginning site: {name}")

    driver.set_window_size(2560, 1440)
    driver.get(url)
    height = driver.execute_script("return document.body.scrollHeight")

    return now(), height


def time_elapsed(start, end):
    return end - start


if __name__ == "__main__":
    for site in sites:
        start_time, last_height = setup(site["name"], site["url"])
        last_height = scroll()
        rescroll(last_height)
        screenshot()
    driver.quit()


