from django.shortcuts import render, redirect
from .models import Produto, Venda, Vendedor, ProdutoVenda

def index(request):
    return render(request, 'app_vendas/index.html')

# RF-1: Cadastrar produto
def cadastrar_produto(request):
    if request.method == 'POST':
        descricao = request.POST['descricao']
        preco = request.POST['preco']
        Produto.objects.create(descricao=descricao, preco=preco)
        return redirect('index')
    return render(request, 'app_vendas/cadastrar_produto.html')

# RF-2: Iniciar venda
def iniciar_venda(request):
    vendedores = Vendedor.objects.all()
    if request.method == 'POST':
        vendedor_id = request.POST['vendedor_id']
        data = request.POST['data']
        vendedor = Vendedor.objects.get(id=vendedor_id)
        Venda.objects.create(vendedor=vendedor, data=data)
        return redirect('index')
    return render(request, 'app_vendas/iniciar_venda.html', {'vendedores': vendedores})

# RF-3: Inserir produto na venda
def inserir_produto_venda(request, venda_id):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        produto_id = request.POST['produto_id']
        quantidade = request.POST['quantidade']
        valor_unitario = request.POST['valor_unitario']
        venda = Venda.objects.get(id=venda_id)
        produto = Produto.objects.get(id=produto_id)
        ProdutoVenda.objects.create(venda=venda, produto=produto, quantidade=quantidade, valor_unitario=valor_unitario)
        return redirect('index')
    return render(request, 'app_vendas/inserir_produto_venda.html', {'produtos': produtos, 'venda_id': venda_id})

# RF-4: Fechar venda
def fechar_venda(request, venda_id):
    venda = Venda.objects.get(id=venda_id)
    produtos_venda = ProdutoVenda.objects.filter(venda=venda)
    total_venda = 0
    produtos_com_subtotal = []

    for pv in produtos_venda:
        subtotal = pv.quantidade * pv.valor_unitario
        total_venda += subtotal
        produtos_com_subtotal.append({
            'produto': pv.produto.descricao,
            'quantidade': pv.quantidade,
            'valor_unitario': pv.valor_unitario,
            'subtotal': subtotal
        })

    if request.method == 'POST':
        # Lógica para fechar a venda (possivelmente atualizar o status da venda)
        return redirect('index')

    return render(request, 'app_vendas/fechar_venda.html', {
        'venda': venda,
        'produtos_venda': produtos_com_subtotal,
        'total_venda': total_venda
    })


# Listar vendas ativas
def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'app_vendas/listar_vendas.html', {'vendas': vendas})

# Cadastrar Vendedor
def cadastrar_vendedor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Vendedor.objects.create(nome=nome)
        return redirect('index')
    return render(request, 'app_vendas/cadastrar_vendedor.html')
