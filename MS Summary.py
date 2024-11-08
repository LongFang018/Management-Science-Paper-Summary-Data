import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


class Dow():
    def art_inf(self, driver, index1, list11):
        # 获取文章的具体信息
        sleep(5)
        driver.implicitly_wait(20)
        try:
            # 1.author
            xpath_au = '//*[@id="sb-1"]/div'
            text_au = driver.find_element(By.XPATH, xpath_au).text
        except:
            text_au = ''
        try:
            # 2.published time
            xpath_time = '//*[@id="pb-page-content"]/div/main/article/div/div[2]/div[2]/span[1]/span[2]'
            text_time = driver.find_element(By.XPATH, xpath_time).text
        except:
            text_time = ''
        try:
            # 3.summary
            if index1 == 0:
                xpath_abs = '//*[@id="pb-page-content"]/div/main/article/div/div[2]/div[3]/div/div[2]'
            else:
                xpath_abs = '//*[@id="pb-page-content"]/div/main/article/div/div[2]/div[3]/div/div[1]/div[2]/p[1]'
            text_abs = driver.find_element(By.XPATH, xpath_abs).text
        except:
            text_abs = ''

        try:
            # 4.Volume
            xpath_vo = '//*[@id="pane-pcw-details"]//h2[@class="volume--title"]'
            text_vo = driver.find_element(By.XPATH, xpath_vo).text
        except:
            text_vo = ''
        try:
            # 5.Metrics
            xpath_me1 = '//*[@id="pane-pcw-details"]//div[@class="download-count-container"]'
            text_me1 = driver.find_element(By.XPATH, xpath_me1).text
            xpath_me2 = '//*[@id="ref_count"]'
            text_me2 = driver.find_element(By.XPATH, xpath_me2).text
            text_metrics = text_me1 + '\n' + text_me2
        except:
            text_metrics = ''

        try:
            # 6.Keywords
            if index1 == 0:
                text_keywords = ''
            else:
                text_keywords = ''
                xpath_keywords = '//*[@id="pane-pcw-details"]/section[2]/div/ul'
                nums = len(driver.find_element(By.XPATH, xpath_keywords).find_elements(By.XPATH, "./li"))
                # Get all articles on the current page
                for num1 in range(1, nums + 1):
                    xpath_word = '//*[@id="pane-pcw-details"]/section[2]/div/ul/li[{}]/a'.format(num1)
                    text_word = driver.find_element(By.XPATH, xpath_word).text
                    text_keywords = text_keywords + ' ; ' + text_word
        except:
            text_keywords = ''

        # Add the information of each article into the table, renamed here
        books = pd.read_excel('MS_6911.xlsx')
        books.loc['Aggregation'] = [list11[1], text_au, text_time, list11[0], text_abs, text_vo, text_metrics, text_keywords]
        books.to_excel('MS_6911.xlsx', index=False)

    def magezine_pro(self):
        option = webdriver.ChromeOptions()
        option.add_argument('window-size=1920x1080')
        option.add_argument('--disable-gpu')
        option.add_argument('--hide-scrollbars')
        option.add_argument('--disable-infobars')
        driver = webdriver.Chrome(options=option)
        # Change Website here
        driver.get('https://pubsonline.informs.org/toc/mnsc/69/11')
        sleep(5)

        driver.implicitly_wait(20)
        # Number of Papers
        str_xpath = '//*[@id="pb-page-content"]/div/main/div[3]//div[1][@class="table-of-content"]'  # 所有评论个数
        page_nums = len(driver.find_element(By.XPATH, str_xpath).find_elements(By.XPATH, "./div"))
        print(page_nums)
        try:
            xpath1 = '//*[@id="hs-eu-confirmation-button"]'
            # click accept
            driver.find_element(By.XPATH, xpath1).click()
        except:
            pass
        # main window
        href_list = []
        # articles on the current page
        for art_num in range(1, page_nums+1):
            xpath_tittle = '//*[@id="pb-page-content"]/div/main//div[{}][@class="issue-item"]/h5/a'.format(art_num)
            # Link and Title
            href1 = driver.find_element(By.XPATH, xpath_tittle).get_attribute("href")
            tittle1 = driver.find_element(By.XPATH, xpath_tittle).text
            href_list.append([href1, tittle1])

        driver.quit()
        sleep(2)
        # Click each link to generate info
        for index1, list11 in enumerate(href_list):
            print('第{}个文章'.format(index1 + 1))
            option = webdriver.ChromeOptions()
            option.add_argument('window-size=1920x1080')
            option.add_argument('--disable-gpu')
            option.add_argument('--hide-scrollbars')
            option.add_argument('--disable-infobars')
            driver = webdriver.Chrome(options=option)
            driver.get(list11[0])
            # enter article page
            self.art_inf(driver, index1, list11)
            driver.quit()
            sleep(1)


if __name__ == "__main__":
    # create a new sheet, change name here!
    books = pd.DataFrame(columns=['Title', 'Author', 'Published Time', 'Link', 'Abstract', 'Volume', 'Metrics', 'Keywords'])
    books.to_excel('MS_6911.xlsx', index=False)
    # start to scrap
    Dow().magezine_pro()
