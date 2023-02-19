from django.http import HttpResponse
from django.shortcuts import render
from .models import Supply
import pandas as pd
from django.db.models import Sum


def get_report(request):
    items_supply = []
    data = {'item': None}
    total = 0
    qs = Supply.objects.values('item__model', 'storage__name').annotate(amount=Sum('amount')).order_by('item')
    for item in qs:
        if data['item'] != item['item__model']:
            if data['item'] is not None:
                data['total'] = total
                items_supply.append(data)
                total = 0
                data = {}
            data['item'] = item['item__model']
        data[item['storage__name']] = item['amount']
        total += item['amount']
    data['total'] = total
    items_supply.append(data)
    items_supply.sort(key=lambda x: -len(x))
    df = pd.DataFrame.from_dict(items_supply)
    df.sort_index(axis=1)
    df.to_excel('items.xlsx', index=False)
    with open('items.xlsx', 'rb') as file:
        data = file.read()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
        response.write(data)
        return response


def home(request):
    return render(request, 'main/index.html')