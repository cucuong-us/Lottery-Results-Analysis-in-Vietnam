import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd
from bs4 import BeautifulSoup
import regex as re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def crawl_xoso_miennam(a_number_times = 1):
    # Cấu hình trình duyệt
    options = Options()
    options.add_argument("--headless")  # chạy nền
    driver = webdriver.Chrome(service=Service(), options=options)

    # Mở trang
    driver.get("https://az24.vn/xsmn-sxmn-xo-so-mien-nam.html")
    time.sleep(3)  # đợi trang load

    # Bấm nút "Xem thêm" vài lần
    for i in range(a_number_times):  # có thể điều chỉnh số lần bấm
        try:
            xem_them = driver.find_element(By.CLASS_NAME, "btn-see-more")
            driver.execute_script("arguments[0].click();", xem_them)
            time.sleep(2)  # đợi dữ liệu load
        except Exception as e:
            print("Không tìm thấy nút hoặc đã hết dữ liệu.")
            break

    # Lấy HTML sau khi đã bấm
    html = driver.page_source
    driver.quit()

    # Regex lấy các khối dữ liệu kết quả
    pattern = r'(\d{1,2}-\d{1,2}-\d{4}</a>.*?<b></b>)'
    matches = re.findall(pattern, html, flags=re.DOTALL)

    dates = []
    names = []
    numbers = []

    for match in matches:
        date = re.findall(r'(\d{1,2}-\d{1,2}-\d{4})', match)
        date = list(set(date))  # lấy unique ngày

        title = re.findall(r'title="(.*?)"', match)
        index = match.find('class="v-g8 "')
        data = match[index:]
        number = np.array(re.findall(r'(\d{2,6})', data))  

        idx = np.arange(len(number))
        for i in range(len(title)):
            dates.append(date[0] if date else None)
            names.append(title[i])
            numbers.append(number[idx % (len(title)) == i])

    # Tạo DataFrame
    df = pd.DataFrame({
        'provinece': names,
        'date': dates,
        'lottery_number': numbers
    })
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
    df = df.dropna(subset=['date'])
    df = df.sort_values(by='date', ascending=False)

    return df
