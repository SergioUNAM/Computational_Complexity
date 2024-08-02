## Descripción del Proyecto / Project Description

Este repositorio contiene un programa diseñado para medir y analizar el tiempo promedio de acceso a elementos en listas de diferentes tamaños en Python. Los resultados se almacenan en un archivo XML, que luego se utiliza para generar gráficos de los datos recopilados.

This repository contains a program designed to measure and analyze the average access time to elements in lists of various sizes in Python. The results are stored in an XML file, which is then used to generate graphs of the collected data.

### Funcionalidades Principales / Main Features

1. **Medición del Tiempo de Acceso a Elementos en Listas / Measuring List Element Access Time:**
   - El programa crea listas de tamaños variables y mide el tiempo promedio para acceder a elementos en ubicaciones aleatorias.
   - Los tiempos de acceso se registran y almacenan para su posterior análisis.

   - The program creates lists of varying sizes and measures the average time to access elements at random locations.
   - The access times are recorded and stored for further analysis.

2. **Generación de Archivos XML / XML File Generation:**
   - Los resultados de las mediciones se almacenan en un archivo XML estructurado, que incluye datos sobre el tamaño de las listas y los tiempos de acceso promedio.

   - The measurement results are stored in a structured XML file, including data on list sizes and average access times.

3. **Visualización de Datos / Data Visualization:**
   - Incluye una función para leer los datos del archivo XML y generar gráficos utilizando la biblioteca `matplotlib`.
   - Los gráficos muestran la relación entre el tamaño de la lista y el tiempo promedio de acceso, así como la distribución del tiempo de acceso en una lista grande.

   - Includes a function to read the data from the XML file and generate graphs using the `matplotlib` library.
   - The graphs display the relationship between list size and average access time, as well as the distribution of access time in a large list.

### Requisitos / Requirements

- Python 3.x
- Bibliotecas: `matplotlib`

- Python 3.x
- Libraries: `matplotlib`

### Uso / Usage

1. **Medir Tiempos de Acceso / Measure Access Times:**
   - Ejecuta el programa principal para realizar las mediciones y generar el archivo XML con los resultados.

   - Run the main program to perform the measurements and generate the XML file with the results.

2. **Visualización / Visualization:**
   - Usa la función `plot_from_xml` para leer los datos del archivo XML y generar gráficos de los resultados.

   - Use the `plot_from_xml` function to read the data from the XML file and generate graphs of the results.
  
## Explicación Teórica

El objetivo de este proyecto es estudiar el comportamiento del tiempo de acceso a elementos en listas de Python conforme aumenta el tamaño de la lista. Python utiliza una estructura de datos subyacente llamada *array* dinámico para implementar listas, lo que implica que el tiempo de acceso a un elemento es generalmente constante, O(1). Sin embargo, este proyecto busca explorar cómo varía este tiempo en la práctica cuando se trabaja con listas de diferentes tamaños y cuando se accede a elementos aleatorios dentro de estas listas.

### Aspectos Teóricos

1. **Complejidad Temporal O(1)**  
   En teoría, acceder a un elemento en una lista por índice debería ser una operación de tiempo constante debido a la estructura de datos de array subyacente. Esto significa que el tiempo requerido para acceder a cualquier elemento no debería depender del tamaño de la lista.

2. **Factores del Sistema**  
   En la práctica, varios factores pueden influir en el tiempo de acceso a elementos, como la administración de la memoria, la caché de la CPU y la recolección de basura. Este experimento busca cuantificar estos tiempos en un entorno controlado para observar cualquier desviación significativa de la teoría.

3. **Distribución del Tiempo de Acceso**  
   Además de la relación entre el tamaño de la lista y el tiempo de acceso promedio, este proyecto también examina la distribución del tiempo de acceso en diferentes posiciones dentro de una lista grande, para determinar si todas las posiciones son accesibles en aproximadamente el mismo tiempo.

### Lugar Idóneo para la Imagen de la Gráfica

## Resultados y Análisis

En esta sección se presentan los resultados de las mediciones de tiempo de acceso. A continuación se muestra una gráfica que ilustra la relación entre el tamaño de la lista y el tiempo promedio de acceso, así como la distribución del tiempo de acceso en una lista grande.

![Gráfica de Acceso a Listas](ruta/a/la/imagen.png)

### Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir posibles mejoras o nuevas funcionalidades.

### Contribuciones / Contributions

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir posibles mejoras o nuevas funcionalidades.

Contributions are welcome. Please open an issue or a pull request to discuss potential improvements or new features.

### Licencia / License

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

This project is licensed under the MIT License. See the LICENSE file for more details.
