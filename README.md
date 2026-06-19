sistema de registro en pokedex

Este es un programa interactivo desarrollado en Python que permite administrar el contenido de una pokedex mediante una estructura CRUD (Crear, Leer, Actualizar, Eliminar)

Funcionalidades

Este proyecto incluye las siguientes funcionalidades a través de un menú interactivo:

Registrar Pokemon: Permite agregar un nuevo libro al sistema solicitando Nombre, Tipos,, etapa de evolucion, region y generacion del pokemon. Valida que no existan duplicados y que los campos no estén vacíos. *Mostrar Pokedex: Muestra la lista completa de todos los pokemon registrados en el sistema de manera ordenada.
Modificar datos del pokemon: Modifica los datos de un pokemon existente buscando por su nombre. Protege los formatos con manejo de excepciones.
Eliminar pokemon: Elimina un libro del sistema de forma permanente buscando por su título.

Requisitos Técnicos Aplicados

Uso de listas principales para guardar los nombres de los pokemon y diccionarios como bases de datos en memoria para guardar los tipos, la etapa de evolucion, la region y la generacion del pokemon.
Uso de funciones independientes y debidamente documentadas.
Validaciones de texto vacío y manejo de excepciones (try/except) para asegurar que el formato de la etapa de evolucion, region y generacion del pokemon sea un número entero (int) obligatorio.
