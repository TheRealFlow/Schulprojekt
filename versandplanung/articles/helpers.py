import json
from random import choices, randint
from typing import List

from versandplanung.articles.models import Article

def get_random_selection_from_list(list: List[Article]) -> list[dict]:
    # articles each user purchases
    article_per_user = randint(1, 6)
    
    chosen_articles = set(choices(list, k=article_per_user))
    
    output: str = "[{"
    for index, article  in enumerate(chosen_articles):
        output += f"\"{article.get_name()}\": {randint(1, 3)}"
        if index < len(chosen_articles) - 1:
            output += "}, {"
        else:
            output += "}]"
            
    return json.loads(output)