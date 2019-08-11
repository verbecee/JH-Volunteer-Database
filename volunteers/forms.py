from .models import Volunteer, Interest, Language, Event, OrganizationAffiliation, Training, Role, VolEmgtCtct
from django import forms

# comments from Josh
# Drop down of the calendar for birth days


class VolunteerForm(forms.ModelForm):
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    middle_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    gender = forms.ChoiceField(
        choices=(
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Other")
        ),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    YEARS = [x for x in range(1950, 2002)]
    birth_date = forms.DateField(
        widget=forms.SelectDateWidget(
            years=YEARS,
            attrs={
                'class': 'form-control',
                'placeholder': "Month Day Year"
            }
        )
    )
    # for birth dates, i would go with DateField
    physical_limitations = forms.ChoiceField(
        choices=(
                ("Y", "Yes"),
                ("N", "No")
        ),
        widget=forms.RadioSelect(
            attrs={
                'class': 'radio'
            }
        )
    )
    physical_explanation = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
    street_address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )

    )
    state = forms.CharField(
        max_length=2,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    zip_code = forms.CharField(
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    phone = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        max_length=40,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    cross_cultural_experiences = forms.CharField(
        max_length=600,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
    why_FDPs = forms.CharField(
        label='Why FDPS',
        max_length=600,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
    spirituality = forms.CharField(
        max_length=600,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    notes = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

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
                  'notes',
                  'cross_cultural_experiences',
                  'why_FDPs',
                  'spirituality'
                  ]


class VolEmgtCtctForm(forms.ModelForm):
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )

    )

    email = forms.EmailField(
        max_length=40,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = VolEmgtCtct
        fields = ['volunteer',
                  'last_name',
                  'first_name',
                  'email',
                  'phone',
                  'address'
                  ]


class InterestForm(forms.ModelForm):
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )

    )
    interest_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Interest
        fields = ['volunteer',
                  'interest_name'
                  ]


class LanguageForm(forms.ModelForm):
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )

    )
    language_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )

    )
    level_fluent = forms.ChoiceField(
        choices=(
            ("mother_tongue", "Native Speak"),
            ("near_native", "Fluent"),
            ("exclt_command", "Highly proficient in spoken and written"),
            ('good_command', 'Good working knowledge'),
            ('working_knowledge', 'basic communication skills')
        ),
        widget=forms.RadioSelect(
            attrs={
                "class": "radio"
            }
        )
    )

    class Meta:
        model = Language
        fields = ['volunteer',
                  'language_name',
                  'level_fluent'
                  ]


class EventForm(forms.ModelForm):
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    event_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    event_date = forms.DateTimeField(
        widget=forms.SelectDateWidget(
            attrs={
                "class": "form-control"
            }
        )
    )
    event_description = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Event
        fields = ['volunteer',
                  'event_name',
                  'event_date',
                  'event_description'
                  ]


class OrganizationAffiliationForm(forms.ModelForm):
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )

    )
    organization_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = OrganizationAffiliation
        fields = ['volunteer',
                  'organization_name'
                  ]


class TrainingForm(forms.ModelForm):
    volunteers = forms.ModelMultipleChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control"
            }
        )

    )
    training_name = forms.CharField(
        max_length=130,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    training_type = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    training_url = forms.URLField(
        max_length=1000,
        widget=forms.URLInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    training_complete = forms.BooleanField(
        label="Tick if training completed"
    )

    class Meta:
        model = Training
        fields = ['volunteers',
                  'training_name',
                  'training_type',
                  'training_url',
                  'training_complete'
                  ]


class RoleForm(forms.ModelForm):
    trainings = forms.ModelMultipleChoiceField(
        queryset=Training.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control"
            }
        )
    )
    volunteer = forms.ModelChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )
    role_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = Role
        fields = ['volunteer',
                  'trainings',
                  'role_name'
                  ]
