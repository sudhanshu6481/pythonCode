Feature: Login functionality
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.all
 Scenario: Successful login

   Given the user is on the login page

   When the user enters valid credentials

   Then the user should be logged in