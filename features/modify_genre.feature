Feature: Modificar genere
Given a particular genre,
As a user,
I want to modify it

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists a genre "genre" to user "user"

  Scenario: Modify genre
    Given I login as user "user" with password "password"
    When I modify genre "genre"
    Then I'm viewing the modified genre
      | Old genre version      |
      | Modified genre version |
