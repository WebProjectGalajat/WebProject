Feature: Eliminar genere
    In order to delete a genre,
    As a user,
    I want to search and select a genre and delete it.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Delete a genre
        Given I login as user "user" with password "password"
        When I type a genre
        Then I'm viewing a list containing
            | name         |
        And the list contains 0 genres