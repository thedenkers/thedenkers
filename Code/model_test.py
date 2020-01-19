def predict_image(imag):
    import os
    import tensorflow as tf
    import numpy as np
    from tensorflow import keras

    # from tensorflow.keras import layers
    # from tensorflow.keras import Model
    #

    # os.chdir('D:\PycharmProjects\SIH\Tensorflow_models')
    new_model = keras.models.load_model('Tensorflow_models/rps20Class4.h5')

    # Show the model architecture
    # new_model.summary()

    sizeImg = 150
    # import numpy as np

    from keras.preprocessing import image
    # import tensorflow_core.keras


    # listofDir = os.listdir('/content/gdrive/My Drive/SIH2020 The_Denkers/Dataset/output3/train')
    listOfDir=['Nanuz Fort','Beach', 'Basilica of Bom Jesus', 'Fort Aguada', 'Chapora Fort', 'Dudhsagar Falls, Goa', 'Mangeshi Temple', 'Dona Paula', 'Se Cathedral', 'Reis Magos Fort', 'Shri Shantadurga Temple', 'Church Of St Augustine', 'Cabo De Rama Fort', 'Mormugao Fort', 'Arvalem Waterfalls', 'Fort Tiracol', 'Church of St. Cajetan', 'Butterfly Conservatory Of Goa', 'Sri Mahadeva Temple','Anjdiv Fort']
    listOfDir.sort()
    # img=tf.io.decode_base64(imag)



    # predicting imagesr
    path =f'{imag}'
    img = image.load_img(path, target_size=(sizeImg, sizeImg))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = new_model.predict(images, batch_size=10)


    print(classes)

    print(listOfDir[np.argmax(classes[0])])
    return np.argmax(classes[0])