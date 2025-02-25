# Gestor de Documentos

[![Streamlit](https://img.shields.io/badge/Deploy%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org)

## Descripción
**Gestor de Documentos** es una  aplicación web desarrollada en Python utilizando Streamlit. Su objetivo es automatizar la verificación y compresión de documentos PDF basados en datos prevenientes de un archivo Excel.La aplicación permite:

- Subir un archivo excel que contiene una lista de facturas
- Subirmúltiples archivos PDF
- Extraer el identificador de facturas de cada PDF
- Comparar estos identificadores con los datos del Excel
- Notificar al usuario sobre la validez de cada documento
- Generar un archivo ZIP con los documentos validados para su descarga

## Características

- **Carga dinámica del Excel:** Cada vez que se sube un archivo Excel, se procesa y limpia para extraer la lista de facturas.
- **Verificación de documentos PDF:** Extraer el identificador de Facturas desde el nombre del archivo (formato: 'prefijo-Identificador.pdf') usando expresiones regulares.
- **Alertas interactivas:** Notifica si el documento cumple con el formato esperado,si esta presente en el Excel o si no se encuentra disponible
- **Generación de ZIP:** Los archivos validados se alamcenan temporalmente y se comprimen en un archivo ZIP listo para ser descargado

[!IMPORTANT]
- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **openpyxl** (para leer archivos Excel)
- Además, se utilizan módulos est+andar de Python como 're', 'io' y 'zipfile'
