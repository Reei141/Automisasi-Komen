import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Konfigurasi opsi browser
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

# Jalankan browser
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# Akses Halaman login
driver.get("https://instagram.com")
time.sleep(5)

# Isi form Login
driver.find_element(By.NAME, "username").send_keys("ISI USN KALIAN")
driver.find_element(By.NAME, "password").send_keys("ISI PASS KALIAN")
time.sleep(10)

# Klik tombol login
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]').click()
time.sleep(10)

# Akses postingan 1
driver.get("isi dengan link postingan instagram")
time.sleep(5)

comment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
comment_button.click()
time.sleep(2)  

fresh_comment_area = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
fresh_comment_area.send_keys("Wah keren banget!")
fresh_comment_area.send_keys(Keys.ENTER)
time.sleep(5)

# Akses postingan 2
driver.get("isi dengan link postingan instagram")
time.sleep(5)

comment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
comment_button.click()
time.sleep(2)  

fresh_comment_area = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
fresh_comment_area.send_keys("Wah keren banget!")
fresh_comment_area.send_keys(Keys.ENTER)
time.sleep(5)

# Akses postingan 3
driver.get("isi dengan link postingan instagram")
time.sleep(5)

comment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
comment_button.click()
time.sleep(2)  

fresh_comment_area = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
fresh_comment_area.send_keys("Wah keren banget!")
fresh_comment_area.send_keys(Keys.ENTER)
time.sleep(5)

# Akses postingan 4
driver.get("isi dengan link postingan instagram")
time.sleep(5)

comment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
comment_button.click()
time.sleep(2)  

fresh_comment_area = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
fresh_comment_area.send_keys("Wah keren banget!")
fresh_comment_area.send_keys(Keys.ENTER)

# Akses postingan 5
driver.get("isi dengan link postingan instagram")
time.sleep(5)

comment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
comment_button.click()
time.sleep(2)  

fresh_comment_area = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Add a comment…']")))
fresh_comment_area.send_keys("Wah keren banget!")
fresh_comment_area.send_keys(Keys.ENTER)
time.sleep(5)

time.sleep(5)
driver.quit()
