from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    context = {
        "title": "walaa",
    }
    return render(request, 'index.html', context)
    