# PruebaBackendEMQU

Para esta prueba decidí utilizar Flask, una instancia local de MySQL y manejar los paquetes usando Conda. El desarrollo se realizó en una computadora corriendo Ubuntu 22.04.

El schema y un conjunto de datos de prueba se encuentran dentro de la carpeta ` /schemas` para recrear la base de datos utilizada.

Para importar los paquetes utilizados se debe correr el siguiente comando usando de conda: ```conda env create --name PruebaEMQU_ABC --file=environment.yml```

Para correr la prueba, se deberá navegar a la carpeta del proyecto, en este caso `../PruebaBackendEMQU/`, activar el ambiente de Conda utilizando el comando `conda activate PruebaEMQU_ABC`, y posteriormente correr el comando `python3 run.py` para comenzar el servidor local. 

Una vez corriendo, se debe visitar la dirección IP indicada, en este caso http://127.0.0.1:5000. Una vez ahí se podrá hacer el recorrido del sitio de prueba.

# Pruebas del programa corriendo
## Dashboard
![](./capturas/Dashboard.png "")

## Agregar un equipo
![](./capturas/Agregar.png "")
![](./capturas/NewEquipo.png "")

## Remover un equipo
![](./capturas/Delete.png "")

## Editar un equipo
![](./capturas/Edit.png "")
![](./capturas/Editado.png "")

## Pingear a los equipos y mostrar los resultados
![](./capturas/Pings.png "")
![](./capturas/ResultadosPings.png "")