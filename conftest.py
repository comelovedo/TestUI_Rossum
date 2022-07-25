import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://data-matching.elis.rossum.ai/upload-companies")
        global PAGE
        PAGE = page
        yield page
        # storage = context.storage_state(path="/Users/bazucer/Desktop/IT/Rossum/Cookie/state.json")
        # context = browser.new_context(storage_state="/Users/bazucer/Desktop/IT/Rossum/Cookie/state.json/state.json")

        browser.close()


def generate_string(num):
    """Function that will generate us a string of length n characters in the test file:"""
    return "x" * num


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'
