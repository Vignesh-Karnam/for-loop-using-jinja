from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':'Vignesh'}
    return render(request,'forloop.html',d)