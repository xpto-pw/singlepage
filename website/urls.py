from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('paginas/bernabeu.html', views.bernabeu_page_view, name='bernabeu'),
    path('contactos', views.contactos_page_view, name='contactos'),
    path('contactosNovo', views.contactosNovo_page_view, name='contactosNovo'),
    path('contactosEdita/<str:contacto_id>', views.contactosEdita_page_view, name='contactosEdita'),
    path('contactosApaga/<str:contacto_id>', views.contactosApaga_page_view, name='contactosApaga'),
    path('comentarios', views.comentarios_page_view, name='comentarios'),
    path('jogadorNovo', views.jogadorNovo_page_view, name='jogadorNovo'),
    path('comentarios', views.comentarios_page_view, name='comentarios'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('resultadosQuizz', views.resultadosQuizz_page_view, name='resultadosQuizz'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('paginas/trafford.html', views.trafford_page_view, name='trafford'),
    path('paginas/bernabeu.html', views.bernabeu_page_view, name='bernabeu'),
    path('paginas/alvalade.html', views.alvalade_page_view, name='alvalade'),
    path('paginas/figo.html', views.figo_page_view, name='figo'),
    path('paginas/zidane.html', views.zidane_page_view, name='zidane'),
    path('paginas/ronaldo.html', views.ronaldo_page_view, name='ronaldo'),
    path('paginas/ronaldinho.html', views.ronaldinho_page_view, name='ronaldinho'),
    path('paginas/sporting.html', views.sporting_page_view, name='sporting'),
    path('paginas/united.html', views.united_page_view, name='united'),
    path('paginas/madrid.html', views.madrid_page_view, name='madrid'),
    path('paginas/juventus.html', views.juventus_page_view, name='juventus'),
    path('multimedia.html', views.multimedia_page_view, name='multimedia'),
    path("sections/<int:num>", views.section, name="section"),

]
