from django.contrib import admin
from .models import Vendedor, Produto, Venda, ProdutoVenda

admin.site.register(Vendedor)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ProdutoVenda)
