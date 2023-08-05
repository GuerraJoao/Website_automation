from selenium import webdriver


def before_feature(context, feature):
    context.browser = webdriver.Firefox()


def after_feature(context, feature):
    context.browser.quit()
