from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pagarme
from prettyprinter import pprint

#You can pass your api_keys as enviroment variable if you wanna
CRYP_KEY = 'your cryp key'

def test(request):
    # You cryp key, founded in Pagar.me dashboard
    key = CRYP_KEY

    # Pull the list of products here
    items = [
        {
            'id': '1', 
            'title': 'Soccer Ball',
            'unit_price': 4000,        #Value in R$ cents
            'quantity': 1
        },
        {
            'id': '2',
            'title': 'Scholar Notebook',
            'unit_price': 2000,              #Value in R$ cents
            'quantity': 2
        },
        {
            'id': '3',
            'title': 'Gloves',
            'unit_price': 500,              #Value in R$ cents
            'quantity': 2
        },
        {
            'id': '4',
            'title': 'Magical Pen',
            'unit_price': 1000,              #Value in R$ cents
            'quantity': 1
        }
    ]
    # Calculate the total amount
    amount = 0
    for item in items:
        amount += (item.get('unit_price') * item.get('quantity'))
    

    # Set the max number of installments you wish. But remember, pagar.me only accept values lower or equal to 12.
    maxInstallments = 4
    #set the number of installments without interest
    freeInstallments = 2
    #set the interestRate 
    interestRate = 10 

    #set the title of the paymentButton
    paymentButton = 'Finalizar a compra'

    context = { 
        'key': key,
        'valor_compra': amount,
        'lista_items': items,
        'installments': maxInstallments,
        'freeInstallments': freeInstallments,
        'interestRate': interestRate,
        'paymentButton': paymentButton
        }

    return render(request, 'test.html', context)

def success(request):
    context = {}
    return render(request, 'success.html', context)

@csrf_exempt
def notification(request):
    # Create here your notification scripts of post-back
    if request.method == 'POST':

        res = request.POST
        pprint(res)    #remove after debuging
        if res['event'] == 'transaction_status_changed':
            
            print(res['transaction[customer][external_id]']) #email type by user in modal
            print(res['current_status'])

            # Alter the value of the status etc.

    return render(request, 'notification.html', {})