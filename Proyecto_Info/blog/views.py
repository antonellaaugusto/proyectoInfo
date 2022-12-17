from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse


from django.views.generic import ListView, DetailView, TemplateView , CreateView , UpdateView, DeleteView
from .models import AgregarComentario

from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
#def mi_vista(request):
#    return HttpResponse("<h1>IVAN XD</h1><h2>HOLAAaa</h2> ")

#pruebas con html url /documento

# def documento (request):
#     documento = """
#     <html>
#     <body>
#     <h1>
#     DOCUMENTO PRIMERA PAGINA 
#     </h1>
#     <h2 stylo = "color: red">
#     Pruebas de html
#     </h2>
#     </body>
#     </html>

# def documento (request):
#     documento = """
#     <html>
#     <body>
#     <h1>
#     DOCUMENTO PRIMERA PAGINA 
#     </h1>
#     <h2>
#     Pruebas de html
#     </h2>
#     </body>
#     </html>
# >>>>>>> 025b6aba83884c178f7d4563a1675850a7d4c8ed

# #     """ 
# #     return HttpResponse(documento)


class Inicio(ListView):
    model = AgregarComentario
    template_name = 'inicio.html'
    ordering = ['-created_date']


class ComentarioDetalle(DetailView):
    model = AgregarComentario
    template_name = 'comentario_detalle.html'

class CrearComentario(CreateView):
    model = AgregarComentario
    form_class = PostForm
    template_name= 'crear_comentario.html'

class EditarComentario(UpdateView):
    model = AgregarComentario
    form_class = PostForm
    template_name = 'edit_comentario.html'

class BorrarComentario(DeleteView):
    model = AgregarComentario
    template_name = 'borrar_comentario.html'
    success_url = reverse_lazy('dashboard_blog')

class Nosotros(TemplateView):
    template_name = "nosotros.html"

class MisionObjetivo(TemplateView):
    template_name = "misionyobjetivo.html"

class DashboardBlog(ListView):
    model = AgregarComentario
    template_name = 'dashboard_blog.html'
    paginate_by = 4
    ordering = ['-created_date']
        