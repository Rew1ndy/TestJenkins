from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def run_gallery_test():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)

    try:
        print("Test: gallery")
        driver.get("https://alexmegua.github.io/game-portfolio/")
        time.sleep(2)

        gallery_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/gallery' and @data-discover='true']"))
        )
        gallery_link.click()
        print("Moving to gallery")

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.slick-arrow.slick-next"))
        )

        for _ in range(4):
            next_button.click()
            time.sleep(0.5)
        print("Pressed 4 times to move")
        time.sleep(2)

        scroll_pause_time = 1
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break 
            last_height = new_height

        print("End of page")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_gallery_test()
