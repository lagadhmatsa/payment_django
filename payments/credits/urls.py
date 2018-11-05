from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name="credits.index"),
    path('statement/', views.statement,name='credits.statement'),
    path('redeem/', views.redeem,name="credits.redeem"),
    path('verify/', views.verify,name="credits.verify"),
    path('confirm/', views.confirm, name="credits.confirm"),
]