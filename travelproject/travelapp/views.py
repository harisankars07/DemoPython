from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from.models import Place
from.models import Team


def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'solution':obj1})
#
# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("how r u?")

