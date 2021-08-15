import glob
#from imageai.Detection import ObjectDetection
from imageai.Detection.Custom import CustomObjectDetection
#detector = ObjectDetection() 
detector = CustomObjectDetection() #Use Custome One !
detector.setModelTypeAsYOLOv3()
detector.setModelPath("polyps/models/detection_model-ex-013--loss-0011.413.h5")
detector.setJsonPath("polyps/json/detection_config.json") # need this for custom model
detector.loadModel()

folders = ["polyps/preview/positive/","polyps/preview/negative/"]
for folder in folders:
	files = glob.glob(folder + "input/*.jpg")
	for file_path in files:
		print(file_path)
		detections = detector.detectObjectsFromImage(input_image=file_path, output_image_path=file_path.replace("input","output"))
