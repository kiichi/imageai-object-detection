# Note: use beta of coremltools
# pip install -U coremltools==5.0b3
# https://github.com/MPieter/YOLO-CoreML/blob/master/Convert/keras-coreml.py
import coremltools as ct
import tensorflow as tf


tf_keras_model = tf.keras.models.load_model("polyps/models/detection_model-ex-028--loss-0009.038.h5")
coreml_model = ct.convert(tf_keras_model,
                          inputs=[ct.ImageType(scale=1/255.0)])

coreml_model.save('ObjectDetector.mlmodel')
