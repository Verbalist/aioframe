from urls import url
import views.{PATH}

urlpatterns = [url('GET',r'/{PATH}', views.{PATH}.main),
               url('GET',r'/{PATH}update/{id}', views.{PATH}.update),
               url('GET',r'/{PATH}create/', views.{PATH}.create),
               url('GET',r'/{PATH}delete/{id}', views.{PATH}.delete),
               url('GET',r'/{PATH}show/{id}', views.{PATH}.show)]