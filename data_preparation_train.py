def prep_factoid(data: dict, test_file: bool = False) -> dict:
    paragraphs = []
    for j, question in enumerate(data['questions']):

        if question['type'] == 'factoid':
            q_text = question['body'].replace(r'\u', '')
            id_base = question['id']
            #id = question['id']
            ideal = question['ideal_answer']
            exact = question['exact_answer']
            if test_file:
                exact = exact[0]
            for i, snippet in enumerate(question['snippets']):
                id = id_base + f'_{i+1:03}'
                context = snippet['text'].replace(r'\u', '')
                answer_start = -1
                is_impossible = False
                if not test_file:
                    for ans in set(ideal+exact):
                        ans = ans.replace(r'\u', '')
                        idx_found = context.lower().find(ans.lower())
                        if idx_found >= 0:
                            answer_start = idx_found
                            exact_answer = ans
                    if answer_start == -1:
                        is_impossible = True
                        continue
                    answers = [{
                        'text': exact_answer,
                        'answer_start': answer_start
                    }]
                else:
                    if len(id) != 28:
                        id = id + f'_{i+1:03}'
                    answers = []
                sample = {
                    'qas': [{
                        'id': id,
                        'question': q_text,
                        'answers': answers
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