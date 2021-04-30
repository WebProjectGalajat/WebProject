Feature: Llista de gèneres
    In order to see my top genres,
    As a user,
    I want to list my top 5 genres.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: List all artists
        Given I login as user "user" with password "password"
        When I list artists
        Then I'm viewing a list containing
            | name      |
        And the list contains 20 artists