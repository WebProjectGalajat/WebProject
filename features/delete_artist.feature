Feature: Eliminar artista
    In order to delete an artist,
    As a user,
    I want to search my artists and select and eliminate one.

    Background: There is a registered user
        Given Exists a user "user" with password "password"
        And Exists an artist "artist" to user "user"

    Scenario: The artist exists
        Given I login as user "user" with password "password"
        When I delete an artist "artist"
        Then I'm viewing a list without artist "artist"
