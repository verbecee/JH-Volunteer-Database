from .models import *
from django.forms import ModelForm

class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['last_name',
                  'first_name',
                  'middle_name',
                  'gender',
                  'birth_date',
                  'physical_limitations',
                  'physical_explanation',
                  'street_address',
                  'state',
                  'zip_code',
                  'phone',
                  'email',
                  'emergency_last_name',
                  'emergency_first_name',
                  'emergency_address',
                  'emergency_phone',
                  'notes',
                  'cross_cultural_experiences',
                  'why_FDPs',
                  'spirituality'
                  ]

class InterestForm(ModelForm):
    class Meta:
        model = Interest
        fields = ['interest_name'
                  ]

    # class Author(models.Model):
    #     name = models.CharField(max_length=100)
    #     title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    #     birth_date = models.DateField(blank=True, null=True)
    #
    #     def __str__(self):
    #         return self.name
    #
    # class Book(models.Model):
    #     name = models.CharField(max_length=100)
    #     authors = models.ManyToManyField(Author)
    #
    # class AuthorForm(ModelForm):
    #     class Meta:
    #         model = Author
    #         fields = ['name', 'title', 'birth_date']
    #
    # class BookForm(ModelForm):
    #     class Meta:
    #         model = Book
    #         fields = ['name', 'authors']