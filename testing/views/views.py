from django.shortcuts import render
# from django.http import HttpResponse

from ..models import Book 
 
def homePageView(request):
    return render(request, "index.html")

def searchView(request): 
    return render(request, "search.html")

def resultsView(request):
    token = request.GET.get('token')
    results = Book.objects.values_list("name", flat=True)
    results = list(filter(lambda t: token in t.lower(), results))
    print(results)
    return render(request, "results.html", { "token": token, "results": results })
