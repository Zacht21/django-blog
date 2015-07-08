from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from .models import Entrada

class IndexView(ListView):
    template_name = 'index.html'
    model = Entrada


class EntradaDetailView(DetailView):
    template_name = 'entrada_detail.html'
    model = Entrada

def home(request):
    contenido = {
        'blog': 'zBlog',
        'titulo': 'Primer titulo',
        'contenido': 'Primer contenido del blog, modificacion al primer contenido dinamico',
        'autor': 'Zacht',
        'dia': '07/JUL/2015',
    }
    return render_to_response('index2.html', contenido)
    # entradas = Entrada.objects.all()[:10]
    # return render_to_response(
    #     'index2.html',
    #     {
    #         'articulos' : entradas
    #     }
    # )
