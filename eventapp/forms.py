from django import forms
from .models import Booking
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput(),
        }

        labels = {
            'cus_name': "Customer Name:",
            'cus_ph': "Customer Phone:",
            'name': "Event Name:",
            'booking_date': "Booking Date:",
            'members_attending': "Number of Members Attending:",
            'approximate_amount': "Approximate Amount:",  
        }
    
    approximate_amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  
            self.fields['approximate_amount'].initial = self.instance.members_attending * 50  
        else: 
            self.fields['approximate_amount'].initial = 0

    def clean(self):
        cleaned_data = super().clean()
        event = cleaned_data.get('name')
        booking_date = cleaned_data.get('booking_date')

        if event and booking_date:
            # Check if there's already a booking for the same event and date
            existing_booking = Booking.objects.filter(name=event, booking_date=booking_date).exclude(pk=self.instance.pk)
            if existing_booking.exists():
                raise ValidationError(f"The event '{event.name}' is already booked for the selected date.")

        return cleaned_data
