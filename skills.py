import json
import pickle
import numpy as np
from PIL import Image
import tensorflow as tf
import cv2

def imagePred(img):
    image = Image.open(img)
    im =  np.asarray(image)
    im =cv2.resize(im, (224 ,224))
    im = np.expand_dims(im, axis=0)
    # im= im/255
    # model_path = "./model.pkl"
    # model = pickle.load(open(model_path,'rb'))
    model = tf.keras.models.load_model('./SVM_Tomatoleaf.h5')
    pred = model.predict(im)
    label = ['Tomato___Bacterial_spot','Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
    ans = "Mara gaya crop"
    # [[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]]
    # compare to label
    print(pred)
    for i in range(len(pred[0]) -1):
        if pred[0][i] == 1:
            ans =  label[i]
            
    
    return ans