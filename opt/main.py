from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import date
from time import sleep
import sys
import userdata

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://teamspirit-5041.cloudforce.com/')
# ユーザによってURLが異なる可能性
#driver.get('https://teamspirit-5041--teamspirit.ap0.visual.force.com/apex/AtkWorkTimeView?sfdc.tabName=01r10000000P9eo')
sleep(2)

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(userdata.name)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(userdata.password)
driver.find_element(By.CSS_SELECTOR, "#Login").click()
sleep(3)

driver.find_element(By.CLASS_NAME, "wt-勤務表").click()
dt = date.today()

sleep(3)

# 今日まで
# diff_count = date.today().day + 1
# for day_count in range(1,diff_count):
# 月末まで
for day_count in range(1,32):
    sleep(1)
    try:
        # 項目が1つのみ場合の記述。項目が複数ある場合は変更する必要がある。
        driver.find_element(By.ID, "dailyWorkCell" + str(dt.year) + "-" + str(dt.month) + "-" + str(day_count).zfill(2)).click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#empWorkSlider0 > tbody > tr:nth-child(2) > td:nth-child(4) > div").click()
        driver.find_element(By.CSS_SELECTOR, "#empWorkLock0").click()
        driver.find_element(By.CSS_SELECTOR, "#empWorkOk").click()
        sleep(2)
        print("[day " + str(day_count) + "] [complete]")
    except:
        try:
            driver.find_element(By.CSS_SELECTOR, "#empWorkCancel").click()
        except:
            print("[day " + str(day_count) +  "] [skip] button missing")
            continue
        print("[day " + str(day_count) + "] [skip] already max?")
        continue

driver.close()
sys.exit()
