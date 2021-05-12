# Created by mcr99 at 12/05/2021
Feature: Modificar genere
  Given a particular genre,
  As a user,
  I want to modify it

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Modify genre
    Given I login as user "user" with password "password"
    When I modify genre
    Then I'm viewing the modified genres
        | name      |
        | modified  |