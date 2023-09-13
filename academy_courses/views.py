from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Course, Opinion, New, Slider, Urls, Video
from django.views.generic import DetailView, CreateView
from .forms import CourseForm, VideoForm

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



def course(request):

    query = request.GET.get('query')

    where = {}
    if query:
        where['name__icontains'] = query

    course = Course.objects.filter(**where)

    return render(
        request,
        'course.html',
        {
            'courses': course
        }
    )


def course_list(request, pk):
    video = Video.objects.filter(course=pk).select_related('course')

    return render(
        request,
        'course_list.html',
        {
            'videos': video,
        }
    )


class CourseDetailView(DetailView):
    model = Video
    template_name = 'course_page.html'
    context_object_name = 'video'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/create.html'
    success_url = reverse_lazy('course')