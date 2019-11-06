# print(original_image.shape)
# (720, 1280,3)

# rectangles = [[100,200,40,100],[200,400,80,170]] 
# labels = [0,1]


img_width = 500
img_height = 500
img_depth = 3
img_filename = "example.jpg"


rectangles = [[100,200,40,100],[200,400,80,170]] 

import xml.etree.cElementTree as ET

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
tree.write("annots/1.xml")
