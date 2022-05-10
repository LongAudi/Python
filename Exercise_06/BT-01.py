from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import pandas as pd
from pandas import ExcelWriter
from time import sleep

path_INPUT = "D:\BTPython\Exercise_06\Input.xlsx"
sheet_INPUT = "Sheet1"

#Xóa những task cũ
# def Clear():
#     os.system("taskkill /f /im chromedriver.exe")
#     os.system("taskkill /f /im chrome.exe")

#Mở excel sử dụng thư viện pandas
def Read_Excel(path,sheet):
    df_INPUT = pd.read_excel(open(path,'rb'), sheet_name = sheet, dtype = object)
    return df_INPUT

#Mở trình duyệt chromedriver sử dụng selenium
def Open_Browser():
    driver = webdriver.Chrome(executable_path=os.path.abspath("C:\chromedriver.exe"))
    return driver

#Hàm xử lý chính
def Process_Main():
    df_INPUT = Read_Excel(path_INPUT,sheet_INPUT)
    print(df_INPUT)
    driver = Open_Browser()
    for idx_INPUT, row_INPUT in df_INPUT.iterrows():
        Input_Q = row_INPUT['Quận-Huyện']
        driver.get('https://thongtindoanhnghiep.co/')
        element = driver.find_element_by_xpath('//*[@id="TinhThanhIDValue"]')
        list_OPTIONS = element.find_elements_by_tag_name("option")
        for option in list_OPTIONS:
            if str(option.text) == "Đà Nẵng":
                option.click()
                sleep(5)
                element = driver.find_element_by_xpath('//*[@id="QuanHuyenIDValue"]')
                list_OPTIONSQ = element.find_elements_by_tag_name("option")
                for option in list_OPTIONSQ:                    
                    if str(option.text).strip() == str(Input_Q).strip():
                        option.click()
                        btn_submit = driver.find_element_by_xpath('//*[@id="fulltextSearch"]/div/section[4]/button')
                        btn_submit = driver.execute_script("arguments[0].click()", btn_submit)
                        list_URLS = driver.find_elements_by_xpath('/html/body/div[2]/div[3]/div[5]/div[1]/div[*]/div/h2/a')
                        for idx_url, i_url in enumerate(list_URLS):
                            driver1 = Open_Browser()
                            driver1.get(i_url.get_attribute("href"))
                            driver1.save_screenshot("./Exercise_06/Output\\Output"+str(idx_url)+"_screenshot.png")
                            driver1.quit()        
    driver.quit()

#Phần thực thi
if __name__ == "__main__":
    print ("Bắt đầu quy trình")
    # Clear()
    Process_Main()
    print ("Kết thúc quy trình")