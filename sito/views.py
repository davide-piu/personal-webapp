import mimetypes
import os
from wsgiref.util import FileWrapper
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Articolo
from django.core.mail import send_mail
from django.http import FileResponse


# Create your views here.


def index(request):
        if request.method == "POST":
            message_name = request.POST['message-name']
            message = request.POST['message']
            message_email = request.POST['message-email']
            send_mail(
                message_name,
                message,
                message_email,  # from email
                ['example@email.com'],  # to email
            )

            return render(request, 'sito/index.html', {'message_name': "Grazie del messaggio " + message_name+"!"})
        else:
            return render(request, 'sito/index.html', {})



