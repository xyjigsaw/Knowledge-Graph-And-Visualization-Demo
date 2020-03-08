# Name: author_class
# Author: Reacubeth
# Mail: noverfitting@gmail.com
# *_*coding:utf-8 *_*

from django.shortcuts import render
from toolkit.initialization import neo_con
from jieba import posseg
import json
import cpca


def is_loc(loc):
    d = cpca.transform([loc], open_warning=False)
    if str(d['省'][0]):
        return True
    if str(d['市'][0]):
        return True
    if str(d['区'][0]):
        return True
    return False


def entity_analysis(entity):
    db = neo_con
    words = entity.split(' ')
    if len(words) == 1:
        if is_loc(words[0]):
            return db.match_location4event_patient(entity)
        else:
            wordp = posseg.cut(words[0])
            for w in wordp:
                if w.flag in ['v', 'vd', 'vn', 'vg']:
                    return db.match_topic4event(entity)
                elif w.flag in ['nr']:
                    return db.match_patient_name(entity)
    elif len(words) == 2:
        isloc_dict = {}
        flag = 0
        for word in words:
            isloc_dict[word] = is_loc(word)
            if isloc_dict[word]:
                flag = 1
        if isloc_dict[words[0]]:
            wordp = posseg.cut(words[1])
            for w in wordp:
                if w.flag in ['v', 'vd', 'vn', 'vg']:
                    return db.match_location_topic4event(words[0], words[1])
                elif w.flag in ['m']:
                    return db.match_location_time4event_patient(words[0], words[1])
                else:
                    gender = words[1].replace('性', '').replace('生', '')
                    return db.match_location_gender4patient(words[0], gender)
        else:
            wordp = posseg.cut(words[0])
            for w in wordp:
                if w.flag in ['v', 'vd', 'vn', 'vg']:
                    return db.match_location_topic4event(words[1], words[0])
                elif w.flag in ['m']:
                    return db.match_location_time4event_patient(words[1], words[0])
                else:
                    gender = words[0].replace('性', '').replace('生', '')
                    return db.match_location_gender4patient(words[1], gender)

        if not flag:
            wordp = posseg.cut(words[0])
            for w in wordp:
                if w.flag in ['m']:
                    return db.match_name_time4location_event(words[1], words[0])
                else:
                    return db.match_name_time4location_event(words[0], words[1])
    elif len(words) == 3:
        loc = ''
        time = ''
        topic = ''
        for word in words:
            if is_loc(word):
                loc = word
                words.remove(word)
                break
        wordp = posseg.cut(words[0])
        for w in wordp:
            if w.flag in ['m']:
                return db.match_location_time_topic4patient(loc, words[0],  words[1])
            else:
                return db.match_location_time_topic4patient(loc, words[1], words[0])

    else:
        answer = db.match_location4event_patient(words[0])
        if len(answer) == 0:
            answer = db.match_topic4event(words[0])
        return answer


def search_entity(request):
    nothing = {}
    if request.GET:
        entity = request.GET['user_text']
        entity_relation = entity_analysis(entity)
        try:
            if len(entity_relation) == 0:
                nothing = {'title': '<h1>Not Found</h1>'}
                return render(request, 'entity.html', {'nothing': json.dumps(nothing, ensure_ascii=False)})
            else:
                return render(request, 'entity.html', {'entity_relation': json.dumps(entity_relation, ensure_ascii=False)})
        except:
            nothing = {'title': '<h1>Not Found</h1>'}
            return render(request, 'entity.html', {'nothing': json.dumps(nothing, ensure_ascii=False)})

    return render(request, "entity.html", {'nothing': nothing})

