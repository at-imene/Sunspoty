from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage, default_storage
import os
import cv2
from .utils import utilslib as u
from tensorflow import keras
import tensorflow as tf
import numpy as np


# Create your views here.
# takes request and sends response 
# request handler
def upload_file(request):
    if request.method == "POST":
        my_uploaded_file = request.FILES['my_uploaded_file'].read() # get the uploaded file
        # do something with the file
        
        # and return the result  
        context={'filePathName':my_uploaded_file}
        return render(request,'index.html',context)          
    else:
        return render(request,'index.html') #render(request, 'index.html')
    
def dbscanAlgo(request):
    
    fileObj = request.FILES["filePath"]
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    
    img = cv2.imread(os.getcwd()+ filePathName)

    # select1 = request.POST['select1']
    input2 =  len(request.POST['input2'])==0
    input3 =  len(request.POST['input3'])==0
    input4 =  len(request.POST['input4'])==0
    if(input2 == True and input3==True and input4==True ):
        sobel_kernel = 3
        sensitivity = 70
        dbscan_eps = 45
    else:
        sobel_kernel = int(input2)
        sensitivity = int(input3)
        dbscan_eps = int(input4)

    cropped = u.croppeImage(img)
    contours = u.find_contours(cropped, sensitivity, sobel_kernel)
    contours_features, filtered_contours = u.getContoursFeatures(contours)

    if(len(contours_features)>0):
        dist = contours_features[:, :2]
        labels = u.apply_DBSCAN(dist, dbscan_eps, 1)
        num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
        wolf_number = len(labels) + num_clusters*10

    resulted_img = u.get_img_contours(cropped, dist, filtered_contours, num_clusters, labels)

    # Filename
    filename = './media/savedImage.jpg'

    # Saving the image
    cv2.imwrite(filename, resulted_img)
    context = {'a':1, 'filePathName':filePathName, 'filename': filename, 'Sunspot': len(labels), 'num_clusters': num_clusters, 'wolf': wolf_number}
    return render(request, 'index.html', context)

def classificationModel(request):
    # Load the pre-trained model
    model_path = 'models/model.h5'
    model = keras.models.load_model(model_path)
    
    fileObj = request.FILES["imageFile"]
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    
    image = cv2.imread(os.getcwd()+ filePathName, cv2.IMREAD_GRAYSCALE)
    # Resize the image to match the model's input size
    IMG_SIZE= 227
    image = cv2.resize(image, (227, 227))
    # image = image / 255.0

    # Expand dimensions to match model input shape
    X = tf.expand_dims(image, axis=0) # np.array(image).reshape(-1, IMG_SIZE, IMG_SIZE, 1)# 

    # Make the prediction
    predictions = model.predict(X)

    # Get the predicted class
    predicted_class = tf.argmax(predictions[0]).numpy()

    print("predictions: " ,predictions)
    print("predicted class: ", predicted_class)
    p_class = 'alpha'
    if predicted_class==1:
        p_class ='beta'
    elif predicted_class==2:
        p_class ='betax'

    context = {'filePathName':filePathName, 'show_classification': True, 'predicted_class': p_class, 
    'alpha': format(predictions[0, 0]*100,".2f"), 'beta': format(predictions[0, 1]*100,".2f"), 'betax': format(predictions[0,2]*100,".2f")}

    return render(request, 'classification.html', context)


def navigate_to_classification_page(request):
    return render(request, 'classification.html')

def navigate_to_help_page(request):
    return render(request, 'help.html')

def navigate_to_about_page(request):
    return render(request, 'about.html')
