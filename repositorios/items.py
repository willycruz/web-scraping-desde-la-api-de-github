import scrapy

# Definiendo items
class RepositorioItem(scrapy.Item):
    # información del repositorio
    titulo = scrapy.Field()
    description = scrapy.Field()
    commits = scrapy.Field()
    watch = scrapy.Field()
    star = scrapy.Field()
    fork = scrapy.Field()
    colaboradores = scrapy.Field()
    fecha_actualizacion = scrapy.Field()
    url_repositorio = scrapy.Field()
    # información del lenguaje
    nombre_lenguajes = scrapy.Field()