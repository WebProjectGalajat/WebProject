Feature: Afegir cançó
    In order to delete a song,
    As a user,
    I want to search and select a song to delete.

    Background: There is a registered user
        Given Exists a user "user" with password "password"

    Scenario: Delete a song
        Given I login as user "user" with password "password"
        When I type a song that is correct
        Then I'm viewing a list containing
            | name              |
        And the list contains 0 songs

    Scenario: Delete a song not on the list
        Given I login as user "user" with password "password"
        When I type a song that does not exist
        Then I get an error saying it doesn't exist