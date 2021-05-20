# web-scraping-desde-la-api-de-github
Software para Web Scraping desde las APIS de repositorios de código

ScrapGit, así como se ha denominado a la aplicación desarrollada corre bajo el sistema operativo Windows.
Para el funcionamiento de este, también se debe tener instalado el framework Django. Este posee su propio servidor local.
Asimismo, para el efecto de modificación o realizar algún aporte al programa, es necesario tener instalado los editores (IDEs), puede ser cualquiera que permita realizar proyectos basados en el lengueje Python, y logicamente tener instalado el lenguaje Python. 
Además de ello será necesario instalar MongoDB, ya que el software utiliza este base de datos NoSQL para almacenar los datos.

Importante indicar que este software utiliza API de GitHub para llevar acabo su objetivo, es decir, para realizar Web Scraping desde la API de GitHub, valga la redundancia.
El archivo web-scraping-desde-la-api-de-github/repositorios/scrapgit_api.py, es el que contiene el códgigo que permite hacer Web Scraping, ahí ocurre toda la magia de esta técnica. 
En el mismo archivo está el código que permite el almacenamiento de la información a la base de datos luego de scrapear los repositorios. Es necesario indicar que en la base de datos sólo se guardarán (ítems de GitHub) lo que se haya optado como necesarios o importantes del repositorio.
