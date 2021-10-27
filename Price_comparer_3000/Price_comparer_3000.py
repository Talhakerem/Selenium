from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

def hb(keyword):
    titles_array = []
    prices_array = []
    browser.get("https://www.hepsiburada.com/")
    sleep(3)
    search = browser.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[1]/div[2]/input")

    search.send_keys(keyword)
    sleep(3)
    search_button = browser.find_element_by_xpath("//*[@id='SearchBoxOld']/div/div/div[2]")
    sleep(3)
    search_button.click()
    sleep(3)

    i = 0
    while i<3:
        titles = browser.find_elements_by_css_selector(".product-title.title")
        titles_array.append(titles[i].text)
        titles[i].click()
        i += 1
        sleep(2)
        price = browser.find_element_by_xpath("//*[@id='offering-price']/span[1]")
        prices_array.append(price.text)
        sleep(2)
        browser.back()
        sleep(2)

    browser.close()
    return prices_array , titles_array

def trendyol(keyword):
    browser.get("https://www.trendyol.com/")
    sleep(3)
    try:
        close_ty = browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/div/div/div[1]")
        sleep(1)
        close_ty.click()
    except:
        print("\n")

    search_ty = browser.find_element_by_xpath("//*[@id='auto-complete-app']/div/div/input")
    search_ty.send_keys(keyword)
    sleep(2)
    search_button_ty = browser.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/i")
    search_button_ty.click()
    sleep(2)
    try:
        overlay_ty = browser.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/a/div[1]/div[2]/div[3]/div[1]")
        overlay_ty.click()
    except:
        z = 3
    sleep(3)
    prices_text = []
    titles_text = []
    flag = 0
    while flag < 4:
        titles_ty = browser.find_elements_by_css_selector(".prdct-desc-cntnr-name.hasRatings")
        titles_text.append(titles_ty[flag].text)
        titles_ty[flag].click()
        sleep(3)
        browser.switch_to.window(browser.window_handles[1])
        prices_ty = browser.find_element_by_css_selector(".product-price-container")
        prices_text.append(prices_ty.text)
        browser.close()
        browser.switch_to.window(browser.window_handles[0])

        flag += 1
    for i in range(0, 3):
        print("{} = {}".format(titles_text[i], prices_text[i]))
        print("\n")


search_keyword = input("What do you want to search? ")

trendyol(search_keyword)



b , d = hb(search_keyword)

for i in range(3):
    print(b[i] , d[i])