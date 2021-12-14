import pytest
import json
import library_data_collection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=s, options=options)

def pytest_sessionstart(session):
    WEB_RECORDS = library_data_collection.load_data('Records/web_records.json')


def test_submitButton_SUCCESS():
    #driver = setup_driver()
    url = 'http://127.0.0.1:5000/'
    driver.get(url)

    page_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page_count_input")))
    page_count.clear()
    page_count.send_keys("111")

    ddc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dewey_decimal_input")))
    ddc.clear()
    ddc.send_keys("987testddc")

    submit = driver.find_element(By.ID, "submit_button")
    submit.click()

    #new window opens and gets focus containing submitted json object
    window1= driver.window_handles[1]
    driver.switch_to.window(window1)
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))
    assert driver.current_url == url + 'submit_action'
    assert result.text == "{'Title': 'book title', 'Author': 'book author', 'Pages': '111', 'DDC': '987testddc', 'Read': 'Read'}"

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_submitButton_invalidDDC_NEGATIVE():
    #driver=setup_driver()
    url = 'http://127.0.0.1:5000/'
    driver.get(url)

    page_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "page_count_input")))
    page_count.clear()
    page_count.send_keys("111")

    submit = driver.find_element(By.ID, "submit_button")
    submit.click()

    #new window opens and gets focus containing submitted json object
    window1= driver.window_handles[1]
    driver.switch_to.window(window1)
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "Body")))
    assert driver.current_url == url + 'submit_action'
    assert result.text == '"400: DDC not valid"'

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_submitButton_invalidPageNumber_NEGATIVE():
    #driver=setup_driver()
    url = 'http://127.0.0.1:5000/'
    driver.get(url)

    ddc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dewey_decimal_input")))
    ddc.clear()
    ddc.send_keys("987testddc")

    submit = driver.find_element(By.ID, "submit_button")
    submit.click()

    #new window opens and gets focus containing submitted json object
    window1= driver.window_handles[1]
    driver.switch_to.window(window1)
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "Body")))
    assert driver.current_url == url + 'submit_action'
    assert result.text == '"400: Please ensure you have entered a number in the Pages field"'

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def test_runReport_SUCCESS():
    result_string = ''
    url = 'http://127.0.0.1:5000/report'
    driver.get(url)

    report = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "report_table")))
    report_text = report.text
    assert report_text.startswith('Total Pages Read')

   

def pytest_sessionfinish(session, exitstatus):
    self.driver.quit()
    with open('Records/web_records.json', 'w') as f:
        json.dump(WEB_RECORDS,f,indent=4)
          



