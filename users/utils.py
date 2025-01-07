from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse


def send_email_confirmation(user, request):
    token = default_token_generator.make_token(user)
    uid = user.pk
    current_site = get_current_site(request)
    confirmation_link = request.build_absolute_uri(
        reverse('users:email_confirm', kwargs={'uid': uid, 'token': token})
    )

    subject = "Confirm Your Email Address"
    message = render_to_string('email_confirmation.html', {
        'user': user,
        'confirmation_link': confirmation_link,
    })

    send_mail(subject, message, 'no-reply@example.com', [user.email])
