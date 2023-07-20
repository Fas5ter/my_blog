from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render

class HelloWorld(View):
    def get(self, request):
        data = {
            'name' : 'Cristian Armando Larios Bravo',
            'years' : 19,
            'codes' : ['Python', 'Django', 'React']
        }
        return render(request, 'hello_world.html', context=data)