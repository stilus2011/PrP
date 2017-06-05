from django.shortcuts import render, get_object_or_404
from .models import Section, Lesson


def index(request):
    sections = Section.objects.all().order_by('-section_priority')
    return render(request, 'lessons/index.html', {'sections': sections})


def detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessons/detail.html', {'lesson': lesson})
