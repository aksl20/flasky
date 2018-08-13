from keras.models import load_model

def load_model(model, weights='../statics/models/weights.h5'):

    model = load_model('../statics/models/weights.h5')
    
    return model

