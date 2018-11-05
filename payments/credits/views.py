from django.shortcuts import render
from django.http import HttpResponse
from .models import AccountBalance, Statement, Verify
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    balances = AccountBalance.objects.filter(userid=4)
    print(balances)
    balance = {'bal': balances}
    return render(request, 'credits/index.html', context=balance)


def statement(request):
    transaction = Statement.objects.filter(userid__fullname="Lagadh")
    transaction_disp = {'trans': transaction}
    return render(request, 'credits/statement.html', context=transaction_disp)


def redeem(request):
    redeem_amount = request.POST['redeem_amount']
    temp = AccountBalance.objects.filter(fullname="Lagadh")

    for y in temp:
        y1 = float(y.balance) - float(redeem_amount)
        if y1 < 0:
            return HttpResponse("Insufficient credits")
    user_bal_update = AccountBalance.objects.filter(fullname="Lagadh").update(balance=y1)
    temp1 = AccountBalance.objects.filter(fullname="admin")
    for x in temp1:
       x1 = float(x.balance) + float(redeem_amount)
    admin_remmit = AccountBalance.objects.filter(fullname="admin").update(balance=x1)
    temp2 = Statement.objects.filter(userid=4)
    for z in temp2:
        z1 = float(z.last1)
        z2 = float(z.last2)
        z3 = float(z.last3)
        z4 = float(z.last4)
        z5 = float(z.last5)
    statement_update = Statement.objects.filter(userid__fullname="Lagadh").update(last5=z4,last4=z3,last3=z2,last2=z1,last1=redeem_amount)
    return HttpResponse("Amount redeemed {} and Credits remaining {}".format(redeem_amount,y1))

def verify(request):
    add_amount = request.POST['add_amount']

    temp = Verify.objects.create(u_id=1,pending_amount=add_amount)
    temp1 = Verify.objects.get(u_id=1)
    subject = 'Payment confirmation'
    message = ('Please use this key for confirmation {}'.format(temp1.key))
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['lagadhkumar.m17@iiits.in',]
    send_mail( subject, message, email_from, recipient_list)
    return render(request, 'credits/pending_pay.html')

def confirm(request):
    pay_key = request.POST['pay_key']
    temp1 = Verify.objects.get(u_id=1)
    html = "You have entered incorrect key" + '<a href="/credits">Click here to go back</a>'
    if pay_key == temp1.key:
        return HttpResponse("You have successfully added credits into your account")
    else:
        return HttpResponse(html)