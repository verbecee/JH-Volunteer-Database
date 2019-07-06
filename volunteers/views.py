from django.shortcuts import render, redirect
from .models import Volunteer, Interest, Language, Event, OrganizationAffiliation, Training, Role, VolEmgtCtct
from .forms import VolunteerForm, VolEmgtCtctForm, InterestForm, LanguageForm, EventForm, OrganizationAffiliationForm, TrainingForm, RoleForm

# Create your views here.


def index(request):
    return render(request, 'volunteers/index.html')


def vol_application(request):
    if request.method == "POST":
        vol_form = VolunteerForm(request.POST)
        VolEmgtContact_form = VolEmgtCtctForm(request.POST)
        interest_form = InterestForm(request.POST)
        lang_form = LanguageForm(request.POST)
        event_form = EventForm(request.POST)
        org_assocition = OrganizationAffiliationForm(request.POST)
        traing_form = TrainingForm(request.POST)
        role_form = RoleForm(request.POST)

        if vol_form.is_valid():
            vol_form.save()
        if VolEmgtContact_form.is_valid():
            VolEmgtContact_form.save()
        if interest_form.is_valid():
            interest_form.save()
        if lang_form.is_valid():
            lang_form.save()
        if event_form.is_valid():
            event_form.save()
        if org_assocition.is_valid():
            org_assocition.save()
        if traing_form.is_valid():
            traing_form.save()
        if role_form.is_valid():
            role_form.save()

    vol_form = VolunteerForm()
    VolEmgtContact_form = VolEmgtCtctForm()
    interest_form = InterestForm()
    lang_form = LanguageForm()
    event_form = EventForm()
    org_assocition = OrganizationAffiliationForm()
    traing_form = TrainingForm()
    role_form = RoleForm()
    context = {
        'volunteer_form': vol_form,
        'VolEContact_form': VolEmgtContact_form,
        'interest_form': interest_form,
        'lang_form': lang_form,
        'event_form': event_form,
        'org_assocition': org_assocition,
        'traing_form': traing_form,
        'role_form': role_form

    }

    return render(request, 'volunteers/forms_volunteer.html', context)
