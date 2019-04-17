from django.shortcuts import render
import pagarme

def teste(request):
    # Inserir sua chave criptograda
    key = CRYP_KEY
    # Inserir o valor da venda
    valor_total = 500 

    # insira a lista de produtos da compra especificada
    items = [
        {
            'id': '1', 
            'title': 'Bola de futebol',
            'unit_price': 1000,
            'quantity': 1
        },
        {
            'id': '2',
            'title': 'Caderno escolar',
            'unit_price': 3200,
            'quantity': 3
        }
    ]

    context = { 
        'key': key,
        'valor_compra': valor_total,
        'lista_items': items
        }

    return render(request, 'teste.html', context)