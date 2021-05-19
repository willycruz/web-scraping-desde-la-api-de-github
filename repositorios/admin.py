from django.contrib import admin
from repositorios.models import Usuario, Repositorio

# Register your models here.

class RepositorioAdmin(admin.ModelAdmin):
	list_display = ('titulo','descripcion','star','fork','fecha_creacion','fecha_actualizacion',
					'url_commits','url_colaboradores','url_lenguajes','url_repositorio')


class UserAdmin(admin.ModelAdmin):
	list_display = ('nombre','apellido','email','password')
	search_fields = ('nombre','apellido')


admin.site.register(Repositorio, RepositorioAdmin)
admin.site.register(Usuario, UserAdmin)
