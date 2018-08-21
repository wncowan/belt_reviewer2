from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^create$', views.create),
    # url(r'^create$', views.create),
    # url(r'^dashboard$', views.show),
    url(r'^login$', views.login),
    # url(r'^users/(?P<id>\d+)$', views.show),
    # url(r'^logout$', views.logout),
    # url(r'^destroy$', views.delete),
    url(r'^books/new$', views.new_book),
    url(r'^books/create$', views.create_book),
    # url(r'^dashboard/admin$', views.manage),
    # url(r'^users/new$', views.admin_new),
    # url(r'^users/create$', views.admin_create),
    # url(r'^users/edit/(?P<id>\d+)$', views.admin_edit),
    # url(r'^success$', views.success),
    # url(r'^/(?P<id>\d+)$', views.show),
    # url(r'^/(?P<id>\d+)/edit$', views.edit),
    # url(r'^/update$', views.update),
    # url(r'^courses/destroy/(?P<id>\d+)$', views.delete),
    # url(r'^courses/destroy/(?P<id>\d+)/confirm_delete$', views.confirm_delete),

]