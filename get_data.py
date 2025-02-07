from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, urllib.request
import string
import pandas as pd
import os

# Initialize the WebDriver
PATH = '/usr/local/bin/geckodriver'
service = Service(PATH)
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

# Function to login to Instagram
def login_instagram():
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    username.clear()
    password.clear()
    username.send_keys("latecig")
    password.send_keys("suraj.me")
    login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(10)
    

# Function to search and collect data
def search_and_collect_data(query):
    print("searching for: ", query)
    time.sleep(5)
    search_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Search']"))
    )
    search_icon.click()
    time.sleep(5)
    searchbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search']"))
    )
    searchbox.clear()
    searchbox.send_keys(query)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)
    # Locate the specific div and collect profile links within it
    search_results_div = driver.find_element(By.CSS_SELECTOR, "div.x6s0dn4.x78zum5.xdt5ytf.x5yr21d.x1odjw0f.x1n2onr6.xh8yej3")
    profile_links = search_results_div.find_elements(By.CSS_SELECTOR, "a.x1i10hfl")
    profile_urls = list(set([link.get_attribute('href') for link in profile_links]))   

    return profile_urls

# Function to collect profile data
def collect_profile_data(profile_url):
    driver.get(profile_url)
    time.sleep(5)
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[role='tab'][aria-selected='true']"))
        )
        is_private = False
    except:
        is_private = True

    if is_private:
        try:
            posts = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.x78zum5.x1q0g3np.xieb3on li:nth-child(1) span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
            ).text
        except:
            posts = None

        try:
            followers = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.x78zum5.x1q0g3np.xieb3on li:nth-child(2) span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
            ).text
        except:
            followers = None

        try:
            following = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul.x78zum5.x1q0g3np.xieb3on li:nth-child(3) span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
            ).text
        except:
            following = None
    else:
        try:
            posts = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
            ).text
        except:
            posts = None

        try:
            followers = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href$='/followers/'] span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
            ).text
        except:
            followers = None

        try:
            following = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href$='/following/'] span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs"))
            ).text
        except:
            following = None

    # Save profile picture
    try:
        profile_pic = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img.xpdipgo.x972fbf.xcfux6l.x1qhh985.xm0m39n.xk390pu.x5yr21d.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xl1xv1r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf.xh8yej3"))
        ).get_attribute('src')
    except:
        profile_pic = None

    try:
        user_id = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2.x1lliihq"))
        ).text
    except:
        user_id = None

    try:
        name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x1ji0vk5.x18bv5gf.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f.x5n08af.x10wh9bi.x1wdrske.x8viiok.x18hxmgj"))
        ).text
    except:
        name = None
    
    # Click on the "Options" button
    try:
        options_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "svg[aria-label='Options']"))
        )
        options_button.click()
    except:
        pass

    # Click on the "About this account" option
    try:
        about_this_account = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.xjbqb8w:nth-child(5)"))
        )
        about_this_account.click()
    except:
        pass

    # Extract "Date joined" information
    try:
        date_joined = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".wbloks_94 > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)"))
        ).text
    except:
        date_joined = None

    # Extract "Former usernames" information
    try:
        former_usernames = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label^='Former usernames'] span[data-bloks-name='bk.components.Text'][style*='font-size: 14px; color: rgb(168, 168, 168);']"))
        ).text
    except:
        former_usernames = None

    if profile_pic and user_id:
        profile_folder = os.path.join('Data', 'profiles', user_id)
        os.makedirs(profile_folder, exist_ok=True)
        profile_pic_path = os.path.join(profile_folder, 'profile_pic.jpg')
        urllib.request.urlretrieve(profile_pic, profile_pic_path)
    
    return {
        'user_id': user_id,
        'name': name,
        'posts': posts,
        'followers': followers,
        'following': following,
        'PVT': is_private,
        'date_joined': date_joined,
        'former_usernames': former_usernames
    }

# Login to Instagram
login_instagram()

# Create profiles and Data folders if they don't exist
os.makedirs('Data', exist_ok=True)
os.makedirs('Data/profiles', exist_ok=True)
# Initialize CSV file
csv_file = os.path.join('Data', 'instagram_data.csv')
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=['user_id', 'name', 'posts', 'followers', 'following', 'PVT', 'date_joined', 'former_usernames'])
    df.to_csv(csv_file, index=False)

# Read names from names.txt
with open('names.txt', 'r') as file:
    names = [line.strip() for line in file]

# Search and collect data for each name
for name in names:
    profile_urls = search_and_collect_data(name)
    for profile_url in profile_urls:
        profile_data = collect_profile_data(profile_url)
        
        # Append new data to CSV file
        df = pd.DataFrame([profile_data])
        df.to_csv(csv_file, mode='a', header=False, index=False)
        
        driver.back()  # Navigate back to the search results
        time.sleep(5)  # Wait for the page to load

# Quit the driver
driver.quit()