Feature: Afegir cançó
    In order to add a song,
    As a user,
    I want to search and select a song.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Add a song
        Given I login as user "user" with password "password"
        When I type a song that is correct
        Then I'm viewing a list containing
            | name              |
            | Hotline Bling     |
        And the list contains 1 songs

    Scenario: Add a song that does not exist
        Given I login as user "user" with password "password"
        When I type a song that does not exist
        Then I get an error saying it doesn't exist