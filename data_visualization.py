import matplotlib.pyplot as plt
import os 
from keras_preprocessing.image import load_img

#Displaying images
# size of the image: 48*48 pixels
pic_size = 48

# input path for the images
base_path = "C:\\Users\\arvin\\OneDrive\\Desktop\\Mini-Project\\images\\"

plt.figure(0, figsize=(12,20))
cpt = 0

for expression in os.listdir(base_path + "train/"):
    for i in range(1,6):
        cpt = cpt + 1
        plt.subplot(7,5,cpt)
        img = load_img(base_path + "train/" + expression + "/" +os.listdir(base_path + "train/" + expression)[i], target_size=(pic_size, pic_size))
        plt.imshow(img, cmap="gray")

plt.tight_layout()
plt.show()