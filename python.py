from selenium import webdriver
from io import BytesIO
import cv2
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# hàm này tìm tọa độ theo hình truyền vào
def common__find__Coordinates__Image(link_img_find,screen):
    image = cv2.imread(link_img_find)
    method = cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(image, screen, method)
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc
    trows,tcols = image.shape[:2]
    return {
        'X' : MPx + (tcols / 2),
        'Y' : MPy + (trows / 2)
    }


# hàm này click theo tọa độ
def common__click__by__Coordinates(point, browser):
    action = ActionChains(browser)
    action.move_by_offset(point['X'], point['Y']).click().perform()

# hàm này dùng để convert hình chụp qua opencv
def common_read_ScreenImage(screenShoot):
    img_stream = BytesIO(screenShoot)
    return cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)


# hàm này dùng để chụp màn hình
def common_get_screenImage(browser):
    return browser.get_screenshot_as_png()


if __name__ == '__main__':
    browser.get('https://splinterlands.com/')
    screen = common_get_screenImage(browser)
    screen = common_read_ScreenImage(screen)
    locationBtnPlayGame = common__find__Coordinates__Image('./img/playnow123.png', screen)
    common__click__by__Coordinates(locationBtnPlayGame, browser)
    cv2.waitKey(0)
 