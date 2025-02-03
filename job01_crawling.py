from selenium import webdriver # 모든 브라우저
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import re
import time
import datetime
import pyautogui
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
options.add_argument('user_agent=' + user_agent)
options.add_argument('lang=ko_KR')

service = ChromeService(executable_path=ChromeDriverManager().install()) # 브라우저 install
driver = webdriver.Chrome(service=service, options=options)

# category = ['Politics']
#category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
category = ['Titles', 'Review']


# df_titles = pd.DataFrame()
for z in range(1):

    url = 'https://m.kinolights.com/discover/explore'
    driver.get(url)
    # button_xpath = '//*[@id="newsct"]/div[4]/div/div[2]' #id가 newsct요소에 있는 div태그4번쨰-div-div2번
    # button_xpath1 = '//*[@id="newsct"]/div[5]/div/div[2]'  # id가 newsct요소에 있는 div태그4번쨰-div-div2번



    time.sleep(1)
    # for i in range(15):
    #     time.sleep(0.5)
    #     if url == 'https://news.naver.com/section/101':
    #         driver.find_element(By.XPATH, button_xpath1).click()
    #     else :
    #         driver.find_element(By.XPATH, button_xpath).click()


    for i in range(1,3):

        df_titles = pd.DataFrame()
        url = 'https://m.kinolights.com/discover/explore'
        driver.get(url)
        time.sleep(1)

        titles = []
        reviews = []
        button_xpath = '//*[@id="contents"]/div/div/div[3]/div[2]/div[{}]/a/div/div[1]/div[1]/img'.format(i)
        button_xpath1 = '//*[@id="review"]'
        button_xpath3 = '//*[@id="content__body"]/div'

        driver.find_element(By.XPATH, button_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, button_xpath1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, button_xpath3).click()
        time.sleep(1)

        title_xpath = '//*[@id="contents"]/div[1]/div[2]/div[1]/div[1]/h2'

        try :
            title = driver.find_element(By.XPATH,title_xpath).text
            title = re.compile('[^가-힣 ]').sub('', title)
            titles.append(title)
            #print(title)
        except: #예외처리
            print('i')
            print(i)


        # 스크롤 다운

        for _ in range(5):  # 5번 페이지 다운 시도
            # 페이지의 body 요소를 찾아서 PAGE_DOWN 키를 보냄
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(1)




        for j in range(1,51):

            try:
                review_xpath = '//*[@id="contents"]/div[5]/section[2]/div/article[{}]/div[3]/a/h5'.format(j)
                review = driver.find_element(By.XPATH, review_xpath).text
                review = re.compile('[^가-힣 ]').sub('', review)
                reviews.append(title)
            except:
                print("j")
                print(j)



        df_section_titles = pd.DataFrame(titles, columns=['Titles'])  # 데이터프레임 생성
        df_section_reviews = pd.DataFrame(reviews, columns=['Reviews'])  # 데이터프레임 생성
        #df_section_titles['category'] = category[z]  # 카테고리 라벨 붙이기
        df_titles = pd.concat([df_section_titles, df_section_reviews], axis='rows', ignore_index=True)  # 빈 데이터프레임에 row정장

    print(df_titles.head())
    df_titles.info()
    #print(df_titles['category'].value_counts())
    df_titles.to_csv('./crawling_data/movie_{}_{}.csv'.format(z,
    datetime.datetime.now().strftime('%Y%m%d')), index=False) # 나노second단위 받은 시간으로 오늘 날짜로 바꿔서 저장

time.sleep(30)
driver.close()

# '//*[@id="newsct"]/div[4]/div/div[1]/div[19]/ul/li[5]/div/div/div[2]/a/strong'
#
# # 재목 xpath
# '//*[@id="contents"]/div[1]/div[2]/div[1]/div[1]/h2'
#
# # 제목 버튼
# "//*[@id="contents"]/div/div/div[3]/div[2]/div[1]/a/div/div[1]/div[1]/img"
# '//*[@id="contents"]/div/div/div[3]/div[2]/div[2]/a/div/div[1]/div[1]/img'
# "//*[@id="contents"]/div/div/div[3]/div[2]/div[5]/a/div/div[1]/div[1]/img"
#
# # 리뷰 버튼
# '//*[@id="review"]'
#
# # 리뷰 내용
# '//*[@id="contents"]/div[5]/section[2]/div/article[1]/div[3]/a/h5'
# '//*[@id="contents"]/div[5]/section[2]/div/article[2]/div[3]/a/h5'
