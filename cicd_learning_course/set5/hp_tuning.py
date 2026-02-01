import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# Mock data load for example
data = pd.read_csv("weather.csv").fillna(0)
# Drop Date column
data = data.drop('Date', axis=1)

# Simple encoding
categorical_cols = data.select_dtypes(include=['object', 'string', 'category']).columns
for col in categorical_cols:
    data[col] = data[col].astype('category').cat.codes

X = data.drop('RainTomorrow', axis=1)
y = data['RainTomorrow']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1993)

# Source: PDF 5, Page 16
model = RandomForestClassifier()
param_grid = json.load(open("hp_config.json", "r"))

# Perform GridSearch
grid_search = GridSearchCV(model, param_grid, cv=2) # cv=2 for speed in demo
grid_search.fit(X_train, y_train)

# Get best params
best_params = grid_search.best_params_
with open("rfc_best_params.json", "w") as outfile:
    json.dump(best_params, outfile)

print("Best params saved.")
