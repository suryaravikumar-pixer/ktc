from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def type_scheme(request):
    
    return render(request, 'scheme.html', {'title': 'type Scheme', 'sname':'jetspeed'})