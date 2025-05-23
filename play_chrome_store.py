import re
import time
import os.path
from playwright.sync_api import Playwright, sync_playwright, expect
import os
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("./dist/out2.log"))
logger.setLevel(logging.DEBUG)

def save_html(page):
    html_content = page.content()
    # 保存到文件
    with open(f"./dist/page.{time.time()}.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def download(page, download_locator):
    # 触发下载
    with page.expect_download() as download_info:
        download_locator.click()
    download = download_info.value
    # 保存到指定路径
    save_path = os.path.join('./dist', download.suggested_filename)
    download.save_as(save_path)
    print(f'文件已下载至：{save_path}')

def run(playwright: Playwright) -> None:
    print(f"os env: {os.environ}")
    browser = playwright.chromium.launch(headless=True, downloads_path='./dist', channel='chrome')
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    # Subscribe to "request" and "response" events.
    page.on("request", lambda request: logger.debug(f">>{request.method}, {request.url}, {request}"))
    page.on("response", lambda response: logger.debug(f"<<{response.status}, {response.url}"))

    # page.goto("https://www.douyu.com/")
    url = os.getenv("PAGE_URL", default="https://chromewebstore.google.com/detail/midscene/gbldofcpkknbggpkmbdaefngejllnief")
    page.goto(url)
    time.sleep(0.2)
    page.screenshot(path=f'./dist/shot.{time.time()}.png', full_page=True)
    save_html(page)

    # page.query_selector()
    if page.get_by_role('button', name="No thanks").count() > 0:
        page.get_by_role('button', name="No thanks").first.click()
    time.sleep(0.2)
    page.screenshot(path=f'./dist/shot.{time.time()}.png', full_page=True)
    save_html(page)

    if page.get_by_placeholder("Search extensions and themes").count() > 0:
        locator = page.get_by_placeholder("Search extensions and themes")
        locator.fill("VPN")
        locator.press("Enter")
        page.get_by_role('combobox', name='Search Chrome Web Store').press("Enter")


    # if page.get_by_text("Extensions", exact=True).count() > 0:
    #     page.get_by_text("Extensions", exact=True).click()
    time.sleep(0.5)
    page.screenshot(path=f'./dist/shot.{time.time()}.png', full_page=True)
    save_html(page)
    # login_frame_locator = page.locator("#login-passport-frame").content_frame
    # login_frame_locator.get_by_text("验证码登录").click()
    # login_frame_locator.get_by_placeholder("请输入手机号", exact=True).click()
    # login_frame_locator.get_by_placeholder("请输入手机号", exact=True).fill("173 7106 5145")
    #
    # login_frame_locator.get_by_role("button", name="获取验证码").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
