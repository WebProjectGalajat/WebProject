Feature: Eliminar artista
    In order to delete an artist,
    As a user,
    I want to search my artists and select and eliminate one.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: The artist exists
        Given I login as user "user" with password "password"
        When I type an artist
        Then I'm viewing a list containing
            | name      |
        And the list contains 0 artists

    Scenario: Delete artist not on the list
        Given I login as user "user" with password "password"
        When I type an artist that doesn't exist
        Then I get an error saying it doesn't exist