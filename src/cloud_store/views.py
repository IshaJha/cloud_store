from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .forms import contactForm



def index_home(request):
    context={
        "page":"Index"
    }
    return render(request,'home_page.html', context)

def contactPage(request):
    if request.method == 'GET': 
        print("IN GET")
        form = contactForm(request.POST or None)
        context = {
            "context":"Contact Form",
            "form":form,
        }

    if request.method == 'POST':
        print("IN POST")
        form = contactForm(request.POST or None)
        
        if form.is_valid():
            fullname =form.cleaned_data['fullname']
            email =form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message =form.cleaned_data['message']
            email_from = settings.EMAIL_HOST_USER

            recipient_list = ['ishaj2210@gmail.com']
            
            content = "Message form: "+fullname+"\n"+ "Email: " +email+"\n"+ message

            send_mail(subject, content,email_from, recipient_list)



        context = {
            "context":"Contact Form",
            "fullname":fullname,
            "email":email,
            "content":content,
        }

            # print(request.POST.get('fullname'))
            # print(request.POST.get())
       
    # return render(request,"contact_page.html", context)
    return render(request,'contact.html', context)