'''
단어 세부 분석
'''

import pickle

def print_count():
    with open("./all_results.p", 'rb') as f:
        data = pickle.load(f)['total']
        
    models = ['gpt-3.5-turbo', 'gpt-4-1106-preview', 'CLOVA X', 'Bard']
    groups = ['서울 남자', '서울 여자', '경상도 남자', '경상도 여자', '전라도 남자', '전라도 여자', '제주도 남자', '제주도 여자']

    for model in models:
        print(">>> ", model)
        for group in groups:
            print("\t>>> ", group, len(data[model][group]))
            
def word_dup():
    with open("./all_results.p", 'rb') as f:
        data = pickle.load(f)['total']
    
    models = ['gpt-3.5-turbo', 'gpt-4-1106-preview', 'CLOVA X', 'Bard']
    groups = ['서울 남자', '서울 여자', '경상도 남자', '경상도 여자', '전라도 남자', '전라도 여자', '제주도 남자', '제주도 여자']
    
    # make result
    result = {group : dict() for group in groups}
    for model in models:
        for group in groups:
            for word in data[model][group]:
                if word in result[group].keys():
                    result[group][word].append(model)
                else:
                    result[group][word] = [model]
    
    # validation check
    result_count = {k : sum([len(m) for _, m in v.items()]) for k, v in result.items()}
    data_count = {group : 0 for group in groups}
    for model in models:
        for group in groups:
            data_count[group] += len(data[model][group])
    
    assert result_count == data_count
    
    # sorting
    for group, words in result.items():
        result[group] = {k : v for (k, v) in sorted(words.items(), key = lambda item: len(item[1]), reverse=True)}
        
    # printing
    for group, words in result.items():
        print(">>> ", group)
        for word, models in words.items():
            print("\t>>> ", word, ": ", models)

    
if __name__ == "__main__":
    word_dup()