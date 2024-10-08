# Descripcion
Automatizacion de pruebas para el sistema **ORANGE HRM**

## Requerimientos
* Instalar los paquetes de `requirements.txt`
````commandline
pip install -r requirements.txt
````
* Instalar Allure Report de https://allurereport.org/docs/install/

## Pasos para ejecutar
* Correr 1 test especifico
```commandline
behave features/login.feature
```
* Correr Todo los tests
```commandline
behave
```
* Correr todo los tests y generar reportes con Allure Report
```commandline
python -m behave -f allure_behave.formatter:AllureFormatter -o ./allure-results
```
* [OPCIONAL] Visualizar los resultados del reporte con allure
```commandline
allure serve ./allure-results
```

# Ejecutar Pruebas Behave en PARALELO
Tiene soporte para ejecutar pruebas Behave en paralelo con la opción de generación de informes Allure.
Admite la ejecución de features específicos, escenarios, etiquetas, y permite la configuración de hilos de ejecución en paralelo.


### Ejecución Básica

Ejecuta todos los archivos `.features` en el directorio predeterminado (`./features`):

```bash
python behave_parallel.py
````
### Especificar Features
Ejecuta archivos Feature. Se agregará la extensión `.feature` si se omite:

```bash
python behave_parallel.py --features=feature1.feature,feature2
```
### Ejecutar Escenarios Específicos
Ejecuta escenarios específicos dentro de los features:

```bash
python behave_parallel.py --scenarios='scenario1','scenario2'
```
### Ejecutar por Etiquetas
Ejecuta escenarios que coincidan con las etiquetas especificadas:

```bash
python behave_parallel.py --tags=tag1,tag2,tag3
```
### Ejecutores/NumeroProcesos Personalizados
Establece el número de hilos paralelos (el valor predeterminado es 2):

```bash
python behave_parallel.py --executors=5
```
### Generar Reportes en Allure
Genera informes Allure para las pruebas:

```bash
python behave_parallel.py --generate_reports
```
### Opciones Combinadas
Combina opciones para ejecutar escenarios o etiquetas específicas y generar informes:

```bash
python behave_parallel.py --executors=5 --generate_reports --features=feature1,feature2 --scenarios='scenario1','scenario2' --tags=tag1,tag2
```

### Ejemplos
Ejecutar un feature específico con ejecución paralela y generar informes:

```bash
python behave_parallel.py --executors=5 --generate_reports --features=feature1
```
Ejecutar escenarios para cada etiqueta en paralelo:

```bash
python behave_parallel.py --executors=5 --tags=smoke,functional
```
Ejecutar todos los escenarios y etiquetas en paralelo para cada feature:

```bash
python behave_parallel.py --executors=5 --features=feature1.feature,feature2.feature --scenarios='scenario1','scenario2' --tags=tag1,tag2
```
Ejecutar escenarios de un feature con etiquetas especificadas en paralelo:

```bash
python behave_parallel.py --executors=5 --features=feature1.feature --tags=smoke,functional
```
