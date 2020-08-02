from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Евгений'
    _context = {'date': date, 'name': name}
    return render(request, 'base.html', _context)