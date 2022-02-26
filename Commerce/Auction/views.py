from collections import UserList
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from .models import Listing
from .forms import (
    CreateBidForm,
    CreateCategoryForm,
    CreateCommentForm,
    CreateListingForm,
    LoginForm,
)

# Create your views here.

def index_view(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'auction/index.html', context=context)


def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        context = {
            'listing': listing
        }
    except:
        raise Http404
    return render(request, 'auction/listing.html', context=context)


def create_listing_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auction:login'))
    form = CreateListingForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            listing = Listing(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                user = request.user,
                starting_price = form.cleaned_data['starting_price'],
                # category = form.cleaned_data['category'],
            )
            listing.save()
            return HttpResponseRedirect(reverse('auction:listings', args=[listing.id]))
    context = {
        'form': form
    }
    return render(request, 'auction/create.html', context=context)

def edit_listing_view(request):
    pass

def delete_listing_view(request):
    pass

def close_listing_view(request):
    pass


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context['message'] = 'Invalid Username or Password.'
    return render(request, 'auction/login.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        username = request.user.username
        password = request.user.password
        user = authenticate(request, username=username, password=password)
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    context = {}
    return render(request, 'auction/logout.html', context=context)


