from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Widget

def index(request):
    widgets = Widget.objects.all()
    total = widgets.aggregate(Sum('quantity'))['quantity__sum']
    print(total)
    return render(request, 'index.html', {'widgets': widgets, 'total': total})

def create(request):
    Widget.objects.create(
        description = request.POST['description'],
        quantity = request.POST['quantity']
    )
    return redirect('/')

def delete(request, widget_id):
    widget = Widget.objects.get(id = widget_id)
    widget.delete()
    return redirect('/')
