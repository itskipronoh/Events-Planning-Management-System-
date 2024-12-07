from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    cus_name = models.CharField(max_length=55)
    cus_ph = models.CharField(max_length=12)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
    members_attending = models.PositiveIntegerField(default=1)
    approximate_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.cus_name} - {self.name.name}"


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    platform = models.CharField(max_length=255)
    overall_experience = models.IntegerField(choices=[
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent')
    ])
    enjoyed_most = models.TextField()

    def __str__(self):
        return f"Feedback for {self.event_name} on {self.date}"
