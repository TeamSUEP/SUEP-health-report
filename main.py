from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from envconfig import username, password, wait_time, confirm_time, headless, fullscreen, quit_on_error, private


def login(driver, username=username, password=password):
    url = r'https://ids.shiep.edu.cn/authserver/login?service=https%3A%2F%2Fehall.shiep.edu.cn%2Fdefault%2Fwork%2Fshiep%2Fmrjktb%2Fmryb.jsp%3Ftype%3Dtb'
    xpaths = {
        'username': '//*[@id="username"]',
        'password': '//*[@id="password"]',
        'login_button': '//*[@id="casLoginForm"]/p[4]/button',
        'msg': '//*[@id="msg"]',
    }

    driver.get(url)

    current_url = driver.current_url
    if current_url.startswith('https://ids.shiep.edu.cn'):
        elements = {}
        for element, xpath in xpaths.items():
            if element != 'msg':
                elements[element] = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, xpath)))

        elements['username'].send_keys(username)
        elements['password'].send_keys(password)
        elements['login_button'].click()

        try:
            elements['msg'] = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, xpaths['msg'])))
            print(f"[ERROR] {elements['msg'].text}")
            return False
        except TimeoutException:
            if private:
                print(f"[INFO] Successfully logged in.")
            else:
                print(f"[INFO] Successfully logged in as {username}.")
            return True
    elif current_url.startswith('https://ehall.shiep.edu.cn'):
        print(f"[INFO] Already logged in.")
        return True
    else:
        print(f"[ERROR] Unknown error.")
        if not private:
            print(f"[INFO] Current URL: {current_url}")
        return False


def submit(driver):
    url = r'https://ehall.shiep.edu.cn/default/work/shiep/mrjktb/mryb.jsp?type=tb'
    xpaths = {
        'daily_track': '//*[@id="radio_dtsftjzgfxd15"]/div',
        'confirm_checkbox': '//*[@id="checkbox_cn38"]/div/ins',
        'submit_button': '//*[@id="post"]',
        'msg': '//*[@id="layui-layer1"]/div[2]',
    }

    driver.get(url)

    elements = {}
    for element, xpath in xpaths.items():
        if element != 'msg':
            elements[element] = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, xpath)))

    elements['daily_track'].click()
    elements['confirm_checkbox'].click()
    print(f"[INFO] Please confirm your information in {confirm_time} seconds.")
    sleep(confirm_time)
    elements['submit_button'].click()

    try:
        elements['msg'] = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, xpaths['msg'])))
        print(f"[ERROR] {elements['msg'].text}")
        return False
    except TimeoutException:
        print(f"[INFO] Successfully submitted.")
        return True


def main():
    global confirm_time

    if headless:
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        confirm_time = 0
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
        if fullscreen:
            driver.fullscreen_window()

    if login(driver):
        if submit(driver):
            driver.quit()
        else:
            if quit_on_error:
                driver.quit()
            exit(1)
    else:
        if quit_on_error:
            driver.quit()
        exit(1)


if __name__ == '__main__':
    main()
