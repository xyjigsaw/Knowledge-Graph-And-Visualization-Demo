# Name: raw2json
# Author: Reacubeth
# Time: 2020/3/11 11:25
# Mail: noverfitting@gmail.com
# *_*coding:utf-8 *_*


def analysis(entity_relation):
    if not entity_relation:
        return {'status': 404, 'message': 'Not Found in Database'}
    format_triple = []
    categories = []
    cat_only = []
    data = []
    links = []
    n1_only = []
    n2_only = []
    n3_only = []

    flag4loc = 0
    for i in range(len(entity_relation)):
        triple = {}
        triple['relation'] = entity_relation[i]['rel']['type']
        relation = {}
        relation['value'] = entity_relation[i]['rel']['type']
        if entity_relation[i]['rel']['type'] == 'diagnosedIn':
            node = {}
            node['id'] = 'l' + entity_relation[i]['n1']['l_id']
            node['draggable'] = 'true'
            node['name'] = entity_relation[i]['n1']['locationName']
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 0
            if node['id'] not in n1_only:
                n1_only.append(node['id'])
                data.append(node)
                if 'Location' not in cat_only:
                    categories.append({'name': 'Location'})
                    cat_only.append('Location')

            relation['source'] = node['id']
            node = {}
            node['id'] = 'p' + entity_relation[i]['n2']['p_id']
            node['draggable'] = 'true'
            try:
                node['name'] = entity_relation[i]['n2']['gender'] + ' ' + entity_relation[i]['n2']['age']
            except KeyError:
                try:
                    node['name'] = entity_relation[i]['n2']['age']
                except KeyError:
                    node['name'] = '未知'
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 1
            if flag4loc == 1: node['category'] = 2
            if node['id'] not in n2_only:
                n2_only.append(node['id'])
                data.append(node)
                if 'Patient' not in cat_only:
                    categories.append({'name': 'Patient'})
                    cat_only.append('Patient')

            relation['target'] = node['id']
            triple['target'] = entity_relation[i]['n1']['locationName']
            try:
                triple['source'] = entity_relation[i]['n2']['gender'] + ' ' + entity_relation[i]['n2']['age']
            except KeyError:
                try:
                    triple['source'] = entity_relation[i]['n2']['age']
                except KeyError:
                    triple['source'] = '未知'
        elif entity_relation[i]['rel']['type'] == 'happenIn':
            flag4loc = 1
            node = {}
            node['id'] = 'l' + entity_relation[i]['n1']['l_id']
            node['draggable'] = 'true'
            node['name'] = entity_relation[i]['n1']['locationName']
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 0
            if node['id'] not in n1_only:
                n1_only.append(node['id'])
                data.append(node)
                if 'Location' not in cat_only:
                    categories.append({'name': 'Location'})
                    cat_only.append('Location')

            relation['target'] = node['id']
            node = {}
            node['id'] = 'e' + entity_relation[i]['n2']['e_id']
            node['draggable'] = 'true'
            node['name'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 1
            if node['id'] not in n2_only:
                n2_only.append(node['id'])
                data.append(node)
                if 'Event' not in cat_only:
                    categories.append({'name': 'Event'})
                    cat_only.append('Event')

            relation['source'] = node['id']
            triple['target'] = entity_relation[i]['n1']['locationName']
            triple['source'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']

        elif entity_relation[i]['rel']['type'] == 'belong2':
            node = {}
            node['id'] = 'e' + entity_relation[i]['n1']['e_id']
            node['draggable'] = 'true'
            node['name'] = entity_relation[i]['n1']['time'] + ' ' + entity_relation[i]['n1']['text']
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 0
            if node['id'] not in n1_only:
                n1_only.append(node['id'])
                data.append(node)
                if 'Event' not in cat_only:
                    categories.append({'name': 'Event'})
                    cat_only.append('Event')

            relation['source'] = node['id']
            node = {}
            node['id'] = 't' + entity_relation[i]['n2']['t_id']
            node['draggable'] = 'true'
            node['name'] = entity_relation[i]['n2']['topicName']
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 1
            if node['id'] not in n2_only:
                n2_only.append(node['id'])
                data.append(node)
                if 'Topic' not in cat_only:
                    categories.append({'name': 'Topic'})
                    cat_only.append('Topic')

            relation['target'] = node['id']
            triple['target'] = entity_relation[i]['n2']['topicName']
            triple['source'] = entity_relation[i]['n1']['time'] + ' ' + entity_relation[i]['n1']['text']
        elif entity_relation[i]['rel']['type'] == 'hasEvent':
            node = {}
            node['id'] = 'p' + entity_relation[i]['n1']['p_id']
            node['draggable'] = 'true'
            try:
                node['name'] = entity_relation[i]['n1']['gender'] + ' ' + entity_relation[i]['n1']['age']
            except KeyError:
                try:
                    node['name'] = entity_relation[i]['n1']['age']
                except KeyError:
                    node['name'] = '未知'
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 0
            if node['id'] not in n1_only:
                n1_only.append(node['id'])
                data.append(node)
                if 'Patient' not in cat_only:
                    categories.append({'name': 'Patient'})
                    cat_only.append('Patient')

            relation['source'] = node['id']
            node = {}
            node['id'] = 'e' + entity_relation[i]['n2']['e_id']
            node['draggable'] = 'true'
            node['name'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']
            node['value'] = 0
            node['symbolSize'] = 50
            node['category'] = 1
            if node['id'] not in n2_only:
                n2_only.append(node['id'])
                data.append(node)
                if 'Event' not in cat_only:
                    categories.append({'name': 'Event'})
                    cat_only.append('Event')

            relation['target'] = node['id']
            triple['source'] = entity_relation[i]['n1']['patientName']
            triple['target'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']

        links.append(relation)
        format_triple.append(triple)

        if 'rel2' in entity_relation[0]:
            for i in range(len(entity_relation)):
                triple = {}
                triple['relation'] = entity_relation[i]['rel2']['type']
                relation = {}
                relation['value'] = entity_relation[i]['rel2']['type']
                if entity_relation[i]['rel2']['type'] == 'happenIn':
                    node = {}
                    node['id'] = 'l' + entity_relation[i]['n3']['l_id']
                    node['draggable'] = 'true'
                    node['name'] = entity_relation[i]['n3']['locationName']
                    node['value'] = 0
                    node['symbolSize'] = 50
                    node['category'] = 2
                    if node['id'] not in n3_only:
                        n3_only.append(node['id'])
                        data.append(node)
                        if 'Location' not in cat_only:
                            categories.append({'name': 'Location'})
                            cat_only.append('Location')

                    relation['target'] = node['id']
                    node = {}
                    node['id'] = 'e' + entity_relation[i]['n2']['e_id']
                    node['draggable'] = 'true'
                    node['name'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']
                    node['value'] = 0
                    node['symbolSize'] = 50
                    node['category'] = 1
                    if node['id'] not in n2_only:
                        n2_only.append(node['id'])
                        data.append(node)
                        if 'Event' not in cat_only:
                            categories.append({'name': 'Event'})
                            cat_only.append('Event')

                    relation['source'] = node['id']
                    triple['target'] = entity_relation[i]['n3']['locationName']
                    triple['source'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']
                elif entity_relation[i]['rel2']['type'] == 'hasEvent':
                    node = {}
                    node['id'] = 'p' + entity_relation[i]['n3']['p_id']
                    node['draggable'] = 'true'
                    try:
                        node['name'] = entity_relation[i]['n3']['gender'] + ' ' + entity_relation[i]['n3']['age']
                    except KeyError:
                        try:
                            node['name'] = entity_relation[i]['n3']['age']
                        except KeyError:
                            node['name'] = '未知'
                    node['value'] = 0
                    node['symbolSize'] = 50
                    node['category'] = 2
                    if node['id'] not in n3_only:
                        n3_only.append(node['id'])
                        data.append(node)
                        if 'Patient' not in cat_only:
                            categories.append({'name': 'Patient'})
                            cat_only.append('Patient')

                    relation['source'] = node['id']
                    node = {}
                    node['id'] = 'e' + entity_relation[i]['n2']['e_id']
                    node['draggable'] = 'true'
                    node['name'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']
                    node['value'] = 0
                    node['symbolSize'] = 50
                    node['category'] = 1
                    if node['id'] not in n2_only:
                        n2_only.append(node['id'])
                        data.append(node)
                        if 'Event' not in cat_only:
                            categories.append({'name': 'Event'})
                            cat_only.append('Event')

                    relation['target'] = node['id']
                    try:
                        triple['source'] = entity_relation[i]['n3']['gender'] + ' ' + entity_relation[i]['n3']['age']
                    except KeyError:
                        try:
                            triple['source'] = entity_relation[i]['n3']['age']
                        except KeyError:
                            triple['source'] = '未知'
                    triple['target'] = entity_relation[i]['n2']['time'] + ' ' + entity_relation[i]['n2']['text']

                links.append(relation)
                format_triple.append(triple)
        # print(data, links, format_triple, categories)
    return {'status': 200, 'message': 'success', 'data': data, 'links': links, 'format_triple': format_triple, 'categories': categories}
