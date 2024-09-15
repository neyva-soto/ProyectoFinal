@admin
Feature: Admin section
  @smoke
  Scenario: Verify that the user is on the Admin Section
    Given The user is logged in
    When The user clicks on the Admin button
    Then the user will be redirected to admin section

