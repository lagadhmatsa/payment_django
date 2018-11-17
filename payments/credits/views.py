from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AccountBalance, Statement, Pending_transactions, Pending_redeem
from django.core.mail import send_mail
from django.conf import settings
from random import *
import uuid
import string
from datetime import datetime
from twilio.rest import Client
from django.utils.crypto import get_random_string

try:
    import httplib

except:
    import http.client as httplib


def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def index(request):
    balances = AccountBalance.objects.filter(userid=1)
    print(balances)
    balance = {'bal': balances}
    return render(request, 'credits/index.html', context=balance)


def statement(request):
    transaction = Statement.objects.filter(userid=1)
    transaction_disp = {'trans': transaction}
    return render(request, 'credits/statement.html', context=transaction_disp)


def pending_redeem(request):
    redeem_amount = request.POST['redeem_amount']
    code = get_random_string(length=6, allowed_chars='1234567890')
    if have_internet():
        temp = Pending_redeem.objects.create(userid=1, redeem_amount=redeem_amount,transaction_id=uuid.uuid4().hex[:12].upper(), code=int(code))
        auth_token = "Twilio account auth token"
        account_sid = "Twilio account SSID"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
             to="Twilio registered mobile number",
             from_="Twilio alloted mobile number",
             body="Use {} code for verification.Amount requested to redeem is {}".format(code, redeem_amount))
    else:
        return HttpResponse("Internet not available.Please check your connection" + '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};</script><a href="/credits">Click here to go to home page</a></head></html>')
    return render(request, 'credits/pending_redeem.html')



def verify_sms(request):
    code = int(request.POST['code'])
    temp1 = Pending_redeem.objects.get(userid=1)
    # print("Hello")
    # print(temp1.code, code)
    redeem_amount = temp1.redeem_amount
    temp2 = Statement.objects.get(userid=1)
    z1 = float(temp2.last1)
    z2 = float(temp2.last2)
    z3 = float(temp2.last3)
    z4 = float(temp2.last4)
    z5 = float(temp2.last5)
    key_err_page = "You have entered incorrect key" + '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};</script><a href="/credits">Click here to go to home page</a></head></html>'
    key_success_page = "You have successfully redeemed {} credits from your account".format(redeem_amount) + '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};</script><a href="/credits">Click here to go to home page</a></head></html>'
    if code == temp1.code:
        temp = AccountBalance.objects.get(userid=1)
        y1 = float(temp.balance) - float(redeem_amount)
        if y1<0:
            return HttpResponse("Insufficient credits")
        else:
            user_bal_update = AccountBalance.objects.filter(userid=1).update(balance=y1)
            statement_update = Statement.objects.filter(userid=1).update(transaction_id_5=temp2.transaction_id_4, transaction_id_4=temp2.transaction_id_3, transaction_id_3=temp2.transaction_id_2, transaction_id_2=temp2.transaction_id_1, transaction_id_1=temp1.transaction_id, last5=z4, last4=z3, last3=z2, last2=z1, last1=redeem_amount, date5=temp2.date4, date4=temp2.date3, date3=temp2.date2, date2=temp2.date1, date1=datetime.now())
            temp1.delete()
            return HttpResponse(key_success_page)
    else:
        temp1.delete()
        return HttpResponse(key_err_page)


def random_key():
    seed()
    key = uuid.uuid4().hex[:8]
    return key

def pending_transactions(request):
    add_amount = request.POST['add_amount']
    key = random_key()
    if have_internet():
        temp = Pending_transactions.objects.create(u_id=1, pending_amount=add_amount, key=key)
        subject = 'Payment confirmation'
        message = ('Please use this key for confirmation {}'.format(key))
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['Recipient email',]
        send_mail( subject, message, email_from, recipient_list)
    else:
        return HttpResponse("Internet not available.Please check your connection" + '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};</script><a href="/credits">Click here to go to home page</a></head></html>')
    return render(request, 'credits/pending_pay.html')


def confirm(request):
    pay_key = request.POST['pay_key']
    temp1 = Pending_transactions.objects.get(u_id=1)
    add_amount = temp1.pending_amount
    temp2 = Statement.objects.get(userid=1)
    z1 = float(temp2.last1)
    z2 = float(temp2.last2)
    z3 = float(temp2.last3)
    z4 = float(temp2.last4)
    z5 = float(temp2.last5)
    key_err_page = "You have entered incorrect key" + '<a href="/credits">Click here to go back</a>'
    key_success_page = "You have successfully added credits into your account" + '<html><head><script>history.pushState(null, null, location.href);window.onpopstate = function () {history.go(1);};</script><a href="/credits">Click here to go to home page</a></head></html>'
    if pay_key == temp1.key:
        temp = AccountBalance.objects.get(userid=1)
        y1 = float(temp.balance) + float(add_amount)
        user_bal_update = AccountBalance.objects.filter(userid=1).update(balance=y1)
        statement_update = Statement.objects.filter(userid=1).update(transaction_id_5=temp2.transaction_id_4,transaction_id_4=temp2.transaction_id_3,transaction_id_3=temp2.transaction_id_2,transaction_id_2=temp2.transaction_id_1,transaction_id_1=temp1.transaction_id,last5=z4, last4=z3, last3=z2,last2=z1, last1=add_amount,date5=temp2.date4,date4=temp2.date3,date3=temp2.date2,date2=temp2.date1,date1=datetime.now())
        temp1.delete()
        return HttpResponse(key_success_page)
    else:

        temp1.delete()
        return HttpResponse(key_err_page)


def transaction_cancel(request):
    temp = Pending_transactions.objects.get(u_id=1)
    temp.delete()
    return redirect('/credits')


def redeem_cancel(request):
    temp = Pending_redeem.objects.get(userid=1)
    temp.delete()
    return redirect('/credits')
