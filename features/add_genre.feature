Feature: Afegir genere
    In order to add a genre,
    As a user,
    I want to search and select a genre.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Add a genre
        Given I login as user "user" with password "password"
        When I type a genre "genre"
        Then I'm viewing a list containing 1 genre
            | name         |
            | UK Drill     |
