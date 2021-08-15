# kiichi
import json
import shutil
import os

f = open('polyps-original/bounding-boxes.json')
data = json.load(f)
f.close()
list = []
for key in data.keys():
	item = {}
	item['image'] = key+'.jpg'
	item['annotations'] = []
	bbox = data[key]['bbox']
	for box in bbox:
		label = box['label']
		x = box['xmin']
		y = box['ymin']
		width = box['xmax'] - box['xmin']
		height = box['ymax'] - box['ymin']
		print(key, label, x, y, width, height)
		rect = {
			'label':label,
			'coordinates':{
				'x':x,
				'y':y,
				'width':width,
				'height':height
			}
		}
		item['annotations'].append(rect)
	list.append(item)

folders = ['train','validation']
datasets = {
	'train':list[0:850],
	'validation':list[850:1000]
}
for folder in folders:
	folder_path = 'polyps/' + folder
	if os.path.exists(folder_path):
		shutil.rmtree(folder_path)
	os.mkdir(folder_path)
	os.mkdir(folder_path+'/images')
	os.mkdir(folder_path+'/annotations')
	# dumping CreateML based annotation.json file for index.html preview purpose anyways
	with open(folder_path + '/annotations.json', 'w') as outfile:
		json.dump(datasets[folder], outfile)
		jsonstr = json.dumps(datasets[folder])
		htmlstr = ''
		with open('index.html', 'r') as htmlfile:
			htmlstr = htmlfile.read() 
			htmlstr = htmlstr.replace('{{{LIST}}}', jsonstr)
		with open(folder_path + '/index.html', 'w') as htmlout:
			htmlout.write(htmlstr)
		for item in datasets[folder]:
			shutil.copyfile('polyps-original/images/'+item['image'], folder_path+'/images/'+item['image'])
			with open('template.xml','r') as xmlfile:
				xmlstr = xmlfile.read()
				xmlstr = xmlstr.replace('{{{FILENAME}}}',item['image'])
				xmlstr = xmlstr.replace('{{{PATH}}}',folder_path+'/images/'+item['image'])
				coord = item['annotations'][0]['coordinates']
				xmlstr = xmlstr.replace('{{{WIDTH}}}', str(coord['width']))
				xmlstr = xmlstr.replace('{{{HEIGHT}}}', str(coord['height']))
				xmlstr = xmlstr.replace('{{{XMIN}}}', str(coord['x']))
				xmlstr = xmlstr.replace('{{{YMIN}}}', str(coord['y']))
				xmlstr = xmlstr.replace('{{{XMAX}}}', str(coord['x'] + coord['width']))
				xmlstr = xmlstr.replace('{{{YMAX}}}', str(coord['y'] + coord['height']))
				xmlstr = xmlstr.replace('{{{NAME}}}','polyp')
				with open(folder_path+ '/annotations/' + item['image'].replace('.jpg','.xml'), 'w') as xmlout:
					xmlout.write(xmlstr)
