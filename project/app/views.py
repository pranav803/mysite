from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.


def hi(request):
    return render(request, 'app/hi.html')


'''#return HttpResponse('<h1>hi</h1>')'''
