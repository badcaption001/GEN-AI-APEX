# -*- coding: utf-8 -*-
"""day2 genai.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/123spNAVzUQsZR7TdFxm7E7TRKdRcYlrl
"""

import json
json.load(open("/content/states_india.geojson"))

data=json.load(open("/content/states_india.geojson"))

type(data)

data['features'][0].keys()

data['features'][0]['properties']

dict["Telangana"]

state=[]
state_code=[]

for i in range(32):
  #state.append(data['features'][i]['properties']['st_nm'])
  #state_code.append(data['features'][i]['properties']['state_code'])
  print(data['features'][i]['properties']['st_nm'])
  print(data['features'][i]['properties']['state_code'])

import pandas as pd

for i in range(32):
  state.append((data['features'][i]['properties']['st_nm']))

state

for i in range(32):
  state_code.append((data['features'][i]['properties']['state_code']))

state_code

!pip install openai==0.28

import openai

openai.api_key="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"

openai_models = openai.Model.list()

type(models.data)

openai_models.data[1].id

print(openai_models.data[2].id)

engine_modles="gpt-3.5-turbo"

!pip install   -q -U google-generativeai

import google.generativeai as genai

genai.configure(api_key="AIzaSyBipcQrM5yq-_r63gDZFm9A9R6IbJlQPMg")

for i in genai.list_models():
  print(i.name)

models=genai.GenerativeModel("gemini-pro")

res=models.generate_content("what is ARPANE")
print(res)