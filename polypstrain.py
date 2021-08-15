from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()

trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="polyps")
trainer.setTrainConfig(object_names_array=["polyp"], batch_size=4, num_experiments=30)

# In the above,when training for detecting multiple objects,
#set object_names_array=["object1", "object2", "object3",..."objectz"]

trainer.trainModel()
