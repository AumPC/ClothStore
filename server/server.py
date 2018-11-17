from flask import Flask, jsonify, request
import time 
from datetime import datetime, time
from flask_cors import CORS
import requests
import json
import matplotlib.image as mpimg

import model

import base64

app = Flask(__name__)
CORS(app)

def send_api(url, image):
    accessKey = "9b9e52ab2e420b6bb424"
    secretKey = "21d2f4c858d554bc3bcf2e1e05d5f553a7243dba"

    # access_key and secret_key
    data = {'access_key': accessKey,
    'secret_key': secretKey}

    filename = {"filename" : image}

    r = requests.post(url, files = filename, data=data)
    content = json.loads(r.content)
    return content

def save_file(data):
    import json
    with open('data.json', 'r') as readfile:
        infor = json.load(readfile)
    infor.append(data)
    with open('data.json', 'w') as outfile:
        json.dump(infor, outfile)

@app.route("/")
def home():
    return ("Execution Server")

@app.route("/send_person", methods=["POST"])
def get_person():
    command = request.form
    image = command["image"].split(",")[1]
    imgdata = base64.b64decode(image)
    filename = "person.jpg"
    with open(filename, 'wb') as f:
        f.write(imgdata)
    img=mpimg.imread(filename)
    img = img[:,:,:3]
    mpimg.imsave(filename, img)
    
    face_url = "https://face.recoqnitics.com/analyze"
    fashion_url = "https://fashion.recoqnitics.com/analyze"
    face_content = send_api(face_url, open(filename,'rb'))
    fashion_content = send_api(fashion_url, open(filename,'rb'))
    
    print("Face : " , face_content)
    print("Fashion : " , fashion_content)
    content = face_content.copy()
    for key in fashion_content:
        content[key] = fashion_content[key]
    print(content)
    with open('person.json', 'w') as outfile:
        json.dump(content, outfile)
    return "Success"

@app.route("/send_image", methods=["POST"])
def get_image():
    command = request.form
    image = command["image"].split(",")[1]
    imgdata = base64.b64decode(image)
    f = open("haha.txt", "w")
    f.write("haha")
    f.close()
    with open("count.txt", 'r') as f:
        count = int(f.read())
    filename = str(count) + '.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    img=mpimg.imread(filename)
    img = img[:,:,:3]
    mpimg.imsave(filename, img)
    
    face_url = "https://face.recoqnitics.com/analyze"
    fashion_url = "https://fashion.recoqnitics.com/analyze"
    face_content = send_api(face_url, open(filename,'rb'))
    fashion_content = send_api(fashion_url, open(filename,'rb'))
    
    print("Face : " , face_content)
    print("Fashion : " , fashion_content)
    content = face_content.copy()
    for key in fashion_content:
        content[key] = fashion_content[key]
    print(content)
    save_file(content)
    # if count % 10 == 0:
    #     model.learn()
    with open("count.txt", 'w') as f:
        f.write(str(count+1))
    return "Success"

@app.route("/suggest", methods=["POST"])
def suggest():
    return model.suggest()

if __name__ == '__main__':
    print("REST API is ready ... ")
    app.run(host='0.0.0.0', port=65520, threaded = False, use_reloader=True)        
        
        
