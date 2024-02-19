from django.shortcuts import render


def get_fetch_articles(request):
    return render(request, 'main_articles.html')

