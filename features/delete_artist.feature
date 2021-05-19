Feature: Eliminar artista
    In order to delete an artist,
    As a user,
    I want to search my artists and select and eliminate one.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: The artist exists
        Given I login as user "user" with password "password"
        When I delete an artist
        Then I'm viewing a list containing 0 artists
