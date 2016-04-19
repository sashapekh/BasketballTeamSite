from django.shortcuts import render
from .models import ImagesLogo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from main.forms import SimpleForm



# Create your views here.
def main(request):
    img_obj = ImagesLogo.objects.all()
    p = Paginator(img_obj, 6)
    page = request.GET.get('page')
    try:
        get_img = p.page(page)
    except PageNotAnInteger:
        get_img = p.page(1)
    except EmptyPage:
        get_img = p.page(p.num_pages)

    return render(request, 'main.html', {'images': get_img})


def test_main(request):
    img_obj = ImagesLogo.objects.all()
    p = Paginator(img_obj, 6)
    page = request.GET.get('page')
    try:
        get_img = p.page(page)
    except PageNotAnInteger:
        get_img = p.page(1)
    except EmptyPage:
        get_img = p.page(p.num_pages)

    return render(request, 'testpage.html', {'images': get_img})


def form_view(request):
    name = ''
    if request.POST:

        form = SimpleForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['username']
            print(type(form))

    else:
        form = SimpleForm()

    return render(request,'forms.html', {'form': form , 'name':name})