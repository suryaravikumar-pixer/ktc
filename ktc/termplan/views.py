from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def type_plan(request):
    return render(request, 'termplan.html', {'title': 'type plan', 'tname':'60days'})