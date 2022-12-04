from django.urls import HttpResponse
def home_page(request):
    print("Home page requested")
    return HttpResponse("This is Home page")