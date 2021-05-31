Feature: Llista de cançons
    In order to see my top songs,
    As a user,
    I want to list my top 30 songs.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: List all songs
        Given I login as user "user" with password "password"
        When I list songs
        Then I'm viewing a list containing my songs
