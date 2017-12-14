from django.shortcuts import render
from django.shortcuts import  redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'cetcarweb/base.html')