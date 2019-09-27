import datetime
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import get_template
from django.http import Http404
from django.template.response import TemplateResponse
from django.template import TemplateDoesNotExist
from django.core.mail import send_mail
from .forms import ContactForm


def about(request):
    return TemplateResponse(request, "custompages/about.html", {})


def technology(request):
    return TemplateResponse(request, "custompages/technology.html", {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Contact Request: ' + form.cleaned_data['name']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            sender = 'server@pysolution.com'
            phone = form.cleaned_data['phone']
            message = ('Client Name: ' + name + '\n\n Phone: ' + phone +
                       '\n\n Email: ' + email + '\n\n Subject: ' + subject +
                       '\n\nMessage:\n ' + form.cleaned_data['message'] +
                       '\n\nMessage sent from contact page')
            recipients = ['info@pysolution.com']
            send_mail(subject, message, sender, recipients)
            submit_time = datetime.datetime.now()
            message = form.cleaned_data['message']
            return redirect("/thank-you/")
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return TemplateResponse(request, "custompages/contact.html", context)


def site_demos(request):
    return TemplateResponse(request, "custompages/site_demos.html", {})


def thank_you(request):
    return TemplateResponse(request, "custompages/thank_you.html", {})


def money_back_guarantee(request):
    return TemplateResponse(request, "custompages/money_back_guarantee.html", {})


def pyrealtor_detail(request, slug):
    template = "custompages/pyrealtor/" + slug + ".html"
    context = {
        'slug': slug,
    }
    print(template)
    try:
        get_template(template)
        return TemplateResponse(request, template, context)
    except TemplateDoesNotExist:
        raise Http404


def pyrealtor_details(request):
    return TemplateResponse(request, "custompages/pyrealtor.html", {'fluid': True, 'fontawesome': True, 'hidenav': True})