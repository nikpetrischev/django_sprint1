from django.shortcuts import render
from django.http import Http404


# List of posts with their params. For testing purposes.
posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]


# Main page/List of posts' previews
def index(request):
    # Send posts list (WiP) into context var.
    context = {'posts': posts}
    # Render template into page.
    return render(request, 'blog/index.html', context)


# Post No.id page with details.
def post_detail(request, id):
    # Try to get required post if it exists.
    try:
        # Send post_<id> into context var.
        context = {
            'post': [post for post in posts if post['id'] == id][0],
        }
    except IndexError:
        raise Http404(f'Post No.{id} does not exist.')
    # Render template into page.
    return render(request, 'blog/detail.html', context)


# Page with the list of posts by category.
def category_posts(request, category_slug):
    # Send category name into context var.
    context = {
        'category': category_slug,
    }
    # Render template into page.
    return render(request, 'blog/category.html', context)
