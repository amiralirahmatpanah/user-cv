from playwright.sync_api import sync_playwright
import time
url = "https://www.tgju.org/"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, timeout=70000)
    page = browser.new_page()
    page.goto(url)
    for i in range(10):
        market_price = page.inner_html("html .index-tabs .currency-min-font .index-tabs-data table.data-table tr td")
        for j in market_price:
            print(market_price)
            time.sleep(1)
    page.pause()