# PYTHON Example for WebScraping on OneLiners
from pkgutil import iter_importers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter
from time import sleep
import pandas
import sys
import os
import util


current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current)

CHROME_PATH = "chromeprofile/chromedriver.exe"
EL_ADDRESS = {
    "new_chat_el" : '//div[@title="Search input textbox"]',
    "attachment_el" : "//div[@title='Attach']",
    "doc_el" : "//input[@accept = '*']",
    "send_el" : "//span[@data-testid='send']"
}

# run chrome.exe on C:\selenium\chromeprofile with remote-debugging-port = 8515
def create_driver():
    chrome_option = webdriver.chrome.options.Options()
    chrome_option.add_experimental_option("debuggerAddress","127.0.0.1:8515")
    #Change chrome driver path accordingly
    created_driver = webdriver.Chrome(executable_path=CHROME_PATH)
    return created_driver

def open_attachment(driver,name_or_number):
    # driver.find_element_by_xpath(EL_ADDRESS["new_chat_el"]).send_keys(name_or_number,"\n")
    # finding new_chat_el and sending details
    el = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, EL_ADDRESS["new_chat_el"]))
    )
    el.send_keys(name_or_number,"\n")
    
    # print("attach finding")
    el = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, EL_ADDRESS["attachment_el"]))
    )
    el.click()
    # print("attach clicked")

def send_pdf(driver, saved_name, send_to):
    open_attachment(driver,send_to)
    
    # print("doc finding")
    doc_el = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, EL_ADDRESS["doc_el"]))
    )
    doc_el.send_keys(saved_name)
    # print("doc done")
    
    # print("send btn finding")
    el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, EL_ADDRESS["send_el"]))
    )
    el.click()
    # print("send clicked")
    sleep(1)
        
        

def connect_whatsapp(driver):
    try:
        driver.get("https:\\web.whatsapp.com")
        el = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, EL_ADDRESS["new_chat_el"]))
        )
    except Exception as err:
        print("Not connected Whatsapp")

def send_files(CSV_PATH, driver, log):
    try :         
        try:
            df = pandas.read_csv(CSV_PATH, index_col="Index")

            for index, row in df.iterrows():
                abs_path = os.path.join(current, f"saved_pdfs\{row['Name']}.pdf")
                send_pdf(driver, abs_path, row['Number'])
                log.insert(tkinter.END, f"\nfile sent to -> {row['Name'] }")

        except Exception as err:
            print(err.__cause__, err)
        else:
            pass
    except Exception as err: 
        print(f"\n\n\n !!!!! SOME ERROR !!!!!\n>       {err.__cause__}{err}")

    finally:
        print("Execution is done")
