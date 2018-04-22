from sis import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^home',views.home1,name='home1'),
]