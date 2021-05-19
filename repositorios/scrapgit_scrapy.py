# Bibliotecas para Web Scraping
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from scrapy.crawler import CrawlerRunner # Permite automarizar el scraping en scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime

# MONGODB
from pymongo import MongoClient
client = MongoClient('localhost')
db = client['db_repositorios']
col = db['repositorios_repositorio']

class ExtractorRepositorio(CrawlSpider):
    name = 'github'
    item_count = 0

    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        'LOG_ENABLED': False # Evitar mostrar los logs
    }

    allowed_domain = ['www.github.com']  # único dominio permitido para visitar
    start_urls = ['https://github.com/search?q=programacion+con+python', # programación con Python
                  #'https://github.com/search?q=python+y+django&type=Repositories'  # Python y Django
                  'https://github.com/search?q=jacoco' # Jacoco
                  #'https://github.com/search?q=programacion+con+java&type=Repositories', #programacion con Java
                  #'https://github.com/search?q=laravel&type=Repositories', # Laravel
                  #'https://github.com/search?q=django&type=Repositories', # Framework Django
                  #'https://github.com/search?q=FICTIZIA' # FICTIZIA
                  ]  # URLs semillas

    # Definición de reglas (tuplas) permiten realizar web scraping horizontal y vertical
    rules = {
        # Paginación
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="next_page"]'))), # Siguiente página
        # Infomación de los repositorios
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="v-align-middle"]')), # Título de repositorios
                            callback = 'parse_item', follow = False)
    }

    def parse_item(self, response):
        # Información repositorio
        titulo = response.xpath('normalize-space(//strong[@class="mr-2 flex-self-stretch"]/a/text())').get()
        descripcion = response.xpath('normalize-space(//div[@class="BorderGrid-cell"]/p[@class="f4 mt-3"]/text())').get()
        commits = response.xpath('normalize-space(//span[@class="d-none d-sm-inline"]/strong/text())').get()
        #watch = response.xpath('normalize-space(//*[@id="js-repo-pjax-container"]/div[1]/div[1]/ul/li[1]/form/a/text())').get()
        #star = response.xpath('normalize-space(//*[@id="js-repo-pjax-container"]/div[1]/div[1]/ul/li[2]/div/form[2]/a/text())').get()
        #fork = response.xpath('normalize-space(//*[@id="js-repo-pjax-container"]/div[1]/div[1]/ul/li[3]/a/text())').get()
        colaboradores = response.xpath('normalize-space(//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[4]/div/h2/a/span/text())').get()
        fecha_actualizacion = response.xpath('normalize-space(//*[starts-with(@class, "link-gray ml-2")]/relative-time/text())').get()
        nombre_lenguajes = response.xpath('//li[@class="d-inline"]//span/text()').get()
        url_repositorio = response.xpath('normalize-space(//*[starts-with(@class, "input-group")]/input/@value)').get()

        # Limpieza
        titulo = titulo.replace('-', ' ').replace('/', '').replace('_', ' ').strip()
        descripcion = descripcion.replace('-', '').replace('/', '').replace('_', ' ').strip()
        commits = commits.replace(',','').strip()
        #watch = watch.replace(' ','').strip()
        #star = star.replace(' ','').strip()
        #fork = fork.replace(' ','').strip()
        colaboradores = colaboradores.replace(',','').strip()
        fecha_actualizacion = fecha_actualizacion.replace('on', '').strip()


        #f = open('./item_repositorios_scrapy5.csv','a')
        #f.write(titulo+","+descripcion+","+commits+","+colaboradores+","+fecha_actualizacion+","+nombre_lenguajes+","+url_repositorio+"\n")
        #f.close()                       #+watch+","+star+","+fork+","

        col.update_one({
            "titulo": titulo
            #"descripcion": descripcion
        },{
            "$set": {
                "descripcion": descripcion,
                "commits": commits,
                "colaboradores": colaboradores,
                "fecha_actualizacion": fecha_actualizacion,
                "nombre_lenguajes": nombre_lenguajes,
                "url_repositorio": url_repositorio,
                "titulo": titulo
            }
        }, upsert=True) # upsert --> Operación de INSERCIÓN en caso de no existir un documento
                        # que cumpla con mi condición. Y Operación de ACTUALIZACIÓN en caso de que
                        # exista un documento que cumpla con mi condición.

        #self.item_count += 1
        #if self.item_count > 20:
         #   raise CloseSpider('item_exceeded')
        #yield git_item

# Permite iniciar scrapy
process = CrawlerProcess()
process.crawl(ExtractorRepositorio)
process.start()

#runner = CrawlerRunner()
#task = LoopingCall(lambda: runner.crawl(ExtractorRepositorio)) # LoopingCall--> Llamada iterativa
#task.start(20) # tiempo (segundos) de ejecución automática
#task.run()