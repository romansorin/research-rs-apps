from sites import sites
from config import driver, LOGGING
import time
from datetime import datetime

SCROLL_PAUSE_TIME = 5
RESCROLL_PAUSE_TIME = 0.5
RESCROLL_INCREMENTS = 200


def now():
    return datetime.now()


def time_elapsed(start, end):
    return end - start


def get_scroll_height():
    return driver.execute_script("return document.body.scrollHeight")


def set_window_height(height=1440):
    driver.set_window_size(2560, height)
    pass


def get_window_height():
    return driver.get_window_size()


def scroll_to(height):
    driver.execute_script(f"window.scrollTo(0, {height})")
    pass


def scroll(height):
    while True:
        if LOGGING: print(f"Scrolling to height {height}")
        scroll_to("document.body.scrollHeight")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = get_scroll_height()
        if new_height == height:
            break
        height = new_height
    return height


def rescroll(height):
    current_scroll = 0

    while current_scroll < height:
        if LOGGING: print(f"Rescrolling page to {current_scroll}")
        scroll_to(current_scroll)
        time.sleep(RESCROLL_PAUSE_TIME)
        current_scroll += RESCROLL_INCREMENTS


def screenshot(filename, height):
    if LOGGING: print(get_window_height())
    set_window_height(height + 150)
    driver.set_window_position(0, 0)
    if LOGGING: print(get_window_height())

    scroll_to("document.body.scrollHeight")
    path = f"./screenshots/{filename}.png"
    driver.find_element_by_tag_name("body").screenshot(path)

    if LOGGING: print(f"Finished site in {time_elapsed(start_time, datetime.now())}")


def setup(name, url):
    if LOGGING: print(f"Beginning site: {name}")

    set_window_height()
    driver.get(url)

    return now(), get_scroll_height()


if __name__ == "__main__":
    for site in sites:
        start_time, last_height = setup(site["name"], site["url"])
        last_height = scroll(last_height)
        rescroll(last_height)
        screenshot(site["name"], last_height)
    driver.quit()
