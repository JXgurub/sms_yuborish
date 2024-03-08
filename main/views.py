
from django.shortcuts import render,redirect
from django.http import HttpRequest
from twilio.rest import Client


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        text = request.POST['text']
        if text:
            account_sid = "AC5ab7dee9a0195f8e317e7ed7e93220b4"
            auth_token = "9a71409d4b83b25164d9a3ccb80a389e"
            client = Client(account_sid,auth_token)
            message = client.messages.create(
                body=" sizga " + name + " sms jo'natdi: " + text,
                from_ = "",
                to = ""
            )
            redirect("/")
        else:
            redirect("/")
    return render(request,"index.html",{})
