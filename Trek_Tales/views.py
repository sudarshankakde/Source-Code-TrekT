import email
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from updates.models import Updates, Testimonials,SiteData,Contact,BookSlot
from datetime import date, timedelta
from django.contrib import messages
import pyshorteners
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
global siteData
global linktree

siteData = SiteData.objects.first
linktree = 'https://linktr.ee/Treak_Tales'




def home(request):
    updates = Updates.objects.order_by('-tour_on_date')[0:3]
    testimonials = Testimonials.objects.order_by('-date_added')[:6]
    return render(request, 'home.html', {'updates': updates, 'Testimonials': testimonials,'sitedata':siteData})


def contact(request):
    if request.method=='POST':
        MailId = request.POST.get('email')
        Message = request.POST.get('message')
        Name = request.POST.get('name')
        contact=Contact(FullName=Name,Message=Message,Email=MailId)
        contact.save()
        subject = 'Thank you for Contacting Us'
        message = f' Dear {Name}, we have received your comment/suggestion. A member of our team will contact you shortly. Thank you for visiting Trek_tales. {linktree}'
        email_from = settings.EMAIL_HOST_USER
        recipient = [MailId,]
        send_mail( subject, message, email_from, recipient,fail_silently=True,)
        messages.success(
                request, f'Your Responce Has Saved. We will Contact You Back Soon. Thank You ')
    return render(request , 'contact.html',{'sitedata':siteData})


def cancelation(request):
    if request.method=='POST':
        TripId = request.POST.get('TripId')
        try:
            instance = get_object_or_404(BookSlot , TripId = f"{TripId}")
            tourId  = TripId[-1]
            tour = get_object_or_404(Updates, id = tourId)
            tour.slorts = tour.slorts + 1
            # email sending
            instanceEmail = instance.email
            
            subject = 'Tour cancelation.'
            message = f" Please be Informed that we have canceled your trip to {tour.Heading} with TripId {TripId}Thanks , {instance.Name} {linktree}"
            email_from = settings.EMAIL_HOST_USER
            recipient = [instanceEmail,]
            send_mail( subject, message, email_from, recipient,fail_silently=True,)
            instance.delete()
            tour.save()
            # message
            messages.success(
                    request, f'Your Tour Has Been Cancelled. With Trip id "{TripId}". Thank You.')
            return render(request,'cancelation.html',{'tripId':TripId,'done':True})
        except :
            # message
            messages.warning(
                request, f"Invalid Trip Id. Please Enter Valid Trip Id With ' - ' Symbol ")
            return render(request,'cancelation.html',{'tripId':TripId,'done':False})


        

    return render(request,'cancelation.html')