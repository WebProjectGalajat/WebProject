Feature: Afegir artista
    In order to add an artist,
    As a user,
    I want to search and select an artist.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: The artist exists
        Given I login as user "user" with password "password"
        When I type an artist
        Then I'm viewing a list containing
            | name      |
            | Drake     |
        And the list contains 1 artists

    Scenario: The artist does not exists
        Given I login as user "user" with password "password"
        When I type an artist that doesn't exist
        Then I get an error saying it doesn't exist