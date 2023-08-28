# Reto equipo #4: Supervivencia en el Titanic

## Links a archivos de los entregables (Las cosas importantes):

- [Entregable 1: 14/08/2023](Pipe/DataCleansing.ipynb) - Limpieza y transformación de datos. Path: `Pipe/DataCleansing.ipynb`. Los resultados de la limpieza se guardan en `Data/train_clean.csv`.
- [Entregable 2: 28/08/2023](Model/resultados_modelos.ipynb) - Notebook con las pruebas de modelos hechas y con su comparación. 
- [File 3](./path/to/file3.ext) - Description of File 3

## ¿Cómo esta organizado nuestro repositorio?
Nuestro arbol de archivos se ve como sigue:
```
📦RetoTitanicBloque1
 ┣ 📂Data
 ┃ ┣ 📜test.csv
 ┃ ┣ 📜train.csv
 ┃ ┗ 📜train_clean.csv
 ┣ 📂Interface
 ┃ ┗ 📜.gitkeep
 ┣ 📂Model
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
 - `Testing`: Aqui guardaremos nuestro playground. Hay notebooks en sucio en los que hacemos pruebas varias y no debe de haber entregables en esta carpeta :)

