from django.shortcuts import render
import pagarme

#You can pass your api_keys as enviroment variable if you wanna
CRYP_KEY = 'cryp_key from dashboard'

def test(request):
    # You cryp key, founded in Pagar.me dashboard
    key = CRYP_KEY

    # Pull the list of products here
    items = [
        {
            'id': '1', 
            'title': 'Soccer Ball',
            'unit_price': 55000,        #Value in R$ cents
            'quantity': 1
        },
        {
            'id': '2',
            'title': 'Caderno escolar',
            'unit_price': 3200,              #Value in R$ cents
            'quantity': 3
        }
    ]
    # Calculate the total amount
    amount = 0
    for item in items:
        amount += (item.get('unit_price') * item.get('quantity'))
    

    #Max number of installments you wish. Remember Pagar.me accept value lower or equal 12.
    maxInstallments = 6

    context = { 
        'key': key,
        'valor_compra': amount,
        'lista_items': items,
        'installments': maxInstallments
        }

    return render(request, 'test.html', context)