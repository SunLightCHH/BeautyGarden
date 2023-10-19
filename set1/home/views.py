from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def course(request):
    return render(request, 'course.html')

def courseDetail(request):
    return render(request, 'course-detail.html')

def contact(request):
    return render(request, 'contact.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def blogarchive(request):
    return render(request, 'blog-archive.html')

def Page404(request):
    return render(request, '404.html')