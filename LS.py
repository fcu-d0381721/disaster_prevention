import numpy as np
import matplotlib.pyplot as plt  # for 畫圖用
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# Import the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout



def main():
  # Import the training set
  dataset_train = pd.read_csv('./output/201801.csv')  # 讀取訓練集
  dataset_train = dataset_train[:1000]
  training_set = dataset_train.iloc[:, 11:].values  # 取「Open」欄位值
  print(training_set)
  sc = MinMaxScaler(feature_range=(0, 1))
  training_set_scaled = sc.fit_transform(training_set)
  X_train = []  # 預測點的前 60 天的資料
  y_train = []  # 預測點
  for i in range(60, 1000):
    X_train.append(training_set_scaled[i - 60:i, 0])
    y_train.append(training_set_scaled[i, 0])
  X_train, y_train = np.array(X_train), np.array(y_train)  # 轉成numpy array的格式，以利輸入 RNN

  X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
  print(X_train)
  # # Initialising the RNN
  regressor = Sequential()
  # # Adding the first LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
  regressor.add(Dropout(0.2))

  # Adding a second LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units=50, return_sequences=True))
  regressor.add(Dropout(0.2))

  # Adding a third LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units=50, return_sequences=True))
  regressor.add(Dropout(0.2))

  # Adding a fourth LSTM layer and some Dropout regularisation
  regressor.add(LSTM(units=50))
  regressor.add(Dropout(0.2))
  regressor.add(Dense(units=1))
  # Compiling
  regressor.compile(optimizer='adam', loss='mean_squared_error')

  # 進行訓練
  regressor.fit(X_train, y_train, epochs=100, batch_size=32)


  dataset_test = pd.read_csv('./output/201801.csv')
  dataset_test = dataset_test[1000:1020]
  real_stock_price = dataset_test.iloc[:, 11:].values
  dataset_total = pd.concat((dataset_train['Total'], dataset_test['Total']), axis=0)
  inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values
  inputs = inputs.reshape(-1, 1)
  inputs = sc.transform(inputs)  # Feature Scaling

  X_test = []
  for i in range(60, 80):  # timesteps一樣60； 80 = 先前的60天資料+2017年的20天資料
    X_test.append(inputs[i - 60:i, 0])
  X_test = np.array(X_test)
  X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))  # Reshape 成 3-dimension
  predicted_stock_price = regressor.predict(X_test)
  predicted_stock_price = sc.inverse_transform(predicted_stock_price)  # to get the original scale
  # Visualising the results
  plt.plot(real_stock_price, color='red', label='Real Google Stock Price')  # 紅線表示真實股價
  plt.plot(predicted_stock_price, color='blue', label='Predicted Google Stock Price')  # 藍線表示預測股價
  plt.title('Google Stock Price Prediction')
  plt.xlabel('Time')
  plt.ylabel('Google Stock Price')
  plt.legend()
  plt.show()

if __name__ == "__main__":
    main()