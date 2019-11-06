import re
import os
import cv2

num = 1

width = 200
height = 200
dim = (width, height)


for root, dirs, files in os.walk(".", topdown=False):
	for name in range(len(files)):
		#print(os.path.join(root, name))
		nameImage = os.path.join(root,files[name])
		nameImage = str(nameImage)
		name_root = str(root)
		if re.search(r'allroadsign',name_root):
			if (r'jpg',nameImage ) or re.search(r'jpeg',nameImage) or re.search(r'png',nameImage) or re.search(r'JPG',nameImage):
				img = cv2.imread(nameImage)

				resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

				cv2.imwrite('allroadsign/'+str(num) + '.jpg', resized )
				num +=1

print(num)
