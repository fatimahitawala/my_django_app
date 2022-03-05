from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def monthly_challenges_num(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    challenge_text = None
    if month == "Jan":
        challenge_text = "this is jan"
    elif month == "Feb":
        challenge_text = "this is text"
    
    elif month == "march":
        challenge_text = "this is text is march"
    else:
        return HttpResponseNotFound("404 forbiddon")
    return HttpResponse(challenge_text)