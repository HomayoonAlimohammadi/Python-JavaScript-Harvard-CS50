from django.shortcuts import render
from matplotlib.pyplot import get
from django.http import Http404
from markdown import Markdown

from .util import (
    list_entries,
    get_entry,
)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": list_entries()
    })

def entry_view(request, title):
    page_content = get_entry(title)
    if page_content is None:
        return Http404
    else:
        page_content = Markdown().convert(page_content)
    context = {
        'page_content' : page_content,
        'title': title,
    }
    return render(request, 'encyclopedia/entry.html', context = context)

