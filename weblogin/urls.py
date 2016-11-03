from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.indexHtml, name='indexHtml'),
    url(r'^index/$', views.indexHtml, name='indexHtml'),
    url(r'^register/$', views.registerHtml, name='registerHtml'),
    url(r'^registerHandler/$', views.registerHandler, name='registerHands'),
    url(r'^login/$', views.loginHtml, name='loginHtml'),
    url(r'^loginHandler/$', views.loginHandler, name='loginHandler'),
    # url(r'^loginSucceed/$', views.loginSucceed, name='loginSucceed'),
    url(r'^loginOut/$', views.loginOut, name='loginOut'),
    url(r'^cart/$', views.cart, name='cart'),
]
