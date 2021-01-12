from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Skill
from profiles.models import Profile

# Create your views here.


def home_view(request):
    return render(request, 'skills/home.html', {})


def skill_view(request):
    user_id = request.user.id
    profile = Profile.objects.get(pk=user_id)
    # Profile is parent_model and child_model is Skill, fields for the child_model
    SkillFormset = inlineformset_factory(Profile, Skill, fields='__all__', extra=1, can_delete=True)
    formset = SkillFormset(request.POST or None, instance=profile)
    if formset.is_valid():
        formset.save()

        return redirect('skills:my-skills')

    qs = profile.skill_set.all()

    context = {
        'formset': formset,
        'qs': qs,
    }

    return render(request, 'skills/add.html', context)
