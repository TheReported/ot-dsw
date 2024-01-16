from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from competitors.models import Competitor
from judge.models import Judge
from teachers.models import Teacher
from votes.models import Vote


def show_main(request):
    return render(request, 'base.html', {'section': 'base'})


def dashboard(request):
    competitors = Competitor.objects.all()
    return render(
        request,
        'competitors/display_competitors.html',
        {
            'section': 'competitors',
            'competitors': competitors,
        },
    )


def search_list(request, search: str = None):
    teachers = Teacher.objects.filter(first_name__icontains=search)
    judge = Judge.objects.filter(first_name__icontains=search)
    competitors = Competitor.objects.filter(
        Q(first_name__icontains=search) | Q(music_styles__name__icontains=search)
    )

    elements = list(teachers) + list(judge)
    for element in list(competitors):
        if element not in elements:
            elements.append(element)

    return render(
        request,
        'competitors/list.html',
        {
            'section': 'competitors',
            'elements': elements,
        },
    )


def competitor_detail(request, slug):
    competitor = get_object_or_404(Competitor, slug=slug)
    return render(
        request,
        'competitors/competitor/detail.html',
        {
            'section': 'competitors',
            'competitor': competitor,
        },
    )


def competitor_nominated(request):
    nominated = Competitor.objects.filter(status=Competitor.Status.NOMINATED)
    return render(
        request, 'competitors/nominated.html', {'section': 'nominated', 'nominated': nominated}
    )


@login_required
@require_POST
def vote_competitor(request, slug):
    user_vote = Vote.objects.filter(user=request.user.id)
    competitor = get_object_or_404(Competitor, slug=slug)
    if user_vote:
        messages.error(request, 'Ya has votado')
        return redirect('competitors:nominated')
    else:
        vote = Vote(user=request.user, competitor=competitor)
        vote.save()
        messages.success(request, 'Has votado correctamente')
        return redirect('competitors:dashboard')
