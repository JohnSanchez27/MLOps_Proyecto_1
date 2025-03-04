import tensorflow as tf
import tensorflow_transform as tft

def preprocessing_fn(inputs):
    """Función de preprocesamiento para transformar los datos de entrada."""

    outputs = {}

    # 1. Normalización Min-Max para características numéricas
    numerical_features = ['Elevation', 'Slope', 'Horizontal_Distance_To_Hydrology',
                          'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
                          'Hillshade_9am', 'Hillshade_Noon', 'Horizontal_Distance_To_Fire_Points']

    for feature in numerical_features:
        outputs[feature] = tft.scale_by_min_max(tf.cast(inputs[feature], tf.float32))
    
    # 2. Transformar 'Soil_Type' en índices de vocabulario
    outputs['Soil_Type'] = tft.compute_and_apply_vocabulary(inputs['Soil_Type']) 
     # 3. Transformar 'Soil_Type' en índices de vocabulario
    outputs['Wilderness_Area'] = tf.one_hot(tft.compute_and_apply_vocabulary(inputs['Wilderness_Area']), depth=4)
    # 4. Mantener la etiqueta 'Cover_Type' sin cambios
    outputs['Cover_Type'] = inputs['Cover_Type']

    return outputs
