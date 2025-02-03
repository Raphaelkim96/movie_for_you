from selenium import webdriver # 모든 브라우저
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import re
import time
import datetime
# import pyautogui
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
options.add_argument('user_agent=' + user_agent)
options.add_argument('lang=ko_KR')

service = ChromeService(executable_path=ChromeDriverManager().install()) # 브라우저 install
driver = webdriver.Chrome(service=service, options=options)

category = ['Titles', 'Review']

def open_in_new_tab(driver, element):
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[-1])

def url_init():
    url = 'https://m.kinolights.com/discover/explore'
    driver.get(url)
    time.sleep(1)

    # 영화/TV 버튼 클릭
    # 버튼 찾기 및 스크롤
    button_xpath4 = "#contents > section > div.media-type-btn-wrap > div > div > div:nth-child(4) > button"
    button = driver.find_element(By.CSS_SELECTOR, button_xpath4)
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    # JavaScript로 클릭 시도
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)  # 페이지 로딩 대기

    # 영화 선택 클릭
    button_xpath5 = '//*[@id="contents"]/section/div[4]/div[2]/div[1]/div[3]/div[2]/div[2]/div/button[1]'   # 영화 선택
    # button_xpath5 = '//*[@id="contents"]/section/div[4]/div[2]/div[1]/div[3]/div[2]/div[2]/div/button[2]' # tv 선택
    driver.find_element(By.XPATH, button_xpath5).click()
    time.sleep(2)  # 페이지 로딩 대기

    #작품 보기 클릭
    button_xpath6 = '//*[@id="applyFilterButton"]/span'
    driver.find_element(By.XPATH, button_xpath6).click()
    time.sleep(2)  # 페이지 로딩 대기

    #인기순 클릭
    button_xpath7 = "#contents > div > div > div.movie-list-title-wrap > button > span"
    button = driver.find_element(By.CSS_SELECTOR, button_xpath7)
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    # JavaScript로 클릭 시도
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)  # 페이지 로딩 대기

    # 리뷰순 클릭
    button_xpath8 = "#root > div > div.modal-layer > div > div > ul > li:nth-child(4) > span"
    button = driver.find_element(By.CSS_SELECTOR, button_xpath8)
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    # JavaScript로 클릭 시도
    driver.execute_script("arguments[0].click();", button)
    time.sleep(2)  # 페이지 로딩 대기

    # for _ in range(32):  # 32번 페이지 다운 시도 영화500개
    for _ in range(22):  # 32번 페이지 다운 시도 영화500개
        # 페이지의 body 요소를 찾아서 PAGE_DOWN 키를 보냄
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)

for z in range(1):

    df_titles = pd.DataFrame()
    url_init()

    for i in range(1,505):
    # for i in range(1,3):
        titles = []
        reviews = []

        button_xpath = '//*[@id="contents"]/div/div/div[3]/div[2]/div[{}]/a/div/div[1]/div[1]/img'.format(i)
        button_xpath1 = '//*[@id="review"]'
        button_xpath3 = '//*[@id="content__body"]/div'

        element = driver.find_element(By.XPATH, button_xpath)
        open_in_new_tab(driver, element)
        time.sleep(1)

        try:
            additional_button_xpath = '//*[@id="contents"]/div[2]/div/section[2]/div/div/div[2]/button'
            additional_button = driver.find_element(By.XPATH, additional_button_xpath)
            additional_button.click()
            time.sleep(1)

            additional_button_xpath = '//*[@id="contents"]/div[2]/div/section[2]/div/div/div/button'
            additional_button = driver.find_element(By.XPATH, additional_button_xpath)
            additional_button.click()
            time.sleep(1)

            additional_button_xpath = '//*[@id="contents"]/div[2]/div/section[2]/div/div/div/button'
            additional_button = driver.find_element(By.XPATH, additional_button_xpath)
            additional_button.click()
            time.sleep(1)

            additional_button_xpath = '//*[@id="contents"]/div[2]/div/section[2]/div/div/div/button'
            additional_button = driver.find_element(By.XPATH, additional_button_xpath)
            additional_button.click()
            time.sleep(2)


            driver.refresh()
            time.sleep(3)

            button_xpath_popup = '//*[@id="contents"]/div[2]/div/section[3]/div/div[1]/a/h2'
            driver.find_element(By.XPATH, button_xpath_popup).click()
            time.sleep(1)
            # input("{}번째 반복에서 멈췄습니다. 계속하려면 Enter를 누르세요...".format(i))

            url_init()

            element = driver.find_element(By.XPATH, button_xpath)
            open_in_new_tab(driver, element)
            time.sleep(2)
            # input("{}번째 반복에서 멈췄습니다. 계속하려면 Enter를 누르세요...".format(i))
            pass
        except:
            # 버튼이 없으면 그냥 넘어감
            pass

        driver.find_element(By.XPATH, button_xpath1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, button_xpath3).click()
        time.sleep(1)

        # 특정 버튼 존재 여부 확인 및 클릭
        try:
            additional_button_xpath = '//*[@id="contents"]/div[2]/div/section[2]/div/div/div[2]/button'
            additional_button = driver.find_element(By.XPATH, additional_button_xpath)
            additional_button.click()
            time.sleep(1)
        except:
            # 버튼이 없으면 그냥 넘어감
            pass

        title_xpath = '//*[@id="contents"]/div[1]/div[2]/div[1]/div[1]/h2'


        try :
            title = driver.find_element(By.XPATH,title_xpath).text
            title = re.compile('[^가-힣 ]').sub('', title)
            titles.append(title)
            print(i)
        except: #예외처리
            print('i')
            print(i)


        # 스크롤 다운
        for _ in range(5):  # 5번 리뷰 페이지 다운 시도
            # 페이지의 body 요소를 찾아서 PAGE_DOWN 키를 보냄
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(1)

        for j in range(1,51):
        # for j in range(1, 2):
            try:
                review_xpath = '//*[@id="contents"]/div[5]/section[2]/div/article[{}]/div[3]/a/h5'.format(j)
                review = driver.find_element(By.XPATH, review_xpath).text
                review = re.compile('[^가-힣 ]').sub('', review)
                reviews.append(review)
            except:
                print("j")
                print(j)
        # 현재 탭(새로 열린 탭) 닫기
        driver.close()

        # 원래 탭으로 돌아가기
        driver.switch_to.window(driver.window_handles[0])

        # 각 영화마다 제목과 리뷰를 매칭하여 데이터프레임 생성
        data = {
            'Title': [title] * len(reviews),  # 리뷰 개수만큼 제목 반복
            'Review': reviews
        }
        df_section = pd.DataFrame(data)
        df_titles = pd.concat([df_titles, df_section], ignore_index=True)

    print(df_titles.head())
    df_titles.info()
    #print(df_titles['category'].value_counts())
    # df_titles.to_csv('./crawling_data/movie_{}_{}.csv'.format(z,
    df_titles.to_csv('./crawling_data/tv_{}_{}.csv'.format(z,
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