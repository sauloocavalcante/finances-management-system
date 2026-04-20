from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are at the home index.")


def transaction(request, transaction_id):
    return HttpResponse("You're looking at transaction %s." % transaction_id)
