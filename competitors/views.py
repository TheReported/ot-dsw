from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render

from competitors.models import Competitor
from judge.models import Judge
from teachers.models import Teacher


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


def competitors_list(request, search: str = None):
    content = ContentType.objects.get_for_models(Competitor, Judge, Teacher)
    if search:
        elements = [
            field.objects.filter(first_name__icontains=search)
            for field in content.keys()
            if field.objects.filter(first_name__icontains=search).exists()
        ]
    else:
        elements = [field.objects.all() for field in content.keys()]
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
