import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from keras.models import Sequential, load_model

def getPredictions(filename):
    classeLabels = ['Infected', 'Healthy corn']
    labelencodernew = LabelEncoder()
    labelencodernew.fit(classeLabels)
    labelencodernew.inverse_transform([1])

    #load model
    new_model = load_model("Model/new_model22.h5")
    image_size = 300
    img_path = 'static/images/'+ filename
    img = np.asarray(Image.open(img_path).resize((image_size,image_size)))
    img = img/300

    img = np.expand_dims(img, axis=0)

    preds = new_model.predict(img)

    pred_class = labelencodernew.inverse_transform([np.argmax(preds)])[0]
    print("Diagnosis is:", pred_class)
    return pred_class

test_prediction = getPredictions('20200610_063449.jpg')