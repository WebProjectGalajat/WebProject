Feature: Afegir cançó
    In order to delete a song,
    As a user,
    I want to search and select a song to delete.

    Background: There is a registered user
        Given Exists a user "user" with password "password"
        And Exists a song "song" to user "user"

    Scenario: Delete a song
        Given I login as user "user" with password "password"
        When I delete a song "song"
        Then I'm viewing a list without song "song"
