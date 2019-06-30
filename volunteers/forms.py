from .models import *
from django.forms import ModelForm

# if you from django.forms import ModelForm then in form class should inherit from ModelForm else it should be forms.ModelForm so correct that error

class VolunteerForm(forms.ModelForm):
    # class VolunteerForm(ModelForm):
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

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['volunteer',
                  'interest_name'
                  ]

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['volunteer',
                  'language_name',
                  'level_fluent'
                  ]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['volunteer',
                  'event_name',
                  'event_date',
                  'event_description'
                  ]

class OrganizationAffiliationForm(forms.ModelForm):
    class Meta:
        model = OrganizationAffiliation
        fields = ['volunteer',
                  'organization_name'
                  ]

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['volunteers',
                  'training_type',
                  'training_url',
                  'training_complete'
                    ]

class RoleForm(models.Model):
    class Meta:
        model = Role
        fields = ['trainings',
                  'volunteer',
                  'role_name'
                  ]

