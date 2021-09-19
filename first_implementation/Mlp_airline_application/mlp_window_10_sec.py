{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://raw.githubusercontent.com/enuguru/aiandml/master/first_implementation/Mlp_airline_application/international-airline-passengers.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Multilayer Perceptron to Predict International Airline Passengers (t+1, given t)\n",
    "import numpy\n",
    "import matplotlib.pyplot as plt\n",
    "from pandas import read_csv\n",
    "import math\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# convert an array of values into a dataset matrix\n",
    "def create_dataset(dataset, look_back=1):\n",
    "\tdataX, dataY = [], []\n",
    "\tfor i in range(len(dataset)-look_back-1):\n",
    "\t\ta = dataset[i:(i+look_back), 0]\n",
    "\t\tdataX.append(a)\n",
    "\t\tdataY.append(dataset[i + look_back, 0])\n",
    "\treturn numpy.array(dataX), numpy.array(dataY)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# fix random seed for reproducibility\n",
    "numpy.random.seed(7)\n",
    "# load the dataset\n",
    "dataframe = read_csv('https://raw.githubusercontent.com/enuguru/aiandml/master/first_implementation/Mlp_airline_application/international-airline-passengers.csv', usecols=[1], engine='python', skipfooter=3)\n",
    "dataset = dataframe.values\n",
    "dataset = dataset.astype('float32')\n",
    "# split into train and test sets\n",
    "train_size = int(len(dataset) * 0.67)\n",
    "test_size = len(dataset) - train_size\n",
    "train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# reshape into X=t and Y=t+1\n",
    "look_back = 1\n",
    "trainX, trainY = create_dataset(train, look_back)\n",
    "testX, testY = create_dataset(test, look_back)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create and fit Multilayer Perceptron model\n",
    "model = Sequential()\n",
    "model.add(Dense(8, input_dim=look_back, activation='relu'))\n",
    "model.add(Dense(1))\n",
    "model.compile(loss='mean_squared_error', optimizer='adam')\n",
    "model.fit(trainX, trainY, epochs=200, batch_size=2, verbose=2)\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Estimate model performance\n",
    "trainScore = model.evaluate(trainX, trainY, verbose=0)\n",
    "print('Train Score: %.2f MSE (%.2f RMSE)' % (trainScore, math.sqrt(trainScore)))\n",
    "testScore = model.evaluate(testX, testY, verbose=0)\n",
    "print('Test Score: %.2f MSE (%.2f RMSE)' % (testScore, math.sqrt(testScore)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# generate predictions for training\n",
    "trainPredict = model.predict(trainX)\n",
    "testPredict = model.predict(testX)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# shift train predictions for plotting\n",
    "trainPredictPlot = numpy.empty_like(dataset)\n",
    "trainPredictPlot[:, :] = numpy.nan\n",
    "trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict\n",
    "# shift test predictions for plotting\n",
    "testPredictPlot = numpy.empty_like(dataset)\n",
    "testPredictPlot[:, :] = numpy.nan\n",
    "testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# plot baseline and predictions\n",
    "plt.plot(dataset)\n",
    "plt.plot(trainPredictPlot)\n",
    "plt.plot(testPredictPlot)\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
