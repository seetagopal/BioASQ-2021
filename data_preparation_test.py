def prep_factoid_test(data: dict, test_file: bool = False) -> dict:
    paragraphs = []
    for j, question in enumerate(data['questions']):
        if question['type'] == 'factoid':
            q_text = question['body'].replace(r'\u', '')
            id_base = question['id']
            #id = question['id']
            #ideal = question['ideal_answer']
           # exact = question['exact_answer']
            if test_file:
                exact = exact[0]
            for i, snippet in enumerate(question['snippets']):
                id = id_base + f'_{i+1:03}'
                context = snippet['text'].replace(r'\u', '')
                sample = {
                    'qas': [{
                        'id': id,
                        'question': q_text,
                        #'answers': answers
                    }],
                    'context': context
                }
                paragraphs.append(sample)
    prepped_dict = {
        'data': [{
            'paragraphs': paragraphs
        }]
    }
    return prepped_dict