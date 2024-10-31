import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep


class Dow():
    def art_inf(self, driver, index1, list11):
        sleep(5)
        driver.implicitly_wait(20)
        try:
            xpath_au = '//*[@id="sb-1"]/div'
            text_au = driver.find_element(By.XPATH, xpath_au).text
        except:
            text_au = ''
        try:
            xpath_time = '//*[@id="pb-page-content"]/div/main/article/div/div[2]/div[2]/span[1]/span[2]'
            text_time = driver.find_element(By.XPATH, xpath_time).text
        except:
            text_time = ''
        try:
            if index1 == 0:
                xpath_abs = '//*[@id="pb-page-content"]/div/main/article/div/div[2]/div[3]/div/div[2]'
            else:
                xpath_abs = '//*[@id="pb-page-content"]/div/main/article/div/div[2]/div[3]/div/div[1]/div[2]/p[1]'
            text_abs = driver.find_element(By.XPATH, xpath_abs).text
        except:
            text_abs = ''

        try:
            xpath_vo = '//*[@id="pane-pcw-details"]//h2[@class="volume--title"]'
            text_vo = driver.find_element(By.XPATH, xpath_vo).text
        except:
            text_vo = ''
        try:
            xpath_me1 = '//*[@id="pane-pcw-details"]//div[@class="download-count-container"]'
            text_me1 = driver.find_element(By.XPATH, xpath_me1).text
            xpath_me2 = '//*[@id="ref_count"]'
            text_me2 = driver.find_element(By.XPATH, xpath_me2).text
            text_metrics = text_me1 + '\n' + text_me2
        except:
            text_metrics = ''

        try:
            if index1 == 0:
                text_keywords = ''
            else:
                text_keywords = ''
                xpath_keywords = '//*[@id="pane-pcw-details"]/section[2]/div/ul'
                nums = len(driver.find_element(By.XPATH, xpath_keywords).find_elements(By.XPATH, "./li"))
                for num1 in range(1, nums + 1):
                    xpath_word = '//*[@id="pane-pcw-details"]/section[2]/div/ul/li[{}]/a'.format(num1)
                    text_word = driver.find_element(By.XPATH, xpath_word).text
                    text_keywords = text_keywords + ' ; ' + text_word
        except:
            text_keywords = ''
