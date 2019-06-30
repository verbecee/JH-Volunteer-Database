from django.shortcuts import render
from .models import Volunteer, Interest, Language, Event, OrganizationAffiliation, Training, Role
from .forms import VolunteerForm, InterestForm, LanguageForm, EventForm, OrganizationAffiliationForm, TrainingForm, RoleForm

# Create your views here.


def vol_application(request):
    voluntee_form = VolunteerForm()
    interest_form = InterestForm()
    lang_form = LanguageForm()
    event_form = EventForm()
    org_assocition = OrganizationAffiliationForm()
    traing_form = TrainingForm()
    role_form = RoleForm()

    context = {
        "volunteer_form": voluntee_form,
        'interest_form': interest_form,
        'lang_form': lang_form,
        'event_form': event_form,
        'org_assocition': org_assocition,
        'traing_form': traing_form,
        'role_form': role_form

    }
    return render(request, 'volunteers/forms_volunteer.html', context)
