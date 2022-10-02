
# Intel Image Classification
This project is about creating a cnn model able to classify an image into one of the following categories:  
* Buildings  
* Forest  
* Glacier
* Mountain
* Sea
* Street  

The project is a joint effort between [Andrea](https://github.com/AndreaViviani89), [Ritthuja](https://github.com/RitthujaKandasamy) and I; it's a challenge given to us during our learning journey at Epicode.  Thanks guys for this great time working together :)!!!   
 
Details about the dataset used can be found [here](https://www.kaggle.com/datasets/puneet6060/intel-image-classification).  
We built a streamlit app that, given an image (drag and drop), tells you to which from the above categories the image belongs too.  
Additionally, the app can receive a folder of mixed images, creates subfolders into which to classify the images.

![final_629e3752eefef9009be2b12a_308736](https://user-images.githubusercontent.com/100673761/172317731-d8185c8b-f3d3-4d45-b0f7-be79b4306cba.gif)


# Requirements
* streamlit
* pytorch
* torchvision
* Pillow
* os
* shutil

# How to use the app
1) *Single image classification*  
 After launching the streamlit app, drag and drop an image to receive a prediction of the class the app thinks its belongs to.
 
3) *Multiple images classification*  
 * Provide the source folder (path) where all the images are located
 * Provide the destination folder name (path) where the classified images should be copy

 It is worth mentioning that the app doesn't delete the source folder to avoid unintentionally deleting important files. 
 For a safer approach, the user can manually delete the source folder after images have been classified.
 
![Accuracy](https://user-images.githubusercontent.com/100673761/172314868-48ccf9d6-41eb-4739-803c-5fa33fafc75b.gif)

