from .models import Course, Opinion, Urls

def slider_footer(request):
    course = Course.objects.all()
    opinion = Opinion.objects.all()
    url = Urls.objects.all()

    return {
        'courses': course,
        'opinions': opinion,
        'urls': url,
    }