import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

# 設定下載路徑
download_dir = "E:\土城長庚醫院\PanelA"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
    
options = webdriver.ChromeOptions()

# 設定下載路徑和開啟自動下載
options.add_experimental_option("prefs", {
  "download.default_directory": download_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
webdriver_chrome_path = './chromedriver'
service = Service(executable_path=webdriver_chrome_path)
driver = webdriver.Chrome(service=service,chrome_options=options)
#get web address
driver.get("https://cid.orthoclinicaldiagnostics.com/")
#setting waiting index
wait = WebDriverWait(driver, 10)
#wait validationCustom01 & send_keys(account)
id = driver.find_element(By.ID,"validationCustom01")
id.send_keys("__________")
#click btn "next" & send_keys(password)
next_btn = driver.find_element(By.ID, "next")
next_btn.click()
pw = driver.find_element(By.CLASS_NAME, "form-control1")
pw.send_keys("__________")
#click login btn(因為"next" & "login"兩個ID是一樣的，所以不用另外find_element)
next_btn.click()
sleep(6)
##登入完成，重新導向
# eantigram 
driver.get("https://orthoplus.orthoclinicaldiagnostics.com/eAntigram/App/default.aspx?culture=zh-tw")
sleep(6)
#product
product_cbb = Select(driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlProduct"))
product_cbb.select_by_value("10")
sleep(2)
#press search
srch_btn = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnSearch")
srch_btn.click()
# driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/form/div[3]/button').click()
#check <tr> column amount
table = driver.find_elements(By.XPATH,"//table[@id='ctl00_ContentPlaceHolder1_dgDocumentList']/tbody/tr")
total_rows = len(table) - 1

pdfnamelst = [
    "ctl00$ContentPlaceHolder1$dgDocumentList$ctl03$btnViewPDF",
    "ctl00$ContentPlaceHolder1$dgDocumentList$ctl04$btnViewPDF",
    "ctl00$ContentPlaceHolder1$dgDocumentList$ctl05$btnViewPDF",
    "ctl00$ContentPlaceHolder1$dgDocumentList$ctl06$btnViewPDF",
    "ctl00$ContentPlaceHolder1$dgDocumentList$ctl07$btnViewPDF",
    "ctl00$ContentPlaceHolder1$dgDocumentList$ctl08$btnViewPDF"
    ]
sleep(3)
for i in range(0,total_rows):
    srch_btn = driver.find_element(By.NAME, pdfnamelst[i])
    srch_btn.click()
    alert = wait.until(EC.alert_is_present())
    alert.accept()
sleep(4)