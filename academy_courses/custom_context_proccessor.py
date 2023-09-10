from .models import Course, Opinion, Urls
from academy_blog.models import Category, Article

def slider_footer(request):
    course = Course.objects.all()
    opinion = Opinion.objects.all()
    url = Urls.objects.all()

    return {
        'courses': course,
        'opinions': opinion,
        'urls': url,
    }

def category(request):
    cat = Category.objects.all()
    latest_article = Article.objects.order_by('-created_at')[:10]

    return {
        'cats': cat,
        'la_ar': latest_article,
    }