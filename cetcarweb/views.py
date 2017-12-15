from django.shortcuts import render
from django.shortcuts import  redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from .forms import Contact
# Create your views here.
def inicio(request):
	request.session['page']='home'
	return render(request,'cetcarweb/index.html')

def somos(request):
	request.session['page']='somos'
	return render(request,'cetcarweb/about.html')

def servicios(request):
	request.session['page']='servicios'
	return render(request,'cetcarweb/services.html')

def cursos(request):
	request.session['page']='cursos'
	return render(request,'cetcarweb/courses.html')

def contacto(request):
	request.session['page']='contact'
	if request.method=='POST':
		form=Contact(request.POST)
		if form.is_valid():
			Mensaje=('%s\n%s\n%s\n%s\n%s' % (form.cleaned_data['nombre'],
										form.cleaned_data['ciudad'],
										form.cleaned_data['email'],
										form.cleaned_data['empresa'],
										form.cleaned_data['mensaje']))
			send_mail(
		    form.cleaned_data['asunto'],
		    Mensaje,
		    'alexacaro14@gmail.com',
		    ['german0917@gmail.com'],
		    fail_silently=False,)
			return HttpResponse(Mensaje)
	form=Contact()
	return render(request,'cetcarweb/contact.html',{'form':form})
