from django.shortcuts import render
from .models import Course, Opinion, New, Slider

# Create your views here.

def index(request):
    slider = Slider.objects.all()
    course = Course.objects.all()
    opinion = Opinion.objects.all()
    new = New.objects.all()

    return render(
        request,
        'index.html',
        {
            'slider': slider,
            'courses': course,
            'opinions': opinion,
            'new': new,
        }
    )