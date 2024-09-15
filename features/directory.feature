@directory
Feature: Directory section

  User story:
  * Go to Directory page
  * I want to manage Directory
  * in order to verify Directory functionality

  Acceptance criteria:
  * Directory is displayed and functional
  @smoke
  Scenario: AUT-216 Verificar que el directorio muestra la lista de empleados
    Given The user is on the Directory Page
    Then Records Found should be shown

