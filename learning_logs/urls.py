"""Arata schema URL pentru learning_logs"""

from django.urls import path
from .import views

app_name = 'learning_logs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page with list of topics
    path('topics/', views.topics, name='topics'),
    #Pagina cu informatiia la teme separate
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Pagina pentru adaugare a temei noi
    path('new_topic/', views.new_topic, name='new_topic'),
    #Pagina pentru adaugarea unei noi note
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Pagina pentru redactarea notelor
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]