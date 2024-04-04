from django.contrib import admin
from .models import Time


@admin.register(Time)
class AdminTime(admin.ModelAdmin):
    list_display = ['nome', 'estado', 'cores', 'ano_de_fundacao', 'tem_mundial']
    list_filter = ['nome', 'estado', 'cores', 'ano_de_fundacao', 'tem_mundial']
    search_fields = ['nome', 'estado', 'cores', 'ano_de_fundacao', 'tem_mundial']

