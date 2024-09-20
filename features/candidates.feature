@candidates
Feature: Candidates page

  User story:
  * Go to Job Candidates Page
  * I want to manage Candidates
  * in order to verify Candidates functionality

  Acceptance criteria:
  * Candidates page is displayed and functional
  @functional
  Scenario: AUT-206 Validar la funcionalidad para agregar Nuevo Candidato en Recruitment con datos correctos
    Given The user is on the Candidates Page
    When User clicks on button Add
    And The user type "Alan" in the input field with name firstName
    And The user type "Brito" in the input field with name lastName
    And The user type "alan@mail.com" for the email
    And User clicks on button Save
    Then User should see "Successfully Saved" text in the page


  @functional
  Scenario: AUT-207 Verificar la funcionalidad al momento de editar Información de un Candidato en recruitment
    Given The user is on the Candidates Page
    When User clicks on button Add
    And The user type ".test candidate name" in the input field with name firstName
    And The user type "Brito" in the input field with name lastName
    And The user type "alan@mail.com" for the email
    And User clicks on button Save
    And The user navigates to Candidates page
    And The user clicks on the "bi-eye-fill" icon for ".test candidate name" row
    And The user click on the edit checkbox
    And User clicks on button Save
    Then User should see "Successfully Updated" text in the page


  @functional
  Scenario: AUT-208 Validar la funcionalidad de Eliminar un Candidato
    Given The user is on the Candidates Page
    When User clicks on button Add
    And The user type ".test candidate to remove" in the input field with name firstName
    And The user type "Brito" in the input field with name lastName
    And The user type "alan@mail.com" for the email
    And User clicks on button Save
    And The user navigates to Candidates page
    And The user clicks on the "bi-trash" icon for ".test candidate to remove" row
    And User clicks on button Yes, Delete
    Then User should see "Successfully Deleted" text in the page


  @functional
  Scenario: AUT-209 Validar la Búsqueda de un Candidato por Nombre
    Given The user is on the Candidates Page
    When User clicks on button Add
    And The user type ".test usuario para buscar" in the input field with name firstName
    And The user type "Brito" in the input field with name lastName
    And The user type "alan@mail.com" for the email
    And User clicks on button Save
    And The user navigates to Candidates page
    And The user type ".test usuario para buscar" for the candidate name field
    And The user clicks on the ".test usuario para buscar" dropdown option
    And User clicks on button Search
    Then The user should see ".test usuario para buscar" card row
