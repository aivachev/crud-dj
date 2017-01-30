from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.core.urlresolvers import reverse

app_name = 'product'

urlpatterns = [
    url('^login/$', auth_views.login, {'template_name': 'product/login_form.html'}, name='login'),
    url('^logout/$', auth_views.logout, {'next_page': '/product/index/'}, name='logout'),
    # ex:
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
	# ex:
    url(r'^index/$', views.IndexView.as_view(), name='index'),
	# ex:
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# ex:
    url(r'^base/$', views.IndexView.as_view(), name='base'),
    # ex:
    url(r'^create/$', views.DeliveryCreate.as_view(), name='create'),
    # ex:
    url(r'^(?P<pk>[0-9]+)/update/$', views.DeliveryUpdate.as_view(), name='update'),
    # ex:
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeliveryDelete.as_view(), name='delete'),
]