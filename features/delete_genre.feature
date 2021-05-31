Feature: Eliminar genere
    In order to delete a genre,
    As a user,
    I want to search and select a genre and delete it.

    Background: There is a registered user
        Given Exists a user "user" with password "password"
        And Exists a genre "genre" to user "user"

    Scenario: Delete a genre
        Given I login as user "user" with password "password"
        When I delete a genre "genre"
        Then I'm viewing a list without genre "genre"
