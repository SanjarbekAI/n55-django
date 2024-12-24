from django.shortcuts import render

from blogs.models import BlogsModel


def home_page_view(request):
    return render(request, 'home.html')


def blogs_page_view(request):
    blogs = BlogsModel.objects.filter(author__is_active=True)

    context = {
        "blogs": blogs
    }

    return render(request, 'blogs.html', context)


def contact_page_view(request):
    return render(request, 'contacts.html')
