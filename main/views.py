from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406430104',
        'name': 'Muhammad Fadhil Al Afifi Fajar',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
