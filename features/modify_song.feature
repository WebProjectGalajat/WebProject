Feature: Modificar canço
Given a particular song,
As a user,
I want to modify its rating or description

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Modify song description
    Given I login as user "user" with password "password"
    When I modify song description
    Then I'm viewing the modified description
      | old description |
      | new description |

  Scenario: Modify song rating
    Given I login as user "user" with password "password"
    When I modify song rating
    Then I'm viewing the modified rating
      | old rating |
      | new rating |