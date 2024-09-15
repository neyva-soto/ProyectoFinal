@jobs
Feature: Job Titles

  User story:
  * Go to Job Titles Page
  * I want to manage Job Titles
  * in order to verify Job Titles functionality

  Acceptance criteria:
  * Job Titles is displayed and functional
  @smoke
  Scenario: OT-J01 Verificar la Carga de la Lista de Job Titles
    Given The user is on the Job Titles Page
    Then Records must be shown for Job Titles

  @functional
  Scenario: OT-J02 Verificar la Existencia del Botón de Agregar Job Titles
    Given The user is on the Job Titles Page
    Then User should see button Add

  @functional
  Scenario: OT-J03 Verificar el Acceso al Formulario de Creación de Job Title
    Given The user is on the Job Titles Page
    When User clicks on button Add
    Then User should see a form with content Job Title

  @functional
  Scenario: OT-J04 Verificar la Disponibilidad de Campos en el Formulario de Creación de Job Title
    Given The user is on the Job Titles Page
    When User clicks on button Add
    Then User should see a form with content Job Title
    And User should see a input field for Job Title
    And User should see a textarea field for Job Description
    And User should see a input field for Job Specification
    And User should see a textarea field for Note

  @functional
  Scenario: OT-J05 Verificar la Validación de Campos en el Formulario de Creación de Job Title
    Given The user is on the Job Titles Page
    When User clicks on button Add
    And User clicks on button Save
    Then User should see the error message "Required"

  @functional
  Scenario: OT-J06 Verificar la Creación de Job Title con Datos Válidos
    Given The user is on the Job Titles Page
    When User clicks on button Add
    And User types ".test Job Title <random>" in Job Title Field
    And User clicks on button Save
    Then User should see the entry ".test Job Title <random>" in the page

  @functional @regression
  Scenario: OT-J07 Verificar la Edición de Job Title Existente
    Given The user is on the Job Titles Page
    When User clicks on button Add
    And User types ".test Job Title <random>" in Job Title Field
    And User clicks on button Save
    And User clicks on icon edit for ".test Job Title <random>"
    And User types ".test Edit <random>" in Job Title Field
    And User clicks on button Save
    Then User should see the entry ".test Edit <random>" in the page

  @functional @regression
  Scenario: OT-J08 Verificar la Eliminación de Job Title
    Given The user is on the Job Titles Page
    When User clicks on button Add
    And User types ".test Job Title <random>" in Job Title Field
    And User clicks on button Save
    And User clicks on icon delete for ".test Job Title <random>"
    And User clicks on button Yes, Delete
    Then User should not see the entry ".test Job Title <random>" in the page

# Pay Grades
  @smoke
  Scenario: OT-J09 Verificar la Carga de la Lista de Pay Grades
    Given The user is on the Pay Grades Page
    Then Records must be shown for Pay Grades

  @smoke
  Scenario: OT-J010 Verificar la Existencia del Botón de Pay Grades
    Given The user is on the Pay Grades Page
    Then User should see button Add
