from django.shortcuts import redirect, reverse, get_object_or_404, render_to_response, render
from django.http.response import HttpResponseRedirect
from .forms import MailForm
from .models import Product, Mail

def landing(request):
    choices = []
    for item in Product.objects.all():
        choices.append((item.id, item.name))

    mail_form = MailForm(choices)

    if request.method == "POST" :
        data = request.POST or None
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        message = data.get('message')
        product = Product.objects.get(id=data.get('product'))
        mail = Mail(name=name, phone=phone, email=email, message=message, product=product)
        print(mail)
        mail.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'landing/landing.html', locals())



