import openai

import os
from utilities.tools import hasherUsername, timeDateWithBreak, get_cfg


def genCode(message):
    cfg = get_cfg()

    if message == None:
        querry_str = cfg['userinfo']['defaultUserMessage']
    else:
        querry_str = message

    userencoded = hasherUsername(cfg['userinfo']['name'])
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if openai.api_key == None:
        openai.api_key = cfg['userinfo']['apiKey']

# https://platform.openai.com/docs/api-reference/completions/create
    print('querry str: ' + querry_str)
    response = openai.Completion.create(
    model="code-davinci-002",
    prompt="<|endoftext|>"+querry_str+"\n--\nLabel:",
    temperature=0.2,
    max_tokens=1000,
    top_p=0.2,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    user = userencoded
    )
    r_id = response.id
    r_obj = response.object
    r_cre = response.created
    r_mod = response.model
    r_us = response.usage
    r_cho = response.choices
    #"finish_reason": "length",
    #"index": 0,
    #"logprobs": null,
    #"text": " Vue.js\n\n"
    res_text =r_cho[0].text
    print(r_cho)

    if r_cho[0].finish_reason != "length":
        f=open("results/"+timeDateWithBreak("_")+".txt","w")
        f.write(res_text)
        print(res_text)
        f.close()
    else:
        f=open("results/"+timeDateWithBreak("_")+".txt","w")
        f.write('len#!')
        f.write(res_text)
        print(res_text)
        f.close()
def engines():
    b = openai.Engine.list()
    print(b)