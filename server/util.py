import pickle
import numpy as np
from warnings import filterwarnings 
filterwarnings("ignore")

__scaler = None
__model = None

def return_model():
    return __model

def predict_yearly_spent(avg_session_length,time_on_app,time_on_website,length_of_membership):
    x = np.array([avg_session_length,time_on_app,time_on_website,length_of_membership],ndmin=2)
    x_scaled = __scaler.transform(x)
    return round(__model.predict(x_scaled)[0],2)

def load_saved_artifacts():
    print("Loading Saved Artifacts...")
    global __model
    global __scaler
    with open("D:\\Ecommerce Predictor\\model\\rg.pickle",'rb') as f:
        __model = pickle.load(f)

    with open("D:\\Ecommerce Predictor\\model\\scaler.pickle",'rb') as f:
        __scaler = pickle.load(f)
    print("Done...")


if __name__ == "__main__":
    load_saved_artifacts()

    print(predict_yearly_spent(33.715981,12.418808,35.771016,2.735160))
       