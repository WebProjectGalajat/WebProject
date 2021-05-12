Feature: Modificar canço
  Given a particular song,
  As a user,
  I want to modify its rating or description

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Modify song
    Given I login as user "user" with password "password"
    When I modify song
    Then I'm viewing the modified songs
        | name      |
        | modified  |