from http.client import HTTPResponse
from django.shortcuts import render
from matplotlib.pyplot import get
from django.http import Http404, HttpResponseRedirect
from markdown import Markdown
from django.urls import reverse
from .forms import (
    CreateForm,
)
from .util import (
    list_entries,
    get_entry,
    save_entry,
)
from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries()
    })

def entry_view(request, title):
    page_content = get_entry(title)
    if page_content is None:
        raise Http404
    else:
        page_content = Markdown().convert(page_content)
    context = {
        'page_content' : page_content,
        'title': title,
    }
    return render(request, 'encyclopedia/entry.html', context = context)


def create_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            title, content = form.cleaned_data['title'], form.cleaned_data['content']
            save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
    form = CreateForm()
    context = {
        'form': form
    }
    return render(request, 'encyclopedia/create.html', context=context)


def random_view(request):
    result = choice(list_entries())
    return HttpResponseRedirect(f'../{result}/')
    