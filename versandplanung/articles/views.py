from django.shortcuts import render


def view_articles(request):
    articles = [
        {
            'name': 'Bier',
            'price': 1.50,
            'quantity': 100
        },
        {
            'name': 'Pizza',
            'price': 2.50,
            'quantity': 50
        },
        {
            'name': 'Klopapier',
            'price': 3.50,
            'quantity': 10
        }
    ]

    return render(request, 'article.html', {
        'articles': articles
    })
