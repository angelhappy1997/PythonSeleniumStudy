'''
I'd like to open a register page which contains the verfication image
Then get the screenshot only with verfication image
'''

from  selenium import webdriver
import time
from PIL import Image
import pytesseract

dr = webdriver.Chrome()
dr.get("http://www.5itest.cn/register?goto=/")
dr.maximize_window()
time.sleep(5)

path = "C:/work/vcPyTest/WebTest"
file1 = path + "/full_screen.png"
file2 = path + "/codeimg.png"

print("存储整个屏幕")
dr.save_screenshot(file1)

print("开始截图")
code_element = dr.find_element_by_id("getcode_num")
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open(file1)
img = im.crop((left,top,right,height))
img.save(file2)
print("关闭窗口")
dr.close()
