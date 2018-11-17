import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
<<<<<<< HEAD

with open("data.json", "r") as f:
    import json
    d = json.load(f)
=======
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
>>>>>>> master
    
def find_max_from_complex_dict(data, compare, target):
      c_max = ""
      v_max = 0
      for d in data:
            if d[compare] > v_max:
                  v_max = d[compare]
                  c_max = d[target]
      return c_max
      
<<<<<<< HEAD

def extract_feature(content):
      if content["faces"] != []:
            feature = {}
            data = content["faces"][0]
            feature["age"] = data["age"]
            feature["emotions"] = max(data["emotions"], key=data["emotions"].get)
            feature["gender"] = data["gender"]["value"]
            feature["color"] = find_max_from_complex_dict(content["person"]["colors"], "ratio", "colorName")
            feature["garment"] = find_max_from_complex_dict(content["person"]["garments"], "confidence", "typeName")
            feature["style"] = find_max_from_complex_dict(content["person"]["styles"], "confidence", "styleName")
      return feature
            
            
feature = extract_feature(d[203])
# from sklearn.model_selection import train_test_split
# train_x, valid_x, train_y, valid_y = train_test_split(train_x, train_y, test_size=0.1, shuffle=False)

# import keras 
# from keras.models import Sequential, Input, Model
# from keras.layers import Dense, Dropout
# from keras.layers.normalization import BatchNormalization
# from keras.layers.advanced_activations import LeakyReLU

# batch_size = 12
# epochs = 5

# #Add network
# model = Sequential()
# model.add(Dense(1000 ,input_shape=(train_x.shape[1],), activation='linear'))
# model.add(Dropout(0.2))
# model.add(LeakyReLU(alpha=0.1))
# model.add(Dense(500, activation='linear'))
# model.add(Dropout(0.2))
# model.add(LeakyReLU(alpha=0.1))
# model.add(Dense(100, activation='linear'))
# model.add(Dropout(0.2))
# model.add(LeakyReLU(alpha=0.1))
# model.add(Dense(train_y.shape[1], activation='linear'))

# model.compile(loss=keras.losses.mean_absolute_error, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

# model.summary()

# try:
#     from keras.models import load_model
#     model = load_model("models/ANN.h5py")
#     print("Load model")
# except:
#     print("There's no model")

# train_x = np.array(train_x)
# train_y = np.array(train_y)
# valid_x = np.array(valid_x)
# valid_y = np.array(valid_y)

# model_train = model.fit(train_x, train_y, batch_size=batch_size,epochs=epochs,verbose=1, validation_data=(valid_x, valid_y))
# model.save("models/ANN.h5py")
=======
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



>>>>>>> master
