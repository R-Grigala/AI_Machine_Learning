import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error, r2_score

# import datasaet from csv file, store it as pandas dataframe
data1 = pd.read_csv('Netflix.csv')

# make sure that Date elements are datetime objects not just strings
print('Date object type:', type(data1['Date'][0]))

data1['Date'] = pd.to_datetime(data1['Date'])
data1.set_index('Date', inplace=True)

# Select features (X) and target (y) - here 'Close' is the target
X = data1.drop(columns=['Close'])
y = data1['Close']

#prepare datasets for modle training/testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)

#model1 = LinearRegression()
#model1 = DecisionTreeRegressor()
model1 = RandomForestRegressor(n_estimators=25, random_state=42)

# train the model
model1.fit(X_train, y_train)

# Make predictions
predict = model1.predict(X_test)

# seperate dataset to compare model prediction and test dataset values
compare = pd.DataFrame({'real': y_test, 'predicted' : predict})
compare['error'] = (compare['real'] - compare['predicted']).round(10)

# Calculate performance metrics
mse = mean_squared_error(y_test, predict)
r2 = r2_score(y_test, predict)
    
print(f"{type(model1).__name__} - Mean Squared Error: {mse:.5f}, R^2 Score: {r2:.5f}")












