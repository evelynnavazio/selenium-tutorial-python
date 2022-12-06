from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CSS_SELECTOR = "css selector"

browser = webdriver.Chrome()
browser.get('https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456%2Cn%3A172636&dc&language=es&ds=v1%3ArJVPmy3WS95jJ3fybOur9bCr1yuaPtcfB4x0DEEMgxk&qid=1670181398&rnid=172456&ref=sr_nr_n_2')

isNextDisabled = False

while not isNextDisabled:
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row")))
        elem_list = browser.find_element(By.CSS_SELECTOR,
                                         "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row")

        items = elem_list.find_elements(
            By.XPATH, '//div[@data-component-type="s-search-result"]')
        for item in items:
            title = item.find_element(By.TAG_NAME, 'h2').text
            price = "No Price Found"
            decimals = "No decimals Found"
            image = "No image Found"
            link = item.find_element(
                By.CLASS_NAME, 'a-link-normal').get_attribute('href')
        try:
            price = item.find_element(
                By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
        except:
            pass
            try:
                image = item.find_element(
                    By.CSS_SELECTOR, '.s-image').get_attribute('src')
            except:
                pass
            try:
                browser.find_element(
                    By.CLASS_NAME, 's-pagination-item').click()
            except Exception as e:
                print(e, "Pagination error")
                isNextDisabled = True

    except Exception as e:
        print(e, "Main error")
        isNextDisabled = True

    print('Title:' + title)
    print('Price:' + price)
    print('Image:' + image)
    print('URL:' + link + "\n")
