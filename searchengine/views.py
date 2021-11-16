from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from .forms import SearchForm


# Home page with form
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        query = request.POST.get('query')
        
        if form.is_valid():
            return HttpResponseRedirect('/search/?q=' + query)
    else:
        form = SearchForm()
        return render(request, 'index.html', {'form': form})


# GET /search/?q=covid
def search(request):
    query = request.GET.get('q', None)

    if query == None or query == '':
        form = SearchForm()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'result.html', {'question': query})
