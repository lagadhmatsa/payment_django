from django.conf.urls import url
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name="credits.index"),
    path('statement/', views.statement, name='credits.statement'),
    path('pending_redeem/', views.pending_redeem, name="credits.pending_redeem"),
    path('pending_transactions/', views.pending_transactions, name="credits.pending_transactions"),
    path('verify_sms/', views.verify_sms, name="credits.verify_sms"),
    path('confirm/', views.confirm, name="credits.confirm"),
    url(r'^transaction_cancel/$', views.transaction_cancel, name='credits.transaction_cancel'),
    url(r'^redeem_cancel/$', views.redeem_cancel, name='credits.redeem_cancel'),
]
