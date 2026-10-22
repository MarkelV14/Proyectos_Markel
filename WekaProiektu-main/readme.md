# Weka Tweet Sentiment Analysis

Proiektu hau Twitter-eko mezuak aztertzeko eta sentimenduak (negatiboa, positiboa, neutrala eta irrelevantea) sailkatzeko Java eta Weka liburutegia erabiltzen dituen ikaskuntza automatikoko (Machine Learning) aplikazioa da. Eredu optimizatua eraikitzeko, prozesamendu naturaleko teknika (NLP) aurreratuak eta parametroen optimizazio automatikoa erabiltzen dira.

### Ezaugarri Nagusiak
*   **Datuen Aurreprozesamendua (`CSVPreprocessor.java`):**
    *   Twitter-eko zarata garbitzen du (URLak, @aipamenak eta RTak kentzen ditu).
    *   Komatxo arteko lerro-jauziak zuriune bihurtzen ditu CSV fitxategien formatua ez apurtzeko.
    *   Trebatze-datuetan (Training), 5 agerpen baino gutxiago dituzten klase minoritarioak (fantasmak) dinamikoki baztertzen ditu.
*   **Prozesamendu Lexikoa eta NLP:**
    *   `StringToWordVector` iragazkia erabiltzen da 5000 hitzeko hiztegiarekin eta TF-IDF eraldaketarekin.
    *   Hapax hitzak (behin bakarrik agertzen direnak) kentzen ditu (`minFreq=2`) generalizazio hobea lortzeko.
    *   Unigramak eta bigramak sortzeko `NGramTokenizer` erabiltzen du.
    *   SVM ereduarentzat ezinbestekoa den L2 normalizazioa aplikatzen du.
*   **Ereduaren Optimizazioa (Grid Search):**
    *   Klasifikaziorako `SMO` (Support Vector Machine) algoritmoa erabiltzen du `PolyKernel` lineal batekin.
    *   `InfoGain` bidezko atributu-hautaketa eta SMOren `C` parametroa automatikoki optimizatzen ditu 10 fold-eko Cross-Validation bidez.
    *   Klaseen desoreka konpontzeko `ClassBalancer` erabiltzen du pisuak doituz.

### Nola Exekutatu

Aplikazioa exekutatzeko, Weka liburutegia (`weka.jar`) zure proiektuko *classpath*-ean egon behar da. Kodea konpilatu ondoren, komando hau erabil dezakezu terminalean:

```bash
java -cp ".:weka.jar" proiektu.TweetSentiment <train_datuak.csv> <test_datuak.csv> <iragarpen_fitxategia.txt> <log_fitxategia.txt>
```

**Exekuzio adibidea:**
```bash
java -cp ".:weka.jar" proiektu.TweetSentiment data/tweetSentiment.train.csv data/tweetSentiment.dev.csv Iragarpenak/iragarpenak.txt Iragarpenak/informe_resultados.txt
```
*(Oharra: Parametroak eman ezean, aplikazioak lehenetsitako ibilbideak erabiliko ditu datuak eta emaitzak kargatzeko eta gordetzeko.)*

---

Este proyecto es una aplicación desarrollada en Java que utiliza la librería Weka para la clasificación de sentimientos en tweets (negativo, positivo, neutral e irrelevante). Implementa un pipeline completo que abarca desde la limpieza profunda de los datos hasta la optimización automática del modelo de clasificación mediante búsqueda en cuadrícula (Grid Search).

### Características Principales
*   **Preprocesamiento de Datos (`CSVPreprocessor.java`):**
    *   Limpia el ruido típico de Twitter mediante la eliminación de URLs mediante expresiones regulares, menciones (@) y retweets (RT).
    *   Arregla fallos estructurales del CSV reemplazando los saltos de línea y comillas internas defectuosas.
    *   Filtra de manera dinámica aquellas filas con clases minoritarias (con menos de 5 apariciones) en el conjunto de entrenamiento.
*   **Procesamiento de Lenguaje Natural (NLP):**
    *   Utiliza `StringToWordVector` con un límite de 5000 palabras y transformaciones TF-IDF.
    *   Elimina palabras con frecuencia menor a 2 (Hapax legomena) para mejorar la generalización del modelo.
    *   Extrae unigramas y bigramas utilizando `NGramTokenizer`, y aplica Stemming (Lovins).
    *   Aplica normalización L2, un paso crítico para estabilizar el hiperplano en modelos SVM.
*   **Clasificador y Optimización de Hiperparámetros:**
    *   El modelo principal es `SMO` (Support Vector Machine) con un kernel polinómico lineal (`PolyKernel` exponente 1.0).
    *   Implementa un Grid Search que cruza la cantidad óptima de atributos (evaluados vía `InfoGain`) con el parámetro de complejidad `C` del algoritmo SMO.
    *   Aplica `ClassBalancer` de Weka para asignar pesos a las instancias y compensar el desbalanceo de las clases durante el entrenamiento.

### Cómo Ejecutar

Asegúrate de tener instalado Java y de incluir la librería `weka.jar` en el classpath de tu proyecto al momento de compilar. Para ejecutar el pipeline completo, usa el siguiente comando:

```bash
java -cp ".:weka.jar" proiektu.TweetSentiment <ruta_train.csv> <ruta_test.csv> <salida_predicciones.txt> <salida_log.txt>
```

**Ejemplo de ejecución:**
```bash
java -cp ".:weka.jar" proiektu.TweetSentiment data/tweetSentiment.train.csv data/tweetSentiment.dev.csv Iragarpenak/iragarpenak.txt Iragarpenak/informe_resultados.txt
```
*(Nota: Si ejecutas el programa sin argumentos, utilizará automáticamente las rutas predeterminadas establecidas en el código para procesar los datos y guardar los reportes.)*