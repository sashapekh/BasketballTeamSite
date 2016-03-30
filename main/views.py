from django.shortcuts import render
from .models import ImagesLogo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


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
    errors = []
    form = {}
    if request.POST:
        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')

        if not form['name']:
            errors.append('Заполните Имя')
        if '@' not in form['email']:
            errors.append('Введите корректный email')
        if not form['message']:
            errors.append('Введите Сообщение')
        if not errors:
            print(form)
            return HttpResponse('Спасибо за ваше сообщение!')
    return render(request, 'forms.html', {'errors': errors, 'form': form})
