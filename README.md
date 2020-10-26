Dataset: 
 Dataset used is International Skin Imaging Collaboration (ISIC) Challenge dataset, from which 760 images collected and divided into 8 classes and each class is having 90 images with 224x224 dimensions. 90% of images used for training and 10% of images are used for testing.

Python Code implementation:
It includes mainly three modules of python code implementations. They are
1.	Preprocessing.py
It deals with dividing the data into classes and augmentation, scaling and resizing.
2.	Extract_Features.py
It deals with extraction of features from images automatically with the help of pre-trained models like Mobile Net, ResNet, Vgg19, etc.
3.	Training.py
It deals with classification, metrics and evaluation using Confusion matrix.
