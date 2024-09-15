@login
Feature: Login - Successfully login

  User story:
  * As a user Login Page
  * I want to put username and password
  * in order login

  Acceptance criteria:
  * Login button should work and enter we page

  @smoke
  Scenario Outline: OT-IS01 Verificar la existencia de los campos usuario y contraseña
    Given The user is on the login page
    Then I see input field in the page with id "<UserId>"
    And I see input field in the page with id "<PasswordId>"

    Examples:
      | UserId    | PasswordId  |
      | username  |  password   |

  @smoke
  Scenario: OT-IS02 Verificar la existencia del boton de inicio de sesión
    Given The user is on the login page
    Then button will be displayed

  @smoke @regression
  Scenario Outline: OT-IS03 Verificar la Funcionalidad del Botón de Inicio de Sesión con Datos Válidos
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then the user should see the following text in the page "<Text>"

    Examples:
      | User    | Password   | Text      |
      | Admin   | admin123   | Dashboard |


  @functional @regression
  Scenario Outline: OT-IS04 Verificar la Funcionalidad del Botón de Inicio de Sesión con Datos incorrectos
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display the error message "<Message>"
    Examples:
      | User  | Password | Message   |
      | Admin | super123 | Invalid credentials |


  @smoke
  Scenario: OT-IS05 Verificar el comportamiento de inicio de sesión cuando los campos usuario y contraseña son vacíos
    Given The user is on the login page
    When the user clicks login button
    Then User and password fields should be displayed are required


  @functional
  Scenario Outline: OT-IS06 Verificar el mensaje de error cuando el campo user name esta vacio
    Given The user is on the login page
    When the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then Then it will be shown that the username field is required

    Examples:
      | Password   | Text      |
      | admin123   | Dashboard |

  @functional
  Scenario Outline: OT-IS07 Verificar el mensaje de error cuando el campo password esta vacio
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user clicks login button
    Then Then it will be shown that the password field is required

    Examples:
      | User  | Text      |
      | admin | Dashboard |


  @functional @regression
  Scenario Outline: OT-IS08 Verificar el comportamiento de inicio de sesion cuando se introducen usuario incorrecto
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display the error message "<Message>"
    Examples:
      | User  | Password | Message   |
      | Admin | super123 | Invalid credentials |

  @functional @regression
  Scenario Outline: OT-IS09 Verificar el comportamiento de inicio de sesion cuando se introduce contraseña incorrecta
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display the error message "<Message>"
    Examples:
      | User  | Password | Message   |
      | Admin | super123 | Invalid credentials |

  @usability
  Scenario Outline: Outline: OT-IS10 Verificar que el campo contraseña muestre puntos por cada letra ingresada
    Given The user is on the login page
    When the user enters the value "<Password>" in the text-input for password
    Then the password field must be hidden

  Examples:

    | Password | Text      |
    | admin123 | Dashboard |

  @functional @integration
  Scenario: OT-IS11 Verificar el Comportamiento del Enlace de Recuperación de Contraseña
    Given The user is on the login page
    When the user clicks in forgotPassword
    Then the new password form will show up

  @functional
  Scenario Outline: OT-IS12 Verifica que los campos de username y password se limpien despues de un intento fallido
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display text-input for username empty
    And will display text-input for password empty

    Examples:

      | User | Password |
      |super |super     |

  @functional
  Scenario Outline: OT-IS13 Verificar la sensibilidad de mayúsculas para login en inicio de sesión
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display a message

    Examples:
      | User  | Password | Text      |
      | ADMIN | admin123 | Dashboard |

  @functional
  Scenario: OT-IS14 Verificar la funcionalidad del enlace OrangeHRM, Inc.
    Given The user is on the login page
    When the user clicks in linkOrange
    Then the will see new page linkOrange


