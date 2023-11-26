from django.shortcuts import get_object_or_404, render

from .models import Teacher


def dashboard(request):
    teachers = Teacher.objects.all()
    return render(
        request,
        'teachers/display_teachers.html',
        {
            'section': 'teachers',
            'teachers': teachers,
        },
    )


def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    return render(
        request,
        'teachers/teacher/detail.html',
        {
            'section': 'teachers',
            'teacher': teacher,
        },
    )
