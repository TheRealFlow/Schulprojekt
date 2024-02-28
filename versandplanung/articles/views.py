from django.shortcuts import render

from versandplanung.articles.models import Article


def view_articles(request):
    """articles = [
        {
            'id': '1',
            'name': 'Bread',
            'price': 1.50,
            'short_description': 'Awesome Product'
        },
        {
            'id': '2',
            'name': 'Milk',
            'price': 2.50,
            'short_description': 'Awesome Product'
        },
        {
            'id': '3',
            'name': 'Eggs',
            'price': 3.50,
            'short_description': 'Awesome Product'
        }
    ]"""
    
    # articles = Article.objects.all() todo make reader form csv/xlsx file

    return render(request, 'articles.html', {
        'articles': articles
    })
