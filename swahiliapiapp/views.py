from django import forms
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from swahiliapiapp.models import English, Swahili


class SearchForm(forms.Form):
    searchterm = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter search term here'}))


def index(request):
    if request.method == "GET":
        return render(request, "swahiliapiapp/index.html", {'words': [], 'form': SearchForm()})
    else:
        f = SearchForm(request.POST)
        if f.is_valid():
            searchterm = f.cleaned_data["searchterm"].lower()
            return HttpResponseRedirect(f'/en-sw/{searchterm}')
        else:
            pass


def english_swahili(request, searchterm):
    words = English.objects.filter(english_word=searchterm)
    return render(request, "swahiliapiapp/index.html", {'words': words, 'form': SearchForm()})


def swahili_english(request, searchterm):
    words = Swahili.objects.filter(swahili_word=searchterm)
    return render(request, "swahiliapiapp/sw-en.html", {'words': words, 'form': SearchForm()})
