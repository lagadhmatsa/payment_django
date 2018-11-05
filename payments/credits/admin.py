from django.contrib import admin

from django.contrib import admin
from .models import  AccountBalance,Statement,Verify

admin.site.register(AccountBalance)
admin.site.register(Statement)
admin.site.register(Verify)
# Register your models here.
