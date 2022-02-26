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
    pass


def logout_view(request):
    pass
