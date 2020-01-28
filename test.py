from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import face_recognition
import keras
from keras.models import load_model
import cv2
import json

#Face Detection

image = face_recognition.load_image_file("simon.jpg")
face_locations = face_recognition.face_locations(image)


output_dict = {"face_present": "", "label": ""}

top, right, bottom, left = face_locations[0]
face_image1 = image[top:bottom, left:right]
image_save = Image.fromarray(face_image1)
image_save.save("image_1.jpg")


"""
top1, right1, bottom1, left1 = face_locations[1]
face_image2 = image[top1:bottom1, left1:right1]
plt.imshow(face_image2)
image_save = Image.fromarray(face_image2)
image_save.save("image_2.jpg")
"""


#Emotion Detection

emotion_dict = {'Angry': 0, 'Sad': 5, 'Neutral': 4,
                'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}
         

face_image = cv2.imread("image_1.jpg")
face_image = cv2.resize(face_image, (48,48))
face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])


model = load_model("emotion_detector_models/model_v6_23.hdf5")
predicted_class = np.argmax(model.predict(face_image))

label_map = dict((v, k) for k, v in emotion_dict.items())
predicted_label = label_map[predicted_class]

output_dict["label"] = predicted_label
if len(face_locations):
  output_dict["face_present"] = True


json_string = json.dumps(output_dict)

with open('json_file.json', 'w') as f:
  json.dump(output_dict, f)

"""
plt.imshow(face_image)
plt.show()
"""
