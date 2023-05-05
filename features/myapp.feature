#Feature: MyApp feature
#
#  Scenario: Basic test
#    Given I have a basic Django application
#    When I run a test
#    Then the test should pass


Feature: Cart and Order Management

  Scenario: Accessing the Cart
  Given a user is logged in
  When the user add their cart
  Then the cart should be displayed with the correct products and quantities

  Scenario: Accessing Orders
  Given a user is logged in
  When the user add their order history
  Then the order history should display the correct orders with product information