from collections import UserList
from http.client import HTTPResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from .models import Listing, Comment, Category
from .forms import (
    CreateBidForm,
    CreateCategoryForm,
    CreateCommentForm,
    CreateListingForm,
    LoginForm,
    CreateUserForm,
)
from django.contrib import messages
from django.db.models import Q


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
    except:
        raise Http404
    comment_form = CreateCommentForm()
    user = request.user
    if user.is_authenticated:
        if user in listing.watchers.all():
            is_watching = True
        else:
            is_watching = False
    else:
        is_watching = False
    context = {
    'listing': listing,
    'is_watching': is_watching,
    'comment_form': comment_form,
    }
    return render(request, 'auction/listing.html', context=context)


def toggle_watch(request, id):
    try:
        listing = Listing.objects.get(id=id)
    except:
        raise Http404
    user = request.user
    if user.is_authenticated:
        if user in listing.watchers.all():
            listing.watchers.remove(user)
            is_watching = False
        else: 
            listing.watchers.add(user)
            is_watching = True
    else:
        return HttpResponseRedirect(reverse('auction:login'))
    context = {
        'listing': listing,
        'is_watching': is_watching,
    }
    return render(request, 'auction/listing.html', context)


def watchlist_view(request):
    user = request.user
    if user.is_authenticated:
        watchlist = user.watchlist.all()
    context = {
        'watchlist': watchlist,
    }
    return render(request, 'auction/watchlist.html', context)


def create_listing_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auction:login'))
    if request.method == 'POST':
        form = CreateListingForm(request.POST, request.FILES or None)
        if form.is_valid():
            listing = Listing(
                title = form.cleaned_data['title'],
                description = form.cleaned_data.get('description'),
                user = request.user,
                starting_price = form.cleaned_data['starting_price'],
                image = form.cleaned_data.get('image')
                # category = form.cleaned_data['category'],
            )
            listing.save()

            categories = form.cleaned_data.get('categories')
            if categories is not None:
                categories = categories.split()
            for category_name in categories:
                try:
                    category = Category.objects.get(name=category_name)
                except:
                    category = Category(name=category_name)
                    category.save()
                listing.category.add(category)
            return HttpResponseRedirect(reverse('auction:listing', args=[listing.id]))
    else:
        form = CreateListingForm()
    context = {
        'form': form,
        'method': 'create'
    }
    return render(request, 'auction/create-edit.html', context=context)


def edit_listing_view(request, id=None):
    try:
        listing = Listing.objects.get(id=id)
        categories = ' '.join([category.name for category in listing.category.all()])
        listing_context = {
            'title': listing.title,
            'description': listing.description,
            'starting_price': listing.starting_price,
            'image': listing.image,
            'categories': categories,
        }
        form = CreateListingForm(listing_context)
        context = {
            'form': form,
            'method': 'edit'
        }
    except:
        raise Http404
    if request.method == 'POST':
        form = CreateListingForm(request.POST, request.FILES or None)
        listing = Listing.objects.get(id=id)
        if form.is_valid():
            
            categories = form.cleaned_data.get('categories')
            if categories is not None:
                categories = categories.split()

            if listing.category is not None:
                for category in listing.category.all():
                    listing.category.remove(category)

            for category_name in categories:
                try:
                    category = Category.objects.get(name=category_name)
                except:
                    category = Category(
                        name=category_name,
                    )
                    category.save()
                listing.category.add(category)

            listing.title = form.cleaned_data['title']
            listing.description = form.cleaned_data.get('description')
            listing.starting_price = form.cleaned_data['starting_price']
            if form.cleaned_data.get('image') is not None:
                listing.image = form.cleaned_data.get('image')

            listing.save()
            return HttpResponseRedirect(reverse('auction:listing', args=[id]))
        else:
            context['message'] = 'Invalid Inputs!'

    return render(request, 'auction/create-edit.html', context=context)
    
    

def delete_listing_view(request, id=None):
    try:
            listing = Listing.objects.get(id=id)     
    except:
        raise Http404

    if request.method == 'POST':
        listing.delete()
        return HttpResponseRedirect(reverse('auction:index'))
        
    context = {
        'listing': listing,
    }
    return render(request, 'auction/delete.html', context)
    


def close_listing_view(request):
    pass


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print('form',form.cleaned_data)
            user = authenticate(request, username=username, password=password)
            print('user',user)
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


def register_view(request):
    form = CreateUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return HttpResponseRedirect(reverse('index'))
        messages.error(request, 'Unsuccessful Registration. Invalid information.')
    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)


def search_view(request):
    if request.method == 'POST':
        q = request.POST['q']
    else:
        q = ''
    listings = Listing.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
    context = {
        'listings': listings
    }
    return render(request, 'auction/index.html', context)

def add_comment_view(request, id):
    form = CreateCommentForm(request.POST or None)
    try:
        listing = Listing.objects.get(id=id)
    except:
        raise Http404
    user = request.user
    if request.method == 'POST':
        if form.is_valid() and user.is_authenticated:
            content = form.cleaned_data.get('content')
            comment = Comment(
                user = user,
                listing = listing,
                content = content,
            )
            comment.save()

    return HttpResponseRedirect(reverse('auction:listing', args=[id]))



def delete_comment_view(request, id, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except: 
        raise Http404
    comment.delete()

    return HttpResponseRedirect(reverse('auction:listing', args=[id]))


def category_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except:
        raise Http404
    listings = Listing.objects.filter(category=category).all()
    context = {
        'listings': listings
    }

    return render(request, 'auction/index.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    for category in categories:
        if category.listings.all().count() == 0:
            category.delete()
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'auction/category_list.html', context)