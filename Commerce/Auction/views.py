from django.shortcuts import render
from .models import Listing

# Create your views here.

def index_view(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'auction/index.html', context=context)


def listings_view(request):
    context = {}
    return render(request, 'auction/listings.html', context=context)


def create_listing_view(request):
    if request.method == 'POST':
        pass
    context = {

    }
    return render(request, 'auction/create.html', context=context)

def edit_listing_view(request):
    pass

def delete_listing_view(request):
    pass

def close_listing_view(request):
    pass