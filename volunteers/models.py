from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Volunteer(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    gender = models.CharField(
        max_length=2,
        choices=(
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Others")
        )
    )
    birth_date = models.DateField(blank=True, null=True)
    # for birth dates, i would go with DateField
    physical_limitations = models.CharField(
        max_length=5,
        choices=(
                ("Y", "Yes"),
                ("N", "No")
        )
    )
    physical_explanation = models.TextField(blank=True, null=True)
    street_address = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=40)
    notes = models.CharField(max_length=600)
    cross_cultural_experiences = models.CharField(max_length=600)
    why_FDPs = models.CharField(max_length=600)
    spirituality = models.CharField(max_length=600)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class VolEmgtCtct(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    e_last_name = models.CharField(max_length=30)
    e_first_name = models.CharField(max_length=30)
    e_address = models.CharField(max_length=50)
    e_email = models.EmailField()
    e_phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.e_last_name} {self.e_first_name} is {self.volunteer}'s contact"


class Interest(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    interest_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.interest_name}"


class Language(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=30)
    level_fluent = models.CharField(
        max_length=30,
        choices=(
            ("mother_tongue", "Native Speak"),
            ("near_native", "Fluent"),
            ("exclt_command", "Highly proficient in spoken and written"),
            ('good_command', 'Good working knowledge'),
            ('working_knowledge', 'basic communication skills')
        )

    )

    def __str__(self):
        return f"{self.language_name}"


class Event(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField('Event date')
    event_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.event_name}"


class OrganizationAffiliation(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.organization_name}"


class Training(models.Model):
    volunteers = models.ManyToManyField(Volunteer)
    training_name = models.CharField(
        max_length=130)
    training_type = models.CharField(
        max_length=30)
    training_url = models.CharField(
        max_length=1000)
    training_complete = models.BooleanField()

    def __str__(self):
        return f"{self.training_name} is completed?...:{self.training_complete}"

class Role(models.Model):
    trainings = models.ManyToManyField(Training)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.role_name}"
