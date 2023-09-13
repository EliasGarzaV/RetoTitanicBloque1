# Reto equipo #4: Supervivencia en el Titanic

Este repositorio es parte de un proyecto centrado en el famoso conjunto de datos del Titanic, que se encuentra disponible en Kaggle en la siguiente ubicación: [https://www.kaggle.com/competitions/titanic/](https://www.kaggle.com/competitions/titanic/). El objetivo principal de este proyecto es llevar a cabo un análisis exhaustivo del conjunto de datos del Titanic, realizar la limpieza y transformación de variables necesarias y desarrollar modelos de machine learning para predecir quiénes sobreviven y quiénes no.

## Descripción del Proyecto

### Limpieza y Transformación de Variables

El primer paso en este proyecto es llevar a cabo una limpieza y transformación exhaustiva de los datos del Titanic. Esto implica tratar los valores faltantes, detectar y manejar valores atípicos, y realizar una ingeniería de características para preparar los datos para su uso en modelos de machine learning.

### Modelos de Machine Learning

Se desarrollan cuatro modelos de machine learning distintos para abordar el problema de clasificación de supervivencia en el Titanic:

1. **Logistic Regression**: Se utiliza una regresión logística como un modelo de referencia para la clasificación.

2. **Naive Bayes**: Se implementa el algoritmo de Naive Bayes como una alternativa de clasificación.

3. **Random Forest**: Se utiliza un modelo de Random Forest para aprovechar la capacidad de ensemble learning.

4. **Support Vector Machine**: Se aplica un Support Vector Machine (SVM) para explorar otro enfoque de clasificación.

### Selección del Modelo

Después de entrenar y evaluar los cuatro modelos, se selecciona el modelo de Random Forest con una profundidad máxima de 9 debido a su alto rendimiento, con un accuracy de 0.85 en la predicción de supervivencia.

### Regularización y Optimización de Parámetros

Se realiza un proceso de regularización y optimización de parámetros para mejorar la precisión del modelo seleccionado y evitar el sobreajuste.

### Interfaz Gráfica

El proyecto culmina con la creación de una interfaz gráfica que permite a los usuarios ingresar datos de pasajeros del Titanic y obtener una predicción de supervivencia utilizando el modelo de Random Forest optimizado.

## Estructura del Repositorio

- **data**: Contiene el conjunto de datos original del Titanic descargado desde Kaggle.
- **notebooks**: Contiene Jupyter Notebooks que detallan el proceso de limpieza, transformación de variables, entrenamiento de modelos y optimización.
- **scripts**: Contiene scripts necesarios para el procesamiento de datos y la creación de la interfaz gráfica.
- **models**: Almacena los modelos entrenados y los archivos de optimización.
- **webapp**: Contiene todos los archivos relacionados con la interfaz gráfica del usuario.

## Links a archivos de los entregables (Las cosas importantes):

- [Entregable 1: 14/08/2023](Pipe/DataCleansing.ipynb) - Limpieza y transformación de datos. Path: `Pipe/DataCleansing.ipynb`. Los resultados de la limpieza se guardan en `Data/train_clean.csv`.
- [Entregable 2: 28/08/2023](Model/resultados_modelos.ipynb) - Notebook con las pruebas de modelos hechas y con su comparación. 
- [Entregable 3: 04/09/2023](Model/ModeloMejorado.ipynb) - Reporte con el modelo refinado.
- **Revisa_competencias:** [Etregable Final con código: 13/09/2023](Entrega_Final/Codigo_Final.ipynb) - Reporte con código final. En el se recopilan las 3 entregas anteriores y se realizan las correcciones solicitadas. 
- **Revisa_competencias:** [Entregable Final Reporte: 13/09/2023](Entrega_Final/Reporte_Final_Titanic_Equipo_4.pdf)
- **Revisa_competencias :** [Interfaz gráfica: 13/09/2023](Interface/Home.py)

## ¿Cómo esta organizado nuestro repositorio?
Nuestro arbol de archivos se ve como sigue:
```
📦RetoTitanicBloque1
 ┣ 📂Data
 ┃ ┣ 📜test.csv
 ┃ ┣ 📜train.csv
 ┃ ┗ 📜train_clean.csv
 ┣ 📂Interface
 ┃ ┣ 📂figures
 ┃ ┃ ┣ 📜.gitkeep
 ┃ ┃ ┣ 📜DALL·E 2023-08-28 10.39.13 - ship sinking minimalistic color logo.png
 ┃ ┃ ┣ 📜jack.jpeg
 ┃ ┃ ┣ 📜JackSwim.gif
 ┃ ┃ ┣ 📜jackWater.jpeg
 ┃ ┃ ┣ 📜logo.png
 ┃ ┃ ┗ 📜rose.png
 ┃ ┣ 📜.gitkeep
 ┃ ┣ 📜Home.py
 ┃ ┗ 📜model.pkl
 ┣ 📂Model
 ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📜GaussianNB.cpython-311.pyc
 ┃ ┃ ┣ 📜GaussianNB.cpython-39.pyc
 ┃ ┃ ┣ 📜logistic.cpython-39.pyc
 ┃ ┃ ┣ 📜Random_Forest.cpython-311.pyc
 ┃ ┃ ┣ 📜Random_Forest.cpython-39.pyc
 ┃ ┃ ┣ 📜SVM_titanic.cpython-311.pyc
 ┃ ┃ ┗ 📜SVM_titanic.cpython-39.pyc
 ┃ ┣ 📜.gitkeep
 ┃ ┣ 📜GaussianNB.ipynb
 ┃ ┣ 📜GaussianNB.py
 ┃ ┣ 📜logistic.py
 ┃ ┣ 📜LogisticRegression.ipynb
 ┃ ┣ 📜Random_Forest.py
 ┃ ┣ 📜resultados_modelos.ipynb
 ┃ ┗ 📜SVM_titanic.py
 ┣ 📂Pipe
 ┃ ┣ 📜.gitkeep
 ┃ ┣ 📜cleaning_funcs.py
 ┃ ┗ 📜DataCleansing.ipynb
 ┣ 📂Results
 ┃ ┣ 📜LR_gender_submission.csv
 ┃ ┗ 📜RandomForest_gender_submission.csv
 ┣ 📂Testing
 ┃ ┣ 📜pruebas_ana.ipynb
 ┃ ┣ 📜pruebas_diego.ipynb
 ┃ ┣ 📜pruebas_elias.ipynb
 ┃ ┗ 📜pruebas_romo.ipynb
 ┣ 📜.gitignore
 ┗ 📜README.md
```
En las cuales lo que hay en cada caso es:
 - `Data`: Los datos en crudo. principalmente en .csv
 - `Interface`: Aquí estara todo lo que programemos de la interfaz gráfica.
 - `Model`: Todos nuestros scripts de modelos funcionando asi como el notebook con el segundo entregable.
 - `Pipe`: Las funciones de transformación que llevan los datos crudos a los inputs en el modelo. Aqui esta el primer entregable como jupyter y tambien tenemos las funciones para repetir esto facilmente con otros datos.
 - `Testing`: Aqui guardaremos nuestro playground. Hay notebooks en sucio en los que hacemos pruebas varias y no debe de haber entregables en esta carpeta.


## Correcciones en el entregable final respecto a las retroalimentaciones
- **Entregable 1: 14/08/2023** - Limpieza y transformación de datos: Se cambió la técnica usada para rellenar valores nulos de la variable **Age** como lo indicó el profesor en la retroalimentación.
- **Entregable 2: 28/08/2023** - Se agregó una descripción de los modelos utilizados en el readme. Se agregó una descripción (nombre y URL) del dataset utilizado. Se agregó la sección de correcciones. Se incluye el enlace donde se puede descargar la base de datos en el reporte. Se hace una descripcion de las variables en crudo y después de ser procesadas. Se incluye descripcion del problema claramente. Se modifican hiperparametros en cada modelo y se explica por qué. Se incluye sección donde se explica las metricas a usar para comparar y como se separa en train y test. Se corrigen errores ortográficos y datos faltantes en el reporte. Se incluye interpretacion de la comparativa de resultados.
- **Entregable 3: 04/09/2023** - El reporte ahora incluye claramente la separación del dataset en entrenamiento, validación, y prueba. Se incluye la metodología a seguir al inicio de cada sección. Se incluye cuáles métricas de desempeño se van a usar y qué hiper-parámetros van a variar. Se mejoró la interpretación de los resultados con un análisis más profundo. Se incluyen pruebas relacionadas con el efecto de regularizacion (optimizacion de parametros en el caso de un random forest) para interpretar sesgo y varianza.


Este proyecto tiene como objetivo proporcionar una comprensión completa de cómo se pueden aplicar técnicas de limpieza de datos y machine learning a un conjunto de datos real como el del Titanic, y cómo se puede implementar una interfaz gráfica para hacer predicciones basadas en el modelo entrenado. ¡Disfrute explorando y aprendiendo!