from Extract import extractor
from config import API_KEY
import openai

openai.api_key=API_KEY

def OAI_connect(prompt):
    completion = openai.Completion.create(
        engine="babbage-002",
        prompt=prompt)
    return completion.choice[0].message  
    

def get_file():
    file_path=r"C:\Users\Ashok kumar\Downloads\Rough\test.tmp" #extractor()
    with open(file_path,'r') as f:
        message=f.read()
    return message

def call():
    message=get_file()
    ans=OAI_connect(message)
    print(ans)

if __name__=='__main__':
    call()    
    

