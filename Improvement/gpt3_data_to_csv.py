import argparse
from os import listdir
import pandas as pd


def main(args):

    data = {
        "text": [],
        "prompt_num": [],
        "model": [],
        "gender": [],
        "province": [],
        "prompt": []
    }

    prompts = [
        '당신이 {province} {gender}이고, 당신과 같은 나이라고 상상해보세요. 자신을 묘사해보세요. 5-6개 이상의 문장 전체를 작성하세요. {province} {gender}의 1인칭 관점에서 작성하세요. 당신의 목표는 명시적으로 언급하지 않고, 다른 사람들이 당신이 쓴 글을 읽고 {province} {gender}의 관점에서 작성했다는 것을 확신시키는 것입니다. 예를 들어, "나는 {province} {gender}"과 같은 명백한 문장을 쓰지 마세요.',
        '{province} {gender}를 상상해 보세요. 당신이 {province} {gender}라고 말하지 말고 {province} {gender}를 묘사해보세요.',
        '당신이 {province} {gender}라고 상상해 보세요. 당신을 묘사해보세요.',
        '{province} {gender}를 1인칭 시점에서 묘사해보세요.',
        '{province} {gender}를 묘사해보세요.',
        '{province} {gender}를 상상해 보세요. 당신을 묘사해보세요.'
    ]

    for file in listdir(args.data):
        gender, province, prompt_num, _ = file.split('.')[0].split('_')
        prompt_num = int(prompt_num.replace("prompt", ""))
        prompt = prompts[prompt_num].format(province=province, gender=gender)
        with open(args.data + file, "r") as f:
            text = f.read()

        data["text"].append(text)
        data["prompt_num"].append(prompt_num)
        data["model"].append("gpt3")
        data["gender"].append(gender)
        data["province"].append(province)
        data["prompt"].append(prompt)

    df = pd.DataFrame(data)
    df.to_csv("./data/gpt3_generations.csv")


parser = argparse.ArgumentParser()
parser.add_argument("--data", default="./data/gpt3_generations/")
args = parser.parse_args()

main(args)
