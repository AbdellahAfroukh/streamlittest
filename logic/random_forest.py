from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import time


def train_model(data:pd.DataFrame):
    x = data.drop(['Temperature moyenne (°C)','Date'],axis=1,inplace=False)
    y = data['Temperature moyenne (°C)'].copy()
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    start_time = time.time()
    rf_model = RandomForestRegressor(n_estimators=300, random_state=42,min_samples_leaf=1,min_samples_split=3,max_depth=None)
    rf_model.fit(x_train, y_train)
    rf_train_time = time.time() - start_time
    start_time = time.time()
    y_pred = rf_model.predict(x_test)
    rf_pred_time = time.time() - start_time
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    score=rf_model.score(x_test,y_test)
    return [mse,r2,mae,rf_model,score,y_pred,rf_train_time,rf_pred_time]

def predict(model,jour,mois,precipitation,humidite,temp_moyenne_mobile,hum_moyenne_mobile):
    train_features = ['Precipitation (mm)','Humidite moyenne (%)','Jour', 'Mois','Temperature moyenne mobile','Humidite moyenne mobile']
    input_data = {
    'Jour': jour,
    'Mois': mois,
    'Precipitation (mm)': precipitation,
    'Humidite moyenne (%)': humidite,
    'Temperature moyenne mobile': temp_moyenne_mobile,
    'Humidite moyenne mobile': hum_moyenne_mobile,
    }
    input_df = pd.DataFrame([input_data])
    input_df = input_df[train_features]
    predicted_temperature = model.predict(input_df)
    return predicted_temperature