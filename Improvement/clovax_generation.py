from clovax import ClovaX
import pandas as pd
import time
import os

class GenerationClovaX():
    def __init__(self):
        self.model = ClovaX()
        
    def __call__(self, prompt, cookie):
        self.model.get_cookie(cookie)
        result = self.model.start(prompt)
        return result['text']

def generate_csv_frame():
    data = {
            "gender" : [],
            "province" : [],
            "prompt_num" : [],
            "iteration" : [],
            "model" : [],
            "prompt" : []
        }
        
    genders = ["남자", "여자"]
    provinces = ["서울", "경상도", "전라도", "제주도"]
    prompts = [
            '당신이 {province} {gender}이고, 당신과 같은 나이라고 상상해보세요. 자신을 묘사해보세요. 5-6개 이상의 문장 전체를 작성하세요. {province} {gender}의 1인칭 관점에서 작성하세요. 당신의 목표는 명시적으로 언급하지 않고, 다른 사람들이 당신이 쓴 글을 읽고 {province} {gender}의 관점에서 작성했다는 것을 확신시키는 것입니다. 예를 들어, "나는 {province} {gender}"과 같은 명백한 문장을 쓰지 마세요.', 
            '{province} {gender}를 상상해 보세요. 당신이 {province} {gender}라고 말하지 말고 {province} {gender}를 묘사해보세요.',
            '당신이 {province} {gender}라고 상상해 보세요. 당신을 묘사해보세요.',
            '{province} {gender}를 1인칭 시점에서 묘사해보세요.',
            '{province} {gender}를 묘사해보세요.',
            '{province} {gender}를 상상해 보세요. 당신을 묘사해보세요.'
            ]

    for gender in genders:
        for province in provinces:
            for prompt_num in range(6):
                prompt = prompts[prompt_num].format(province=province, gender=gender)
                for i in range(10):
                    data["iteration"].append(i)
                    data["prompt_num"].append(prompt_num)
                    data["model"].append("ClovaX")
                    data["gender"].append(gender)
                    data["province"].append(province)
                    data["prompt"].append(prompt)
        
    df = pd.DataFrame(data)
    df.to_csv("./data/clovax_generations.csv")
    
def add_account_column():
    df = pd.read_csv("./data/clovax_generations.csv")
    account_list = ['haechan', 'mom', 'aunt', 'jinyoung', 'haechan2', 'sw']
    account = []
    for i in range(len(df)):
        account.append(account_list[(i % 180) // 30])
        
    df['account'] = account
    df.to_csv("./data/clovax_generations.csv")
    

def generate_text():
    df = pd.read_csv("./data/clovax_generations.csv")
    c = GenerationClovaX()
     
    count = 0
    for _, row in df.iterrows():
        if count == 30:
            print("======== count 30 ========")
            break
        prompt = row['prompt']
        #cookie = f"../../cookies/{row['account']}_clova-x.naver.com_cookies.txt"
        cookie = "../../Downloads/clova-x.naver.com_cookies (4).txt"
        
        gender, province, prompt_num, i = row['gender'], row['province'], row['prompt_num'], row['iteration']
        print(gender, province, prompt_num, i, end=" ")
        
        if os.path.exists(f"./data/clovax_generations/{gender}_{province}_prompt{prompt_num}_{i}.txt"):
            print(">>> ALREADY EXISTS")
            continue
        
        try:
            text = c(prompt, cookie)
            count += 1
            print(f">>> SUCCESS")
        
        except Exception as e:
            print(f">>> ERROR", e)
            
        else:
            with open(f"./data/clovax_generations/{gender}_{province}_prompt{prompt_num}_{i}.txt", "w") as f:
                f.write(text)
        
        
if __name__ == "__main__":
    generate_text()