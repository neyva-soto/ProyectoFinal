@vacancies
Feature: Vacancies page

  User story:
  * Go to Vacancies Page
  * I want to manage Vacancies
  * in order to verify Vacancies functionality

  Acceptance criteria:
  * Vacancies page is displayed and functional
  @functional
  Scenario: AUT-211 Verificar la funcionalidad para crear una nueva vacante
    Given The user is on the Vacancies Page
    When User clicks on button Add
    And The user type "Vacante Inventada <random>" for Vacancy Name
    And The user type "a" for Hiring Manager
    And The user clicks on the "a" dropdown option
    And The user selects "HR" option from Job Title dropdown
    And User clicks on button Save
    Then User should see "Edit Vacancy" text in the page


  @functional
  Scenario: AUT-212 Verificar la funcionalidad del botón Editar Información de una Vacante
    Given The user is on the Vacancies Page
    When User clicks on button Add
    And The user type "Vacante Inventada <random>" for Vacancy Name
    And The user type "a" for Hiring Manager
    And The user clicks on the "a" dropdown option
    And The user selects "HR" option from Job Title dropdown
    And User clicks on button Save
    And The user navigates to Vacancies page
    And The user clicks on the "bi-pencil-fill" icon for "Vacante Inventada" row
    And User clicks on button Save
    Then User should see "Successfully Saved" text in the page


  @functional
  Scenario: AUT-213 verificar la funcionalidad para eliminar una vacante
    Given The user is on the Vacancies Page
    When User clicks on button Add
    And The user type "Vacante Inventada <random>" for Vacancy Name
    And The user type "a" for Hiring Manager
    And The user clicks on the "a" dropdown option
    And The user selects "HR" option from Job Title dropdown
    And User clicks on button Save
    And The user navigates to Vacancies page
    And The user clicks on the "bi-trash" icon for "Vacante Inventada" row
    And User clicks on button Yes, Delete
    Then User should see "Successfully Deleted" text in the page

  @functional
  Scenario: AUT-214 validar la funcionalidad de la Búsqueda de vacante por Puesto de trabajo
    Given The user is on the Vacancies Page
    When User clicks on button Add
    And The user type "Vacante Para buscar <random>" for Vacancy Name
    And The user type "a" for Hiring Manager
    And The user clicks on the "a" dropdown option
    And The user selects "HR" option from Job Title dropdown
    And User clicks on button Save
    Then User should see "Edit Vacancy" text in the page
    When The user navigates to Vacancies page
    And The user selects "HR" option from Job Title dropdown in vacancies view
    And User clicks on button Search
    Then The user should see "Vacante Para buscar" card row


  @functional
  Scenario: AUT-214 validar la funcionalidad de la Búsqueda de vacante por Puesto de trabajo
    Given The user is on the Vacancies Page
    When User clicks on button Add
    And The user type "Vacante Para buscar2 <random>" for Vacancy Name
    And The user type "a" for Hiring Manager
    And The user clicks on the "a" dropdown option
    And The user selects "HR" option from Job Title dropdown
    And User clicks on button Save
    Then User should see "Edit Vacancy" text in the page
    When The user navigates to Vacancies page
    And The user selects "Active" option from Status dropdown in vacancies view
    And User clicks on button Search
    Then The user should see "Vacante Para buscar2" card row
