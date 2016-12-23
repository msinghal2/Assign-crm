from django.conf.urls import url
from . import views

app_name = 'assign'

urlpatterns = [
    # /assign/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/assign/<empid>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /assign/employee/add/
    url(r'^employee/add/$', views.EmpCreate.as_view(), name='emp-add'),

    # /assign/employee/2/
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmpUpdate.as_view(), name='emp-update'),

    # /assign/employee/2/delete
    url(r'^employee/(?P<pk>[0-9]+)/delete/$', views.EmpDelete.as_view(), name='emp-delete'),

#FOR ASSIGNMENTS

    # /assign/assignment/
    url(r'^assignment/$', views.AssignIndexView.as_view(), name='assignindex'),

    #/assign/assignment/<assignid>/
    url(r'^assignment/(?P<pk>[0-9]+)/$', views.AssignDetailView.as_view(), name='assigndetail'),

    # /assign/assignment/add/
    url(r'^assignment/add/$', views.AssignCreate.as_view(), name='assignadd'),

    #/assign/assignment/delete/<assignid>/
    url(r'^assignment/delete/(?P<pk>[0-9]+)/$', views.AssignDelete.as_view(), name='assigndelete'),

    # /assign/assignment/update/2/
    url(r'^assignment/update/(?P<pk>[0-9]+)/$', views.AssignUpdate.as_view(), name='assignupdate'),

#FOR DELEGATIONS

    # /assign/delegation/
    url(r'^delegation/$', views.DelegIndexView.as_view(), name='delegindex'),

    # /assign/delegation/<delegid>/
    url(r'^delegation/(?P<pk>[0-9]+)/$', views.DelegDetailView.as_view(), name='delegdetail'),

    # /assign/delegation/add/
    url(r'^delegation/add/$', views.DelegCreate.as_view(), name='delegadd'),

    # /assign/delegation/delete/<delegid>
    url(r'^delegation/delete/(?P<pk>[0-9]+)/$', views.DelegDelete.as_view(), name='delegdelete'),

    # /assign/delegation/update/2/
    url(r'^delegation/update/(?P<pk>[0-9]+)/$', views.DelegUpdate.as_view(), name='delegupdate'),

]