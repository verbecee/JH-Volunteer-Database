from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ModelForm
# Create your models here.

class Volunteer(models.Model):
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(1, "Please enter a valid name.")])
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(1, "Please enter a valid name.")])
    middle_name = models.CharField(max_length=30)
    gender = models.IntegerField
    birth_date = models.DateTimeField('Date of birth')
    physical_limitations = models.IntegerField(default=0)
    physical_explanation = models.CharField(max_length=200)
    street_address = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Please enter a valid address.")])
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2, "Please enter a valid state abbreviation.")])
    zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5, "Please enter a valid zipcode.")])
    phone = models.CharField(max_length=12, validators=[MinLengthValidator(7, "Please enter a valid phone number (xxx-xxx-xxxx).")])
    email = models.CharField(max_length=40, validators=[MinLengthValidator(4, "Please enter a valid email.")])
    emergency_last_name = models.CharField(max_length=30)
    emergency_first_name = models.CharField(max_length=30)
    emergency_address = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=12, validators=[MinLengthValidator(7, "Please enter a valid phone number (xxx-xxx-xxxx).")])
    notes = models.CharField(max_length=600)
    cross_cultural_experiences = models.CharField(max_length=600)
    why_FDPs = models.CharField(max_length=600)
    spirituality = models.CharField(max_length=600)

class Interest(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    interest_name = models.CharField(max_length=50)

class Language(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=30)
    level_fluent = models.IntegerField(default=0)

class Event(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, validators=[MinLengthValidator(1, "Please enter a valid event name.")])
    event_date = models.DateTimeField('Event date')
    event_description = models.CharField(max_length=200)

class OrganizationAffiliation(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=50, validators=[MinLengthValidator(1, "Please enter a valid organization name.")])

class Training(models.Model):
    volunteers = models.ManyToManyField(Volunteer)
    training_type = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    training_url = models.CharField(max_length=1000, validators=[MinLengthValidator(1)])
    training_complete = models.IntegerField(default=0)

class Role(models.Model):
    trainings = models.ManyToManyField(Training)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=30, validators=[MinLengthValidator(1)])