import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def save_html(page):
    html_content = page.content()
    # 保存到文件
    with open(f"./dist/page.{time.time()}.html", "w", encoding="utf-8") as f:
        f.write(html_content)


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, downloads_path='./dist')
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://www.douyu.com/")
    page.goto("https://chromewebstore.google.com/detail/midscene/gbldofcpkknbggpkmbdaefngejllnief")
    page.get_by_text("Extensions").click()
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
