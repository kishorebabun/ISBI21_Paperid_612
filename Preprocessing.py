# organize imports
import os
import glob
import datetime
import shutil
# print start time
print ("[INFO] program started on - " + str(datetime.datetime.now))

# get the input and output path
input_path  = '/home/kbabu89/NewCodeUsing PreTrained Model/jpg1/'
output_path = '/home/kbabu89/NewCodeUsingPreTrainedModel/dataset1/train'

# get the class label limit
class_limit =8 

# take all the images from the dataset
image_paths = glob.glob('/home/kbabu89/NewCodeUsingPreTrainedModel/jpg1/*.jpg')

# variables to keep track
label = 0
i = 0
j = 90

# flower17 class names ---for Flower problem






#lesion 8 class names ---for lesion problem
class_names = ["actinic", "basal", "derma", "mela", "nev","pig", "squam", "vas"]



#os.system("copy " + original_path + " " + cur_path + image_path)
# change the current working directory
os.chdir(output_path)

# loop over the class labels
for x in range(1, class_limit+1):
	# create a folder for that class
	os.system("mkdir " + class_names[label])
	# get the current path
	cur_path = output_path + "/" + class_names[label] + "/"
	# loop over the images in the dataset
	for image_path in image_paths[i:j]:
		original_path = image_path
		image_path = image_path.split("/")
		image_path = image_path[len(image_path)-1]
		shutil.copy(original_path, cur_path+image_path)   
	i += 90
	j += 90
	label += 1

# print end time
print ("[INFO] program ended on - " + str(datetime.datetime.now))


    
