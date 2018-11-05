from django.db import models
import string
from random import *

class AccountBalance(models.Model):
    userid = models.AutoField(primary_key=True,null=False)
    fullname = models.CharField(max_length=30,null=False)
    balance = models.FloatField(null=False,default=0)

    def __str__(self):
        return self.fullname

class Statement(models.Model):
    last1 = models.FloatField(default=0)
    date1 = models.DateField(format('%Y-%m-%d'),auto_now=True)
    last2 = models.FloatField(default=0)
    date2 = models.DateField(format('%Y-%m-%d'),auto_now=True)
    last3 = models.FloatField(default=0)
    date3 = models.DateField(format('%Y-%m-%d'),auto_now=True)
    last4 = models.FloatField(default=0)
    date4 = models.DateField(format('%Y-%m-%d'),auto_now=True)
    last5 = models.FloatField(default=0)
    date5 = models.DateField(format('%Y-%m-%d'),auto_now=True)
    userid = models.ForeignKey(AccountBalance, on_delete=models.PROTECT)
    #transaction_id = models.ForeignKey(Verify, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.userid)

def random_key():
    min_char = 16
    max_char = 20
    allchar = string.ascii_letters + string.punctuation + string.digits
    key = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return key

def random_transaction_id():
    min_char = 10
    max_char = 14
    allchar = string.ascii_letters + string.digits
    transaction_id = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return transaction_id

class Verify(models.Model):
    transaction_date = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=12,default=random_key(),unique=True)
    transaction_id = models.CharField(max_length=14,default=random_transaction_id(),unique=True)
    u_id = models.IntegerField(null=False)
    pending_amount = models.FloatField(null=False)

    def __str__(self):
        return str(self.u_id)