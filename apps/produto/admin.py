from django.contrib import admin
from apps.produto.models import Produto

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'comprador', 'vendedor', 'moeda', 'preco', 'em_estoque')
    search_fields = ('id', 'moeda', 'preco')
    list_filter = ('moeda', 'em_estoque', 'comprador', 'vendedor')
    fieldsets = (
        (None, {
            'fields': ('comprador', 'vendedor', 'moeda', 'preco', 'imagem', 'em_estoque')
        }),
    )
    readonly_fields = ('imagem',)

admin.site.register(Produto, ProdutoAdmin)
