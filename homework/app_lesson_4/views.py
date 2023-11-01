from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Count
#  from django.urls import reverse_lazy
from .models import Advertisement
from .forms import AdvertisementsForm


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_lesson_4/index.html', context)


def top_sellers(request):
    users = User.objects.annotate(adv_counts=Count('advertisement').order_by('-adv_count'))
    context = {
        'users': users,
    }
    return render(request, 'app_lesson_4/top-sellers.html', context)


def advertisement_post(request):
    form = AdvertisementsForm()
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = Advertisement(**form.cleaned_data)
            advertisements.User = request.user
            advertisements.save()
            url = reverse('main-page')
            return redirect(url)
    context = {'form': form}
    return render(request, 'app_lesson_4/advertisement-post.html', context)


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {
        'advertisement': advertisement,
    }
    return render(request, 'app_lesson_4/advertisement.html', context)
