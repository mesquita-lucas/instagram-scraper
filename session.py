from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

class Session:
    def __init__(self):
        self.driver = self._configurar_driver()
        self._wait = WebDriverWait(self.driver, 5)

    def scrape(self, page_name: str):
        scraper = _Scraper(self.driver)

        return scraper.scrape(page_name)

    def login(self, username, password):
        self.driver.get(
            "https://instagram.com/"
        )

        username_input = self._wait.until(
                EC.visibility_of_element_located(
                    (
                            By.CSS_SELECTOR,
                            "input[name='email']"
                    )
                )
            )
    
        password_input = self._wait.until(
                    EC.visibility_of_element_located(
                        (
                                By.CSS_SELECTOR,
                                "input[name='pass']"
                        )
                    )
                )
    
        login_button = self._wait.until(
                EC.element_to_be_clickable(
                    (
                            By.XPATH,
                            "//div[@role='button' and normalize-space()='Log in']"
                    )
                )
            )
    
        username_input.send_keys(username)

        password_input.send_keys(password)

        login_button.click()

    def _configurar_driver(self):
        options = Options()
        options.add_experimental_option("detach", True)
            
        driver = webdriver.Chrome(options=options)
            
        return driver
    
class _Scraper:
    FIRST_POST = (
        By.XPATH,
        "(//main//a[contains(@href, '/reel/') or contains(@href, '/p/')])[1]"
    )

    POST_DATETIME = (
        By.CSS_SELECTOR,
        "article time[datetime]"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//div[@role='dialog']//button[.//*[local-name()='svg' and @aria-label='Next']]"
    )

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def scrape(self, page_name: str):
        self._open_profile(page_name)
        self._open_first_post()

        return self._collect_posts()

    def _open_profile(self, page_name):
        self.driver.get(f"https://instagram.com/{page_name}")

    def _open_first_post(self):
        first_post = self._wait.until(
            EC.element_to_be_clickable(
                self.FIRST_POST
            )
        )

        first_post.click()

        self._wait.until(
            lambda driver:
                "/p/" in driver.current_url
                or "/reel/" in driver.current_url
        )

    def _get_current_post(self):
        time_element = self._wait.until(
            EC.visibility_of_element_located(
                self.POST_DATETIME
            )
        )

        url = self.driver.current_url

        datetime_value = time_element.get_attribute("datetime")

        return {
            "url": url,
            "datetime": datetime_value
        }

    def _go_to_next_post(self):
        current_url = self.driver.current_url

        
        next_button = self._wait.until(
            EC.element_to_be_clickable(self.NEXT_BUTTON)
        )

        try:
            next_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", next_button)

        
        self._wait.until(
            EC.url_changes(current_url)
        )

    def _collect_posts(self):
        posts = []
        visited_urls = set()

        while True:

            post = self._get_current_post()

            url = post["url"]

            visited_urls.add(url)
            posts.append(post)

            print(
                f"{len(posts)} | "
                f"{post['datetime']} | "
                f"{post['url']}"
            )

            try:
                self._go_to_next_post()
            except TimeoutException:
                print("Os posts acabaram")
                break

        return posts;