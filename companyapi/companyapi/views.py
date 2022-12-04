from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page requested")
    friends = [
        'ankit',
        'ravi',
        'uttam'
    ]
    # return HttpResponse("<h1>This is Home page<h1>")
    return JsonResponse(friends,safe=False)