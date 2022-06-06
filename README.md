
# Intel Image Classification
This project is about creating a cnn model able to classify an image into one of the following categories:  
* Buildings  
* Forest  
* Glacier
* Mountain
* Sea
* Street
 
Details about the dataset used can be found [here](https://www.kaggle.com/datasets/puneet6060/intel-image-classification).  
We built a streamlit app that, given an image (drag and drop), tells you to which from the above categories the image belongs too.  
Additionally, the app can receive a folder of mixed images, creates subfolders into which to classify the images.

# Requirements
* streamlit
* pytorch
* torchvision
* Pillow
* os
* shutil

# How to use the app
1) Single image classification
 After launching the streamlit app, drag and drop and image to receive a prediction of the class the app thinks its belongs to
 
3) Multiple images classification
 * Provide the source folder (path) where all the images are located
 * Provide the destination folder name (path) where the classified images should be copy

 It is worth mentioning that the app doesn't delete the source folder to avoid unintentionally deleting important files. 
 For a safer approach, the user can manually delete the source folder after images have been classified.
