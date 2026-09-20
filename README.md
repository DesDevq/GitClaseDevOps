Proyecto de una calculadora para la clase DevOps 2026-2

Explicación de cada comando de git usados en el repositorio:

git init:
Con el comando git init se inicializa el repositorio dentro de la carpeta.

git add:
El comando git add [nombre del archivo] o git add . (en el caso de que el programador quiera agregar todos los cambios realizados) sirve para elegir qué archivos van a entrar en el siguiente commit.

git commit:
El comando git commit guarda en local los archivos que se agregaron con git add, junto a un mensaje que quiere dejar el desarrollador. Siempre es recomendado escribir un mensaje claro de qué se actualizó en el código.

git push:
git push sirve para subir al repositorio de GitHub los commits que se hicieron en local.

git status:
git status nos sirve para verificar que archivos faltan por incluir en el git add. También muestra qué archivos ya están listos para el commit.

git diff:
Nos sirve para ver las diferencias entre lo que estaba antes y lo que se cambió en los archivos, línea por línea. Las líneas con - son las que se eliminaron y las líneas con + son las que se agregaron. Es útil para revisar los cambios antes de hacer el commit.

git log:
Nos sirve para verificar desde la terminal los commits realizados teniendo información del autor, y la fecha exacta junto el mensaje del commit.

git restore:
El comando git restore [nombre del archivo] sirve para deshacer los cambios que se hicieron en un archivo y que todavía no se han agregado con git add. El archivo vuelve a quedar como estaba en el último commit.
