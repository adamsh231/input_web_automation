# %%
from simpeg import loginSimpeg, tambahJabatanByNIP
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("E:\Programs/chromedriver.exe")

# %%
loginSimpeg(driver, "nurohman", "123456")

# %%
tambahJabatanByNIP(time, driver, nip=197211092007011010)


# %%
import os
import sys

os.path.dirname(sys.executable)

# %%
