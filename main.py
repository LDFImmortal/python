import time

from flask import Flask
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

app = Flask(__name__)


def search(search_name, list1):
    url = "https://s.wanfangdata.com.cn/paper"
    service = Service(executable_path=r"C:\Program Files\chromedriver-win64\chromedriver.exe")
    opt = Options()
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_experimental_option("detach", True)

    # 使用上面定义的服务对象来创建一个Edge浏览器的WebDriver对象来模拟浏览器操作
    browser = webdriver.Edge(service=service, options=opt)

    # 调用maximize_window方法，使浏览器窗口最大化显示
    browser.maximize_window()
    # 添加显式等待
    wait = WebDriverWait(browser, 10)
    # 访问网页
    browser.get(url)
    time.sleep(2)
    # 点击高级检索
    wait.until(lambda x: x.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/div/div/div[2]/span")).click()
    # 选择下拉框(非select选择框)
    wait.until(lambda x: x.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]")).click()
    time.sleep(1)
    select_elements = browser.find_elements(By.XPATH, "/html/body/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[2]")
    return str(select_elements[0])
    # # 输入查询条件
    # element_search = browser.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div[1]/div/div/div[1]/div[2]/input")
    # element_search.send_keys(search_name, Keys.ENTER)
    # # 出版时间倒叙
    # wait.until(lambda x: x.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/div[2]/div/div[3]/div[2]/div[1]/div[2]")).click()
    # # 循环查询前五条搜索结果
    # for i in range(1, 6):
    #     wait.until(lambda x: x.find_element(By.XPATH, "/html/body/div[5]/div/div[3]/div[2]/div/div[4]/div[2]/div[1]/div/div[" + str(i) + "]/div/div[1]/div[2]/span[2]")).click()
    #     window = browser.window_handles
    #     browser.switch_to.window(window[1])
    #     wait.until(lambda x: x.find_element(By.XPATH, "//*[@id='essential']/div[6]/div[1]/span[2]/span/span[2]/span")).click()
    #     element_text = wait.until(lambda x: x.find_element(By.XPATH, "//*[@id='essential']/div[6]/div[1]/span[2]/span/span[1]"))
    #     list1.append(element_text.text)
    #     browser.close()
    #     browser.switch_to.window(window[0])
    #     time.sleep(2)
    # return str(list1)


@app.route('/test/<search_name>', methods=['GET'])
def test(search_name):
    return search(search_name, list1=[])


if __name__ == '__main__':
    app.run(debug=True)
