from django.db import models
import uuid
from random import seed

class AccountBalance(models.Model):
    userid = models.AutoField(primary_key=True, null=False)
    fullname = models.CharField(max_length=30, null=False)
    balance = models.FloatField(null=False, default=0)

    def __str__(self):
        return self.fullname


class Statement(models.Model):
    last1 = models.FloatField(default=0)
    transaction_id_1 = models.CharField(max_length=12, unique=True)
    date1 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    last2 = models.FloatField(default=0)
    transaction_id_2 = models.CharField(max_length=12, unique=True)
    date2 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    last3 = models.FloatField(default=0)
    transaction_id_3 = models.CharField(max_length=12, unique=True)
    date3 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    last4 = models.FloatField(default=0)
    transaction_id_4 = models.CharField(max_length=12, unique=True)
    date4 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    last5 = models.FloatField(default=0)
    transaction_id_5 = models.CharField(max_length=12, unique=True)
    date5 = models.DateField(format('%Y-%m-%d'), auto_now=True)
    userid = models.ForeignKey(AccountBalance, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.userid)


def random_transaction_id():
    seed()
    transaction_id = uuid.uuid4().hex[:12].upper()
    return transaction_id


class Pending_transactions(models.Model):
    transaction_date = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=12, default=0, unique=True)
    transaction_id = models.CharField(max_length=14, default=random_transaction_id(), unique=True)
    u_id = models.IntegerField(null=False)
    pending_amount = models.FloatField(null=False)

    def __str__(self):
        return str(self.u_id)


class Pending_redeem(models.Model):
    transaction_date = models.DateTimeField(auto_now=True)
    code = models.IntegerField(default=666781, unique=True)
    transaction_id = models.CharField(max_length=14, default=uuid.uuid4().hex[:12].upper(), unique=True)
    userid = models.IntegerField(null=False)
    redeem_amount = models.FloatField(null=False)

    def __str__(self):
        return str(self.userid)
