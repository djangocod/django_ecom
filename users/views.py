
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.conf import settings
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage,send_mail
from .token import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from .models import TakeMessage
# Create your views here.


def send_email_user(user, request):
    subject = 'activate email'
    current_site = get_current_site(request)
    body = render_to_string('users/active_account.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': force_str(urlsafe_base64_encode(force_bytes(user.pk))),
        'token': generate_token.make_token(user)
    })
    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.FROM_USER_EMAIL,
        to=[user.email, ]
    )
    email.send()


def account_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            n_f = form.save(commit=False)
            n_f.username = form.cleaned_data.get('username')
            n_f.email = form.cleaned_data.get('email')
            n_f.set_password(form.cleaned_data.get('password1'))
            form.save()
            send_email_user(n_f, request)
            messages.success(request, 'Please Check Your Email Address ')
            return redirect('/')

    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def account_activte(request, uidb64, token):
    try:
        user_id = urlsafe_base64_decode(force_str(uidb64))
        user = get_user_model().objects.get(id=user_id)
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                request, 'your account has been activated successfully')
            login(request, user)
            return redirect('/')
    except:
        messages.error(request, 'please try again later')

    return render(request, 'users/errors_activate.html')


def account_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'welcom ' + user.username + ' back')
                return redirect('/')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def account_logout(request):
    logout(request)
    messages.success(request, 'You Logged out Successfully ')
    return redirect('/')


def users_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and subject and message:
            send_mail(subject, message,email,[settings.FROM_USER_EMAIL,])
            TakeMessage.objects.create(
                name=name, email=email, subject=subject, message_body=message)
            messages.success(request,'We Get Your Contact , Thank You')
            return redirect('/')

        else:
            messages.success(request, 'Sorry , Something is Going Wrong')
    return render(request,'users/contact.html')

