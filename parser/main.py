import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

from parser.processing import parse_stats

BASE_URL = "https://www.fanfiction.net"


def parse_fanfiction_page(driver):
    driver.implicitly_wait(10)

    stories = driver.find_elements(By.CSS_SELECTOR, "div.z-list.zhover.zpointer")

    parsed_stories = []
    for story in stories:
        title_element = story.find_element(By.CSS_SELECTOR, "a.stitle")
        title = title_element.text
        link = BASE_URL + title_element.get_attribute("href")
        author_element = story.find_element(By.CSS_SELECTOR, "a[href*='/u/']")
        author = author_element.text
        author_link = BASE_URL + author_element.get_attribute("href")
        summary = story.find_element(By.CSS_SELECTOR, "div.z-indent.z-padtop").text
        stats_element = story.find_element(By.CSS_SELECTOR, "div.z-padtop2.xgray").text

        stats_dict = parse_stats(stats_element)

        parsed_stories.append(
            {
                "title": title,
                "link": link,
                "author": author,
                "author_link": author_link,
                "summary": summary.split("Rated:")[0],
                **stats_dict,
            }
        )

    return parsed_stories


def main(save_path: str, parse_start_page: int = 1, parse_end_page: int = 5) -> None:
    template_page_url = BASE_URL + "/book/Harry-Potter/?&srt=1&r=103&p={}"

    all_fanfics = []

    tqdm_bar = tqdm(total=parse_end_page - parse_start_page + 1, position=0, desc="Parsing pages")

    for page_num in range(parse_start_page, parse_end_page + 1):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        temp_url = template_page_url.format(page_num)
        driver.get(temp_url)

        stories = parse_fanfiction_page(driver)
        all_fanfics.extend(stories)

        df = pd.DataFrame(all_fanfics)
        df.to_csv(save_path, index=False)

        driver.quit()
        tqdm_bar.update(1)

    print("Data saved to {}.".format(save_path))


if __name__ == "__main__":
    main(save_path="fanfics.csv", parse_start_page=1, parse_end_page=5)
