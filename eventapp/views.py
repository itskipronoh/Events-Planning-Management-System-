from django.shortcuts import render,redirect
from . models import Event
from .forms import BookingForm
from datetime import datetime
from .models import Contact
from django.contrib import messages
from .models import Feedback
from django.utils.dateparse import parse_date

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def gallery(request):
    return render(request,'gallery.html')
def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request,'events.html',dict_eve)
def booking(request):
    approximate_amount = 0
    cost_per_member = 50  # cost per member
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.approximate_amount = booking.members_attending * cost_per_member
            booking.save()
            messages.success(request, f"Booking successful! Approximate amount: ${booking.approximate_amount}")
        else:
            # If the form is invalid, errors will be shown on the template.
            messages.error(request, "There was an issue with your booking. Please review the errors below.")
    else:
        form = BookingForm()

    if request.method == 'GET' and 'members_attending' in request.GET:
        try:
            members_attending = int(request.GET.get('members_attending'))
            approximate_amount = members_attending * cost_per_member
        except (ValueError, TypeError):
            approximate_amount = 0

    dict_form = {
        'form': form,
        'approximate_amount': approximate_amount
    }
    return render(request, 'booking.html', dict_form)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def feedback_view(request):
    if request.method == 'POST':
        event_name = request.POST.get('eventName')
        date = parse_date(request.POST.get('date'))
        platform = request.POST.get('platform')
        overall_experience = int(request.POST.get('overallExperience'))
        enjoyed_most = request.POST.get('enjoyedMost')

        feedback = Feedback(
            event_name=event_name,
            date=date,
            platform=platform,
            overall_experience=overall_experience,
            enjoyed_most=enjoyed_most
        )
        feedback.save()
        messages.success(request, 'Thank you for your feedback!')
        # return redirect('/') 

    return render(request, 'feedback.html')