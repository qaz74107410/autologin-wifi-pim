import time
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

from config import my_username, my_password

app_version = 0.3
retry = 0
islogin = False

# URL of PIMHotspot
# url = "http://172.23.65.12/guest/PIMHotspot.php"
# url = "https://1.1.1.1/login.html"
url = "http://1.1.1.1/login.html"

# web id element find by name
username_name = "username"
password_name = "password"
submit_name = "Submit"

# max wait time check (sec)
MAX_WAIT = 1
MAX_RETRY = 2

# in case PIM redirect
expected_titles = ["Logged In","Panyapiwat"]

# silent driver running 
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-urlfetcher-cert-requests')
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# if chromedriver is not in your path, you’ll need to add it here
driver = webdriver.Chrome(options=options) 

driver.get(url)
print("-- Auto PIMHotspot login --")
print("version : " + str(app_version))


while retry < MAX_RETRY and not islogin :
  driver.find_element_by_name(username_name).send_keys(my_username)
  driver.find_element_by_name(password_name).send_keys(my_password)

  # select element in from then submit
  driver.find_element_by_name(submit_name).click()

  for index, et in enumerate(expected_titles):

    try:  
      WebDriverWait(driver, MAX_WAIT).until(EC.title_contains(et))
      islogin = True
      if islogin : break
    except Exception as e:
      pass

  retry += 1

driver.quit()

if islogin is True:
  print("Login successful. Exiting...")
else: 
  print("Unable to login. Please try again")

time.sleep(3)