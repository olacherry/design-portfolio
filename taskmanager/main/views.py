from django.shortcuts import render, redirect
from .forms import CardForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def works(request):
    return render(request, 'main/works.html')

def type(request):
    return render(request, 'main/type.html')

def network(request):
    return render(request, 'main/social_network.html')

def vk(request):
    return render(request, 'main/vk_type.html')

def inst(request):
    return render(request, 'main/inst_type.html')

def vk_a(request):
    return render(request, 'main/vk_advert.html')

def vk_c(request):
    return render(request, 'main/vk_creative.html')

def inst_p(request):
    return render(request, 'main/inst_post.html')

def inst_s(request):
    return render(request, 'main/inst_story.html')

def product(request):
    return render(request, 'main/product_type.html')

def product_m(request):
    return render(request, 'main/product_merch.html')

def product_pr(request):
    return render(request, 'main/product_print.html')

def contact(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
    form = CardForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context)

