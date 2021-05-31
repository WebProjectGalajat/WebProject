Feature: Modificar artista
Given a particular artist,
As a user,
I want to modify it

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists an artist "artist" to user "user"

  Scenario: Modify an artist
    Given I login as user "user" with password "password"
    When I modify artist "artist"
    Then I'm viewing the modified artist
      | Old artist      |
      | Modified artist |
