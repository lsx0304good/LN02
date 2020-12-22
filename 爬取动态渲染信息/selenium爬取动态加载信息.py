from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

try:
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://item.jd.com/12353915.html')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "m-item-inner")))
    name_div = driver.find_element_by_css_selector('#name').find_elements_by_tag_name('div')
    summary_price = driver.find_element_by_id('summary-price')
    print('商品标题：')
    print(name_div[0].text)
    print('宣传语：')
    print(name_div[1].text)
    print('编著信息：')
    print(name_div[4].text)
    print('价格信息：')
    print(summary_price.text)
    driver.quit()
except Exception as e:
    print('显示异常信息！', e)

