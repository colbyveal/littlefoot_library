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


def test_e2e_SUCCESS():
    #Submit new record
    web_records = {}

    prev_report = library_data_collection.process_report(library_data_collection.load_data('Records/web_records.json'))
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
    window1= driver.window_handles[1]
    driver.switch_to.window(window1)
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))

    #Query web_records list
    web_records = library_data_collection.load_data('Records/web_records.json')
    assert result.text == "{'Title': 'book title', 'Author': 'book author', 'Pages': '111', 'DDC': '987testddc', 'Read': 'Read'}"

    #Run report
    report = library_data_collection.process_report(web_records)
    prev_total = prev_report['Total Pages Read : ']
    new_total = report['Total Pages Read : ']
    assert (int(new_total) - int(prev_total)) == 111