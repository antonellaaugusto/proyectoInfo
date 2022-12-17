from django.urls import path
from .views import Inicio, ComentarioDetalle, CrearComentario, EditarComentario, BorrarComentario, MisionObjetivo, Nosotros, DashboardBlog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('', Inicio.as_view(), name='Inicio'),
    path('comentario/<int:pk>',ComentarioDetalle.as_view(), name='comentario_detalle'),
    path('crear_comentario/', CrearComentario.as_view(), name='crear_comentario'),
    path('comentario/edit/<int:pk>',EditarComentario.as_view(), name='editar_comentario'),
    path('comentario/<int:pk>/remover',BorrarComentario.as_view(), name='borrar_comentario'),
    path('misionyobjetivos',MisionObjetivo.as_view(), name='misionyobjetivo'),
    path('nosotros',Nosotros.as_view(), name='nosotros'),
    path('dashboard_blog',DashboardBlog.as_view(), name='dashboard_blog'),
]

urlpatterns += staticfiles_urlpatterns()