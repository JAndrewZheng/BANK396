import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import random


def upload_youtube(PATH, video_desc):
    # Start the selenium bot
    bot = webdriver.Chrome()
    
    # Open the studio youtube page
    bot.get("https://studio.youtube.com")
    with open("test_key.txt") as f:
        username = f.readline().strip()
        password = f.readline().strip()
    
    f.close()
    
    #username = "imTESTING320@gmail.com"
    #password = "BANK396$"
    # Enter the username
    
    WebDriverWait(bot, 20).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@aria-label='Email or phone']"))).send_keys(username)
    #bot.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys(username)
    l = bot.find_elements(By.XPATH, "//button[@jscontroller='soHxf']")
    l[1].click()
    
    # Wait for password screen to show up
    time.sleep(5)
              
    # Enter the password
    bot.find_element(By.XPATH, "//input[@aria-label='Enter your password']").send_keys(password)
    l = bot.find_elements(By.XPATH, "//button[@jscontroller='soHxf']")
    l[1].click()
    
    # Wait for youtube studio to load 
    time.sleep(3)
    
    elements = bot.find_elements(By.XPATH, "//div[@class='DRfwgc shUNU']")
    second_security = len(elements) > 0
    
    if second_security and elements[0].text == 'You’re signed in':
        
        ele_class = "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 k97fxb yu6jOd"
        bot.find_elements(By.XPATH, "//button[@class='" + ele_class + "']").click()
        time.sleep(3)
        
    # Upload youtube video
    upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()
    
    # Wait for the upload screen to show up
    time.sleep(1)
    
    # Attach the youtube video as a file
    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    #simp_path = 'videos/{}'.format(str(nameofvid))
    #abs_path = os.path.abspath(simp_path)
    abs_path = os.path.abspath(PATH)
    file_input.send_keys(abs_path)
    
    time.sleep(7)
    
    next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    
    not_for_kids = bot.find_element(By.XPATH, '//*[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]')
    not_for_kids.click()
    
    # Type in a description in the description box
    description = bot.find_element(By.XPATH, '//*[@aria-label="Tell viewers about your video (type @ to mention a channel)"]')
    description.send_keys(video_desc)
    
    for i in range(3):
        next_button.click()
        time.sleep(1)
    
    bot.find_element(By.XPATH, '//*[@name="PRIVATE"]').click()
    
    done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)
    bot.quit()


def upload_tiktok(PATH, video_desc):
    option = webdriver.ChromeOptions()
    
    option.add_argument("--profile-directory=Default")
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument("window-size=1920,1000")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    
    bot = webdriver.Chrome(options = option)
    bot.get("https://www.tiktok.com/login")
    
    time.sleep(5)
    
    with open("key.txt") as f:
        username = f.readline().strip()
        password = f.readline().strip()
    
    f.close()
    
    elements = bot.find_elements(By.XPATH, "//div[@role='link']")
    
    element = elements[1]
    
    for id in elements:
        if id.text == "Continue with Google":
            element = id
    
    element.click()
    
    time.sleep(10)
    
    bot.switch_to.window(bot.window_handles[1])
    
    time.sleep(5)
    
    login = WebDriverWait(bot, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@aria-label='Email or phone']")))
    for char in username:
        time.sleep(random.randint(2500, 5000)/10000)
        login.send_keys(char)
    
    time.sleep(0.25)
    #bot.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys(username)
    l = bot.find_elements(By.XPATH, "//button[@jscontroller='soHxf']")
    l[1].click()
    
    # Wait for password screen to show up
    time.sleep(4)
              
    # Enter the password
    answer = bot.find_element(By.XPATH, "//input[@aria-label='Enter your password']")
    
    for char in password:
        time.sleep(random.randint(2500, 5000)/10000)
        answer.send_keys(char)
        
    time.sleep(0.25)
    l = bot.find_elements(By.XPATH, "//button[@jscontroller='soHxf']")
    l[1].click()
    
    time.sleep(10)
    
    bot.switch_to.window(bot.window_handles[0])
    
    time.sleep(2)
    
    bot.get("https://www.tiktok.com/creator#/upload?scene=creator_center")
    
    time.sleep(5)
    
    abs_path = os.path.abspath(PATH)
    bot.find_element(By.XPATH, "//input[@type='file']").send_keys(abs_path)
    
    time.sleep(2)
    
    bot.execute_script("window.scrollTo(0, 1000)")
    
    time.sleep(3)
    
    post = bot.find_element(By.XPATH, "//button[@class='css-y1m958']").send_keys(abs_path)
    post.click()


# +
def upload_instagram(PATH, video_desc):
                     
    with open("test_key.txt") as f:
        username = f.readline().strip()
        password = f.readline().strip()
    
    f.close()
    
    option = webdriver.ChromeOptions()
    
    option.add_argument("--profile-directory=Default")
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument("window-size=1920,1000")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    
    bot = webdriver.Chrome(options = option)
    bot.get("https://www.instagram.com")
    
    WebDriverWait(bot, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@aria-label='Phone number, username, or email']"))).send_keys(username)
    
    time.sleep(1)
    bot.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys(password)
    time.sleep(1)
    #bot.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys(username)
    bot.find_element(By.XPATH, "//button[@class='_acan _acap _acas _aj1-']").click()
    
    time.sleep(5)
    
    bot.find_elements(By.XPATH, "//a[@href='#']")[2].click()
    time.sleep(1)

    abs_path = os.path.abspath(PATH)
    bot.find_element(By.XPATH, "//input[@accept='image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime']").send_keys(abs_path)
    
    time.sleep(2)
    
    if bot.find_element(By.XPATH, 
    "//span[@class='x1lliihq \
    x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw \
    x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x \
    x1i0vuye x133cpev x1xlr1w8 x5n08af x4zkp8e x41vudc x10wh9bi x1wdrske x8viiok \
    x18hxmgj']").text == "Video posts are now shared as reels":
        bot.find_element(By.XPATH, "//button[@class='_acan _acap _acaq _acas _acav _aj1-']").click()
    
    time.sleep(2)
    
    for _ in range(2):
        for element in bot.find_elements(By.XPATH, "//div[@role='button']"):
            if element.text == "Next":
                break
        element.click()
        time.sleep(2)
    
    for element in bot.find_elements(By.XPATH, "//div[@role='button']"):
        if element.text == "Share":
            break
    element.click()
    time.sleep(2)