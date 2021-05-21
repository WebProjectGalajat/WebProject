Feature: Llista d'artistes
    In order to see my top artists,
    As a user,
    I want to list my top 20 songs.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: List all artists
        Given I login as user "user" with password "password"
        When I list artists
        Then I'm viewing a list containing my artists
