Feature: Login page

  Scenario Outline: Try to login in the site
    Given website is launched
    And username <username> is inserted
    And password <password> is inserted
    When login button is clicked
    Then login is <result>

  Examples: Credentials
   | username      | password     | result  |
   | standard_user | secret_sauce | success |
   | standard_user | abcd         | failure |
   | empty         | empty        | failure |