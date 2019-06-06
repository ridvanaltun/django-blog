from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from _blog.models import Blog
from .forms import ContactForm

def IndexView(request):

    # Order by created date
    blog = Blog.objects.order_by('-created_date')
    context = {
        "blog": blog
    }

    #return HttpResponse("Hello World!")
    # templates/web/index.html
    return render(request, 'web/index.html', context)

def AboutView(request):
    return render(request, 'web/about.html')

#@login_required
def BlogDetailView(request, id):

    # Blog.objects.get(id = id) is same as Blog.objects.filter(id = id).first()
    blog = Blog.objects.get(id = id)
    context = {
        "blog": blog
    }
    return render(request, 'web/blog-detail.html', context)

def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        Contact = form.save(commit = True)
        return redirect("_blog:contact")
    context = {
        "form": form
    }
    return render(request, 'web/contact.html', context)