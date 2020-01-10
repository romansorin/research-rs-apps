from sites import sites
from config import driver, LOGGING
import time
from datetime import datetime

SCROLL_PAUSE_TIME = 5
RESCROLL_PAUSE_TIME = 0.5


def now():
    return datetime.now()


def time_elapsed(start, end):
    return end - start


def get_scroll_height():
    return driver.execute_script("return document.body.scrollHeight")


def scroll(height):
    while True:
        if LOGGING: print(f"Scrolling to height {height}")
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
        if LOGGING: print(f"Rescrolling page to {current_scroll}")
        driver.execute_script(f"window.scrollTo(0, {current_scroll})")
        time.sleep(RESCROLL_PAUSE_TIME)
        current_scroll += 200


def screenshot(filename):
    if LOGGING: print(driver.get_window_size())

    driver.set_window_size(2560, last_height + 150)
    driver.set_window_position(0, 0)
    driver.execute_script("window.scrollTo(0, 0)")

    if LOGGING: print(driver.get_window_size())

    path = f"./screenshots/{filename}.png"

    driver.find_element_by_tag_name("body").screenshot(path)
    if LOGGING: print(f"Finished site in {time_elapsed(start_time, datetime.now())}")


def setup(name, url):
    if LOGGING: print(f"Beginning site: {name}")

    driver.set_window_size(2560, 1440)
    driver.get(url)

    return now(), get_scroll_height()




if __name__ == "__main__":
    for site in sites:
        start_time, last_height = setup(site["name"], site["url"])
        last_height = scroll(last_height)
        rescroll(last_height)
        screenshot(site["name"])
    driver.quit()
