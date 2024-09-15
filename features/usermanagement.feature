@user_management
Feature: UserManagement section

  @smoke
  Scenario: UM02-TC1 Verify that the user is on the
    Given The user is logged in
#   And The user is on the admin page
    When The user clicks on the Admin button
    Then the user will be redirected to admin section

#  @functional
#  Scenario:verify ascending order of users
#    Given The user is logged in
#    When The user clicks on the Admin button
#    And  The user clicks on the sort button
#    And  The user clicks on the up button
#    Then users must be displayed
  @usability
  Scenario: UM02-TC3 verify ascending order of users
    Given The user is logged in
    When The user clicks on the Admin button
    Then users must be displayed

@smoke
Scenario: UM02-TC4 Verify Search Bar functionality
    Given The user is logged in
    When The user clicks on the Admin button
    Then will display the search bar

@smoke
Scenario: UM02-TC5 Verify of the create user button
    Given The user is logged in
    When The user clicks on the Admin button
    Then will display button create user

@functional @regression @integration
Scenario: UM02-TC6 Verify of the Create User Button
    Given The user is logged in
    When The user clicks on the Admin button
    And The user cliks on the add user button
    Then will display page add user section

@functional
Scenario: UM02-TC7 Verificar el Acceso al Formulario de Creación de Usuario
    Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    Then User should see a form with content Add User

@functional
Scenario: UM02-TC8 Verificar la Disponibilidad de Campos en el Formulario de Creación de Job Title
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    Then User should see a form with content Add User
    And User should see a input field for Employee Name
    And User should see a input field for Username
    And User should see a input field for Password
    And User should see a input field for Confirm Password

@smoke
Scenario: UM02-TC9 Verificar la existencia del boton Reset de user management
    Given The user is logged in
    When the user clicks on the Admin button
    Then User should see button Reset

@smoke
Scenario: UM02-TC10 Verificar la existencia del boton Search de user management
    Given The user is logged in
    When the user clicks on the Admin button
    Then User should see button Search

@smoke
Scenario: UM02-TC11 Verificar la existencia del boton eliminar
    Given The user is logged in
    When the user clicks on the Admin button
    Then User should see button trash

@smoke
Scenario: UM02-TC12 Verificar la existencia del boton editar
    Given The user is logged in
    When the user clicks on the Admin button
    Then User should see button edit

@functional
Scenario: UM02-TC13 Verificar la validacion de campos obligatorios en add user
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    And User clicks on button Save
    Then User should see "Required" message in the page
    And User should see "Passwords do not match" message in the page

@functional
Scenario: UM02-TC14 Verificar la existencia del boton cancel al  momento de crear un usuario nuevo
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    Then User should see button Cancel


@functional
Scenario: UM02-TC15 Verificar la existencia del boton save
 Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    Then User should see button Save

@smoke @functional
Scenario: UM02-TC16 Verificar la existencia del boton search hidden
    Given The user is logged in
    When the user clicks on the Admin button
    Then User should see button hidden


@usability
Scenario: UM02-TC17 Verificar la Disponibilidad de Campo de Employee Name
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    Then User should see a input field for Employee Name

@functional @regression @integration
Scenario: UM02-TC18 Verificar creacion de usuario con contraseña y confirmacion de contraseña diferente
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    And User types text ".sample employee name <random>" in Employee Name Field
    And User types text ".sample user <random>" in Username Field
    And User types text ".sample password <random>" in Password Field
    And User types text ".sample password <random>" in Confirm Password Field
    And User clicks on button Save
    Then User should see "Required" message in the page
    And User should see "Passwords do not match" message in the page

@functional
Scenario: UM02-TC19 Verificar creacion de usuario con datos vacios
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on button Add
    And User clicks on button Save
    Then User should see "Required" message in the page
    And User should see "Passwords do not match" message in the page

@functional
Scenario: UM02-TC20 Verificar la existencia del boton save al  momento de modificar un usuario
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on icon edit
    Then User should see button Save

@functional
Scenario: UM02-TC21 Verificar el Manejo de Errores en el Formulario de Edición
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on icon edit
    Then User should see button Save


@functional @regression
Scenario: UM02-TC22 Verificar el comportamiento del formulario editar user cuando se deja vacio el campo employee name
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on icon edit
    And User types text " " in Employee Name Field
    Then User should see button Save
    And User should see "Required" message in the page

@functional
Scenario: UM02-TC23 Verificar el comportamiento del formulario editar user cuando se introduce valores erroneos en el campo employee name
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on icon edit
    And User types text ".sample employee name <random>" in Employee Name Field
    Then User should see button Save
    And User should see "Invalid" message in the page

@functional
Scenario: UM02-TC24 Verificar la persistencia de datos despues de recargar la pagina
  Given The user is logged in
    When The user clicks on the Admin button
    And User clicks on icon edit
    And User types text ".sample employee name <random>" in Employee Name Field
    Then User should see button Save
    And User should see "Invalid" message in the page

@functional
Scenario: UM02-TC26 Verificar el mensaje de la Confirmación de Eliminación
  Given The user is logged in
    When the user clicks on the Admin button
    And User clicks on icon delete
    Then User should see button Yes,delete

@functional
Scenario: UM02-TC27 Verificar el mensaje de la Confirmación de Eliminación
  Given The user is logged in
    When the user clicks on the Admin button
    And User clicks on icon delete
    Then User should see button No,Cancel

@functional
Scenario: UM02-TC28 Verificar el funcionamiento del icono salir despues de hacer clic en modificar informacion
    Given The user is logged in
    When the user clicks on the Admin button
    And User clicks on icon delete
    And User clicks on icon exit
    Then User should see a input field for Username

@functional
Scenario: UM02-TC29 Verificar el funcionamiento del boton de seleccion de todos los usuarios de user management
    Given The user is logged in
    When the user clicks on the Admin button
    And User clicks icon selection
    Then User should see button Delete Selected

@functional
Scenario: UM02-TC30 Verificar el funcionamiento de user management cuando se eliminan todos los mensajes
    Given The user is logged in
    When the user clicks on the Admin button
    And User clicks icon selection
    Then User should see button Delete Selected
    And User should see button Yes,delete

@functional
Scenario: UM02-TC30 Verificar el funcionamiento de user management cuando se cancela el proceso de eliminacion de todos los usuarios
    Given The user is logged in
    When the user clicks on the Admin button
    And User clicks icon selection
    Then User should see button Delete Selected
    And User should see button No,Cancel


@functional
Scenario: UM02-TC31 Verificar el funcionamiento de user management cuando se cierra la ventana de mensaje del proceso de eliminacion de todos los usuarios
    Given The user is logged in
    When the user clicks on the Admin button
    And User clicks icon selection
    And User clicks on button Delete Selected
    And User clicks on icon exit
    Then User should see a input field for Username