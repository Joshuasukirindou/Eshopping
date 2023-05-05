# # from behave import given, when, then
# #
# # @given('I have a basic Django application')
# # def step_given_i_have_a_basic_django_application(context):
# #     pass
# #
# # @when('I run a test')
# # def step_when_i_run_a_test(context):
# #     pass
# #
# # @then('the test should pass')
# # def step_then_the_test_should_pass(context):
# #     pass
#
#
from behave import given, when, then
from django.test import Client
from estore.models import User
from django.contrib.auth.hashers import make_password
import random
import string

def random_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "@example.com"

@given('a user is logged in')
def step_given_a_user_is_logged_in(context):
    # Create a test user and log them in
    User.objects.filter(name='admin-test').delete()
    context.user = User.objects.create(name='admin-test', email=random_email(), password=make_password('123456'))
    context.client = Client()  # Initialize Django test client
    response = context.client.post('/user/login/', {'username': 'admin-test', 'password': '123456'})
    assert response.status_code == 302

@when('the user add their cart')
def step_when_the_user_accesses_their_cart(context):
    # Access the cart page
    response = context.client.get('/order/cart/')
    context.cart_response = response

@then('the cart should be displayed with the correct products and quantities')
def step_then_the_cart_should_be_displayed_with_the_correct_products_and_quantities(context):
    # Check the cart response
    assert context.cart_response.status_code == 200

@when('the user add their order history')
def step_when_the_user_accesses_their_order_history(context):
    # Access the order history page
    context.order_response = context.client.get('/order/')

@then('the order history should display the correct orders with product information')
def step_then_the_order_history_should_display_the_correct_orders_with_product_information(context):
    # Check the order history response
    assert context.order_response.status_code == 200