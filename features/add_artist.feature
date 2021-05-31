Feature: Afegir artista
    In order to add an artist,
    As a user,
    I want to search and select an artist.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: The artist exists
        Given I login as user "user" with password "password"
        When I type an artist "artist"
        Then I'm viewing the artist details containing 1 artist
