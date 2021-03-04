import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import debug

def predict_website(url,classifier):
    url1 = r'{}'.format(url)
    feature = debug.features(url1)
    f= np.array(feature).reshape(1, -1)
    y_pred = classifier.predict(f)
    return y_pred