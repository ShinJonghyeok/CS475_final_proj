import argparse
from os import listdir
import pandas as pd

def main():
    df = pd.read_csv("./data/clovax_generations.csv")
     
    texts = []
    file_list = listdir("./data/clovax_generations/")
    for _, row in df.iterrows():        
        gender, province, prompt_num, i = row['gender'], row['province'], row['prompt_num'], row['iteration']
        print(gender, province, prompt_num, i, end=" ")

        if f"{gender}_{province}_prompt{prompt_num}_{i}.txt" in file_list:
            with open(f"./data/clovax_generations/{gender}_{province}_prompt{prompt_num}_{i}.txt", "r") as f:
                text = f.read()
    
        else:
            text = " "
        
        texts.append(text)
    
    assert len(texts) == len(df)
    df['text'] = texts
    df.to_csv("./data/clovax_generations.csv")
            
if __name__ == "__main__":
    main()