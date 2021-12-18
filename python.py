from selenium import webdriver
from PIL import Image, ImageDraw
from io import BytesIO
import cv2
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains
import time
from promise import Promise



# def __find__Coordinates__Image(link, screen):
#     image = cv2.imread(link)
#     method = cv2.TM_SQDIFF_NORMED
#     result = cv2.matchTemplate(image, screen, method)
#     mn,_,mnLoc,_ = cv2.minMaxLoc(result)
#     MPx,MPy = mnLoc
#     trows,tcols = image.shape[:2]
#     locationX = MPx + (tcols /2)
#     locationY = MPy + (trows /2)
#     return {
#         'X' : locationX,
#         'Y' : locationY
#     }
    
# def __click__by__Coordinates(point, browser):
#     action = ActionChains(browser)
#     action.move_by_offset(locationX,locationY).click().perform()
    
    
# def screenImage(screenShoot):
#     img_stream = BytesIO(screenShoot)
#     return cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)


# def main():

#     #screen shot first
#     
    
# def run(browser):
#     screenShoot = browser.get_screenshot_as_png()
#     return screenShoot
    
# def main():
#     browsers = []
#     for _ in range(4):
#         browser = webdriver.Chrome()
#         browser.get('https://splinterlands.com/')
#         browsers.append(browser)
#     screenshots = []
#     with ThreadPoolExecutor(max_worker=2) as executor:
#         for result in executor.map(run, browsers):
#             screenshots.append(result)
    
    
            
#     print("123123123")
    # screen = screenImage(screenShoot)

# main()





btnPlayNow = cv2.imread('./img/playnow123.png')
# screen shoot

browser = webdriver.Chrome()
browser.get('https://splinterlands.com/')
#screen shot first
screen = browser.get_screenshot_as_png()
# convert image lib in BytesIO

img_stream = BytesIO(screen)
screen = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
# find image in screen
method = cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(btnPlayNow, screen, method)


# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

print("MPx",MPx)
print("MPy",MPy)

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = btnPlayNow.shape[:2]

# Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
cv2.line(screen, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
# ActionChains(browser).move_by_offset((MPx+tcols)/2,(MPy+trows)/2).click().perform()

e = browser.find_element_by_id("play_now_btn")

location = e.location
size = e.size
w, h = size['width'], size['height']
print(location)
print(size)
print(w, h)

locationX = MPx + (tcols /2)
locationY = MPy + (trows /2)
print(locationX)
print(locationY)
# create action chain object
action = ActionChains(browser)
action.move_by_offset(locationX,locationY).click().perform()


# cv2.imshow("img", screen)
cv2.waitKey(0)







wwheckPlayNow
playnow

check


