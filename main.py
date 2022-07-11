# open chrome and go to the url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from time import sleep

other_url = 'https://www.google.ca/search?q=Placeholder&hl=en&tbm=isch&source=hp&biw=1249&bih=1247&ei=HlXLYofnKoSH0PEPjvO1iA8&iflsig=AJiK0e8AAAAAYstjLnLNCiCQlFp8kfpk4ajzUSxbDcP3&ved=0ahUKEwiH7s7cse_4AhWEAzQIHY55DfEQ4dUDCAc&uact=5&oq=Placeholder&gs_lcp=CgNpbWcQA1AVWCNgPWgAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img'
driver = webdriver.Chrome('D:\\chromedriver.exe')
driver.get(other_url)
driver.implicitly_wait(10)
Input_Path = 'C:\\DATA\\DATA_UPLOAD_MOREDATA'  # Input Directory

for dirpath, dirnames, filenames in os.walk(Input_Path):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)

    for filename in filenames:
        driver.get(other_url)
        full_path = os.path.join(dirpath, filename)
        print(dirpath)
        driver.find_element(By.XPATH, '//*[@id="sf"]/div[1]/div[2]/div/div[3]/div[1]/span').click()
        driver.find_element(By.XPATH, '//*[@id="kO001e"]/div[2]/div/div[1]/div/div/div[3]/form/div[1]/div[1]/a').click()
        sleep(2)
        try:
            driver.find_element(By.XPATH, '//*[@id="kO001e"]/div[2]/div/div[1]/div/div[1]/div[3]/form/div[2]/div[2]/input').send_keys(full_path)
            driver.find_element(By.XPATH, '//*[@id="rso"]/div[2]/div/div[2]/g-section-with-header/div[1]/title-with-lhs-icon/a/div[2]/h3').click()
            for i in range(1, 4):
                driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img').screenshot(f'{dirpath}\\{filename}({i}).jpg')
        except:
            pass
