import openai

import os
from utilities.tools import hasherUsername, timeDateWithBreak
from configparser import ConfigParser

def get_cfg():
    file = 'config.cfg'
    cfg = ConfigParser()
    cfg.read(file)
    print(cfg['userinfo']['apiKey'])
def genCode(message):
    if message == None:
        querry_str = "create html page for website developer with javascript animations"
    a = "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"
    user = "HeavyKisielPayne"
    userencoded = hasherUsername(user)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = a

# https://platform.openai.com/docs/api-reference/completions/create
    response = openai.Completion.create(
    model="code-davinci-002",
    prompt="<|endoftext|>"+querry_str+"\n--\nLabel:",
    temperature=1.0,
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
        f.close()
    else:
        f=open("results/"+timeDateWithBreak("_")+".txt","w")
        f.write('len#!')
        f.write(res_text)
        f.close()
def engines():
    b = openai.Engine.list()
    c = openai.Image.create()
    print(b)