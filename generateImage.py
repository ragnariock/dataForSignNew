import cv2
from random import randint
import xml.etree.cElementTree as ET

def image_genearte(ragne_images,range_sign):
	iteration = 1
	name_folder_images = 'images/'
	name_folder_sign = 'allroadsign/'
	normal_folder = 'good/'
	
	num_range = int(ragne_images / range_sign)
	second_iteration = 0 
	iter_sign = 1 

	for i in range(range_sign):
		print(i)
		for j in range(second_iteration,num_range):
			img_size_annots_h = randint(200,300) 
			img_size_annots_w = randint(200,300) 
			img_size =(600,600)
			img_size_annots = (img_size_annots_h,img_size_annots_w)
			
			image = cv2.imread(name_folder_images+str(iteration)+'.jpg')
			image_sign = cv2.imread(name_folder_sign+str(iter_sign)+'.jpg')

			new_image = cv2.resize(image,img_size)

			new_image_sign = cv2.resize(image_sign,img_size_annots)

			sign = new_image_sign
			image = new_image

			image[img_size_annots[0]:img_size_annots[0]+sign.shape[0], img_size_annots[1]:img_size_annots[1]+sign.shape[1]] = sign 
			cv2.imwrite(normal_folder+str(iteration)+'.jpg',image)
			
			img_width = img_size_annots_w
			img_height = img_size_annots_h
			img_depth = 3
			rectangles = [[img_size_annots[0],(img_size_annots[0]+sign.shape[0]),img_size_annots[1],(img_size_annots[1]+sign.shape[1])]]
			
			name = normal_folder+str(iteration)+'.jpg'
			img_filename = (name)

			root = ET.Element('annotation')
			ET.SubElement(root, 'folder').text = 'annots' # set correct folder name
			ET.SubElement(root, 'filename').text = img_filename
			size = ET.SubElement(root, 'size')

			ET.SubElement(size, 'width').text = str(img_width)
			ET.SubElement(size, 'height').text = str(img_height)
			ET.SubElement(size, 'depth').text = str(img_depth)

			ET.SubElement(root, 'segmented').text = '0'
			for box in rectangles:
			    name = "class"# class name
			    xmin = box[0] #set correct index
			    ymin = box[1] #set correct index
			    xmax = box[2] #set correct index
			    ymax = box[3] #set correct index

			    obj = ET.SubElement(root, 'object')
			    ET.SubElement(obj, 'name').text = name
			    ET.SubElement(obj, 'pose').text = 'Unspecified'
			    ET.SubElement(obj, 'truncated').text = '0'
			    ET.SubElement(obj, 'occluded').text = '0'
			    ET.SubElement(obj, 'difficult').text = '0'

			    bx = ET.SubElement(obj, 'bndbox')
			    ET.SubElement(bx, 'xmin').text = str(xmin)
			    ET.SubElement(bx, 'ymin').text = str(ymin)
			    ET.SubElement(bx, 'xmax').text = str(xmax)
			    ET.SubElement(bx, 'ymax').text = str(ymax)
			tree = ET.ElementTree(root)
			tree.write("annots/"+str(iteration)+".xml")

			iteration+=1
			num_range +=1
			second_iteration +=1
	
		iter_sign +=1

image_genearte(545,6)
