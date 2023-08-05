from behave import *
from utils import *


@given("website is launched")
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/")


@given("username {username} is inserted")
def step_impl(context, username):
    element = wait_until_find_element_by_id(context.browser, "user-name")
    # element = context.browser.find_element(By.ID, "user-name")
    insert_text(context.browser, element, username)


@given("password {password} is inserted")
def step_impl(context, password):
    element = wait_until_find_element_by_id(context.browser, "password")
    # element = context.browser.find_element(By.ID, "password")
    insert_text(context.browser, element, password)


@when("login button is clicked")
def step_impl(context):
    element = wait_until_find_element_by_id(context.browser, "login-button")
    # element = context.browser.find_element(By.ID, "login-button")
    click_on_element(context.browser, element)


@then("login is {result}")
def step_impl(context, result):
    # In case of success, the inventory container should appear, so we look for its existence,
    # In case of failure, the login container should be visible
    if result == 'success':
        # Here no assert is made because if the element does not exist, the find_element will automatically throw an error
        # context.browser.find_element(By.ID, "inventory_container")
        wait_until_find_element_by_id(context.browser, "inventory_container")
    elif result == 'failure':
        wait_until_find_element_by_id(context.browser, "login_button_container")
        # context.browser.find_element(By.ID, "login_button_container")
