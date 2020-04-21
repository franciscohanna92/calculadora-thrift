# Calculadora con Thrift
En este proyecto de ejemplo, se utilizó el framework para desarrollo RPC llamado Apache Thrift para desarrollar un servicio que provee las operaciones básicas de una calculadoras más una operación que permite identificar si un número es par o impar.

A partir del código generado por Thrift, se implementaron cliente y servidor en Python.

## ¿Qué es Thrift?
Thrift es un framework que permite especificar la interfaz de servicios en archivos thrift, los cuales cuentan con una sintaxis muy similar a C. A partir de esta especificación del servicio, Thrift permite generar código en varios lenguajes (C#, Java, Python, etc) que contiene la lógica para la transmisión de información por la red (marshalling, empaquetado, etc). Luego, en el lenguaje de preferencia se codificación las implementaciones necesarias para cliente y servidor, proveyendo implementación para las operaciones ofrecidas por el servicio (especificadas en el archivo thrift del servicio).

Podés leer más en la página oficial del [proyecto Apache Trhift.](https://thrift.apache.org/)

## ¿Cómo usar este ejemplo?

1. Clonar el reposotiro
`git clone `

2. Instalar las dependencias
`pip install -r requirements.txt`

3. Correr el servidor en un terminal
`python server.py`

4. Correr el cliente en otro terminal
`python client.py`