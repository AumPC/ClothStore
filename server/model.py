import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def get_mapper(data):
      mapper = {"Nothing" : -1}
      for datum in data:
            if datum not in mapper:
                  mapper[datum] = len(mapper) - 1
      return mapper

def map(data, mapper):
      result = []
      for datum in data:
            if datum in mapper:
                  result.append(mapper[datum])
            else:
                  result.append(mapper["Nothing"])
      return result
    
def find_max_from_complex_dict(data, compare, target):
      c_max = ""
      v_max = 0
      for d in data:
            if d[compare] > v_max:
                  v_max = d[compare]
                  c_max = d[target]
      return c_max
      
def extract_feature(content):
      feature = {}
      if content["faces"] != []:
            data = content["faces"][0]
            feature["age"] = [data["age"]]
            feature["emotions"] = [max(data["emotions"], key=data["emotions"].get)]
            feature["gender"] = [data["gender"]["value"]]
            feature["color"] = [find_max_from_complex_dict(content["person"]["colors"], "ratio", "colorName")]
            feature["garment"] = [find_max_from_complex_dict(content["person"]["garments"], "confidence", "typeName")]
            feature["style"] = [find_max_from_complex_dict(content["person"]["styles"], "confidence", "styleName")]
            add_random_value(feature)
      return feature

def add_random_value(data):
      data["product_no"] = [random.randint(1,10)]
      return data

def learn():
      import json
      with open('data.json', 'r') as readfile:
            infor = json.load(readfile)
      
      train = {"age":[], "emotions":[], "gender":[], "color":[], "garment":[], "style":[], "product_no":[]}
      from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
      for d in infor:
            e = extract_feature(d)
            for key in e:
                  train[key] += e[key]
      
      train = pd.DataFrame(train)
      
      for key in train:
            mapper = get_mapper(train[key])
            train[key] = map(train[key], mapper)
      train_y = train["product_no"]
      train_x = train.drop(["product_no"], axis=1)
      
      rfr = RandomForestClassifier()
      rfr.fit(train_x, train_y)

      save_model(rfr, "rfr")

def suggest():
      return "Suggest"



