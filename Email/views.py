from django.shortcuts import render,redirect
from django.template.loader import  get_template
from django.core.mail import EmailMultiAlternatives
from Main.settings import EMAIL_HOST_USER

# Create your views here.
def sendMail(request, username, email_to):
	try:
		ctx = {
			'user':username,
		}
		message = get_template('mail.html').render(ctx)
		msg = EmailMultiAlternatives(
				'subject',
				message,
				EMAIL_HOST_USER,
				[email_to],
			)

		msg.attach_alternative(message, "text/html")
		msg.send()
		print('Email Sent') 
	except:
		print('Something Went Wrong')

		

	

def index(request):
	if request.method == "POST":
		username = request.POST.get('username')
		email_to = request.POST.get('email')

		sendMail(request ,username, email_to)
	return render(request, 'index.html')