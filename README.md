# Reto equipo #4: Supervivencia en el Titanic

## Links a archivos de los entregables (Las cosas importantes):

- [Entregable 1: 14/08/2023](Pipe/DataCleaning.ipynb) - Limpieza y transformación de datos. Path: `Pipe/DataCleaning.ipynb` 
- [File 2](./path/to/file2.ext) - Description of File 2
- [File 3](./path/to/file3.ext) - Description of File 3

## ¿Cómo esta organizado nuestro repositorio?
Nuestro arbol de archivos se ve como sigue:
```
📦RetoTitanicBloque1
 ┣ 📂Data
 ┃ ┣ 📜test.csv
 ┃ ┗ 📜train.csv
 ┣ 📂Interface
 ┃ ┗ 📜.gitkeep
 ┣ 📂Model
 ┃ ┗ 📜.gitkeep
 ┣ 📂Pipe
 ┃ ┣ 📜.gitkeep
 ┃ ┣ 📜cleaning_funcs.py
 ┃ ┗ 📜DataCleaning.ipynb  **Primer entregable**
 ┣ 📂Testing
 ┃ ┣ 📜pruebas_diego.ipynb
 ┃ ┣ 📜pruebas_elias.ipynb
 ┃ ┗ 📜pruebas_romo.ipynb
 ┃ ┗ 📜pruebas_ana.ipynb
 ┣ 📜.gitignore
 ┗ 📜README.md
```
En las cuales lo que hay en cada caso es:
 - `Data`: Los datos en crudo. principalmente en .csv
 - `Interface`: Aquí estara todo lo que programemos de la interfaz gráfica.
 - `Model`: Todos nuestros scripts de modelos funcionando.
 - `Pipe`: Las funciones de transformación que llevan los datos crudos a los inputs en el modelo. Aqui esta el primer entregable como jupyter y tambien tenemos las funciones para repetir esto facilmente con otros datos.
 - `Testing`: Aqui guardaremos nuestro playground. Hay notebooks en sucio en los que hacemos pruebas varias y no debe de haber entregables en esta carpeta :)

