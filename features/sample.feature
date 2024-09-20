@candidates
Feature: Candidates page
  @functional
  Scenario: AUT-210 Verificar la funcionalidad de Filtrado de Candidatos por Estado de Aplicación
    Given The user is on the Candidates Page
    When User clicks on button Add
    And The user type ".test usuario para filtrar" in the input field with name firstName
    And The user type "Brito" in the input field with name lastName
    And The user type "alan@mail.com" for the email
    And User clicks on button Save
    And The user navigates to Candidates page
    And The user clicks on the status dropdown
    And The user clicks on the ".test usuario para buscar" dropdown option
    And User clicks on button Search
    Then The user should see ".test usuario para filtrar" card row