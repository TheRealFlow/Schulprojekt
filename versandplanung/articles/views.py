from django.shortcuts import render


def view_articles(request):
    articles = [
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
    ]

    return render(request, 'articles.html', {
        'articles': articles
    })
