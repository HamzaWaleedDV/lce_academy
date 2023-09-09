from django.shortcuts import render
from .models import Course, Opinion, New, Slider, Urls

# Create your views here.

def index(request):
    slider = Slider.objects.all()


    return render(
        request,
        'index.html',
        {
            'slider': slider,
        }
    )


def about(request):
    aboutus_image = Slider.objects.first()
    opinion = Opinion.objects.all()

    return render(request, 'about.html', {'image': aboutus_image,})