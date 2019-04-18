from django.shortcuts import render
import pagarme

#You can pass your api_keys as enviroment variable if you wanna
CRYP_KEY = 'your cryp_key'

def test(request):
    # You cryp key, founded in Pagar.me dashboard
    key = CRYP_KEY

    # Pull the list of products here
    items = [
        {
            'id': '1', 
            'title': 'Soccer Ball',
            'unit_price': 4590,        #Value in R$ cents
            'quantity': 1
        },
        {
            'id': '2',
            'title': 'Scholar Notebook',
            'unit_price': 1798,              #Value in R$ cents
            'quantity': 3
        }
    ]
    # Calculate the total amount
    amount = 0
    for item in items:
        amount += (item.get('unit_price') * item.get('quantity'))
    

    # Set the max number of installments you wish. But remember, pagar.me only accept values lower or equal to 12.
    maxInstallments = 3

    context = { 
        'key': key,
        'valor_compra': amount,
        'lista_items': items,
        'installments': maxInstallments
        }

    return render(request, 'test.html', context)

def success(request):
    context = {}
    return render(request, 'success.html', context)