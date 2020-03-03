# Name: author_class
# Author: Reacubeth
# Mail: noverfitting@gmail.com
# *_*coding:utf-8 *_*

from django.shortcuts import render
from toolkit.initialization import neo_con

import json


def search_entity(request):
    nothing = {}
    if request.GET:
        entity = request.GET['user_text']
        db = neo_con
        entity_relation = db.get_rel(entity)
        if len(entity_relation) == 0:
            nothing = {'title': '<h1>Not Found</h1>'}
            return render(request, 'entity.html', {'nothing': json.dumps(nothing, ensure_ascii=False)})
        else:
            return render(request, 'entity.html', {'entity_relation': json.dumps(entity_relation, ensure_ascii=False)})

    return render(request, "entity.html", {'nothing': nothing})
