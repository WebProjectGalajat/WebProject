Feature: Modificar canço
Given a particular song,
As a user,
I want to modify its rating or description

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists a song "song" to user "user"

  Scenario: Modify song
    Given I login as user "user" with password "password"
    When I modify song "song"
    Then I'm viewing the modified song
      | old song |
      | modified song |
