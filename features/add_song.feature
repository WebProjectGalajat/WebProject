Feature: Afegir cançó
    In order to add a song,
    As a user,
    I want to search and select a song.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Add a song
        Given I login as user "user" with password "password"
        When I type a song "song"
        Then I'm viewing details containing 1 song
            | name              |
            | Hotline Bling     |
