import requests # pip install requests
import json     # pip install json

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# Path of image (jpg/jpeg/png)
file = "pretty image.png"

img=mpimg.imread(file)
img = img[:,:,:3]

mpimg.imsave("haha.jpg", img)

imgplot = plt.imshow(img)
plt.show()
# url name
url = "https://face.recoqnitics.com/analyze"
accessKey = "9b9e52ab2e420b6bb424"
secretKey = "21d2f4c858d554bc3bcf2e1e05d5f553a7243dba"
# access_key and secret_key
data = {'access_key': accessKey,
  'secret_key': secretKey}

filename = {'filename': open("haha.jpg",'rb')}
print(filename)
r = requests.post(url, files = filename, data=data)
print(r.content)
content = json.loads(r.content)
print(content)