from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import MyUser, Register
import json, datetime
from django.views.decorators.csrf import csrf_exempt
import paypalrestsdk

paypalrestsdk.configure({
    "mode": "sandbox",  # sandbox or live
    "client_id": "AXr4E2lLxbOZenekDKpiPcTzdBT_QqQfbAl2rQXS-7fUtQfrwIDh-BL3RnFbDT7N8uBETEkkLb9ZjmD8",
    "client_secret": "EHUCAop_rMCQ4rUFw1Z93mnAcp3gpahnArG7JXthwhTj6g-4Oqq7nRbGcd6TSb3_ODy_SdUdL1RTCZB3"})


# Create your views here.
def index(request):
    return render(request, 'index.html')


def mobile(request):
    return render(request, 'mobile.html')


def talk(request):
    return render(request, 'talk_index.html')


def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = MyUser.objects.filter(username=username)
        password = MyUser.objects.filter(password=password)

        if int(username) == 1:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')


def explore(request):
    return render(request, 'explore.html')


def listing(request):
    return render(request, 'listing.html')


def single_listing(request):
    return render(request, 'single-listing.html')


# def register(request):
#     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        birth = datetime.datetime.strptime(request.POST['birth'], '%Y-%m-%d')
        email = request.POST['email']
        phone = request.POST['phone']
        nation = request.POST['nation']
        existUsername = MyUser.objects.filter(username=username).count()

        if int(existUsername) > 0:
            return JsonResponse({'status': 400, 'message': 'failed', 'data': "user is here！"})
        else:
            createUser = MyUser(username=username, password=password, birth=birth, email=email, phone=phone,
                                nation=nation)  # birth=birth,
            createUser.save()
            registerUser = Register(username=username, password=password, birth=birth, email=email, phone=phone,
                                    nation=nation)  # birth=birth,
            registerUser.save()
            return JsonResponse({'status': 200, 'message': 'success', 'data': "user created！"})

    return render(request, 'register.html')


def register_api(request):
    result = {'message': ''}
    if request.POST:
        if MyUser.objects.filter(username=request.POST['username']):
            result['message'] += '用戶名重複；'
        if MyUser.objects.filter(email=request.POST['email']):
            result['message'] += 'email重複；'
        if MyUser.objects.filter(phone=request.POST['phone']):
            result['message'] += '電話號碼重複'

        # return HttpResponse(json.dumps(result), content_type="application/json")
        return JsonResponse(result)

    return HttpResponse('')


@csrf_exempt
def pay(request):
    if request.method == 'POST':
        paymoney = request.POST.get('money')
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"},
            "redirect_urls": {
                "return_url": "http://localhost:3000/payment/execute",
                "cancel_url": "http://localhost:3000/"},
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "item",
                        "sku": "item",
                        "price": float(paymoney),
                        "currency": "HKD",
                        "quantity": 1}]},
                "amount": {
                    "total": float(paymoney),
                    "currency": "HKD"},
                "description": "This is the payment transaction description."}]})

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    # Convert to str to avoid Google App Engine Unicode issue
                    # https://github.com/paypal/rest-api-sdk-python/pull/58
                    approval_url = str(link.href)
                    print("Redirect for approval: %s" % (approval_url))
                    return JsonResponse({'status': 200, 'message': 'success', 'data2': approval_url})
        else:
            return JsonResponse({'status': 206, 'message': 'success', 'data2': "Payment created failed！"})


payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": "0.01",
                "currency": "HKD",
                "quantity": 1}]},
        "amount": {
            "total": "0.01",
            "currency": "HKD"},
        "description": "This is the payment transaction description."}]})

if payment.create():
    print("Payment created successfully")
else:
    print(payment.error)
