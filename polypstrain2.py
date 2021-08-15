# other example to continue from pre-trained model.
# this shows the bigger batch size which causes a bit more random walk 
# but it should approach the result quicker using more memory.
# try experiments like 100 or more? watch the loss function value though
# model file size difference ? in batch_size 4 v.s. 32?
from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()

trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="polyps")
trainer.setTrainConfig(object_names_array=["polyp"], batch_size=32, num_experiments=100
, train_from_pretrained_model='polyps/models/detection_model-ex-013--loss-0011.413.h5')
trainer.trainModel()
