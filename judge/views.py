from django.shortcuts import get_object_or_404, render

from .models import Judge


def dashboard(request):
    judges = Judge.objects.all()
    return render(
        request,
        'judges/display_judge.html',
        {
            'section': 'judges',
            'judges': judges,
        },
    )


def judge_detail(request, slug):
    judge = get_object_or_404(Judge, slug=slug)
    return render(
        request,
        'judges/judge/detail.html',
        {
            'section': 'judges',
            'judge': judge,
        },
    )
