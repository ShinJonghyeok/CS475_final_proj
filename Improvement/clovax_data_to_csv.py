import argparse
import os
import pandas as pd

def main():
    df = pd.read_csv("./data/clovax_generations.csv")
     
    texts = []
    file_list = os.listdir("./data/clovax_generations/")
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
            
            
def excel_to_txt():
    df = pd.read_excel("./data/clovax_generations.xlsx")
    
    for _, row in df.iterrows():        
        gender, province, prompt_num, i = row['gender'], row['province'], row['prompt_num'], row['iteration']
        print(gender, province, prompt_num, i, end=" ")

        if os.path.exists(f"./data/clovax_generations/{gender}_{province}_prompt{prompt_num}_{i}.txt"):
            print(">>> already exists")
            continue
        
        if type(row['text'])==float or row['text'].isspace():
            print(">>> no text")
            continue
        
        with open(f"./data/clovax_generations/{gender}_{province}_prompt{prompt_num}_{i}.txt", "w") as f:
            f.write(row['text'])
            print(">>> success")
        
        
        
            

if __name__ == "__main__":
    #excel_to_txt()
    pass