from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages


# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        listing = request.POST['listing']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

    # Check if user has made that inquyry already
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.all().filter(
            listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error(
                request, 'You have already made an inquiry for that listing.')
            return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, name=name, email=email, phone=phone,
                      user_id=user_id, listing_id=listing_id, messages=message)
    contact.save()
    send_mail(
        'Property Listing Inquiry',
        'There has been an inquiry for ' + listing +
        '. Sign into the admin panel for more info.',
        'akhad0015@gmail.com',
        [realtor_email, 'akhad0015@gmail.com'],
        fail_silently=False
    )
    messages.success(
        request, 'Your request has been submitted a realtor wil get back to you soon')
    return redirect('/listings/'+listing_id)
