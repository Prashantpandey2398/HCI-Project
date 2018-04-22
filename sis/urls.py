from sis import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^home',views.home1,name='home1'),
    url(r'^marks',views.marks,name='marks'),
    url(r'^dac',views.dac,name='dac'),
    url(r'^feedback',views.feedback,name='feedback'),
    url(r'^news',views.news,name='news'),
    url(r'^login',views.afterlogin,name='afterlogin'),
]