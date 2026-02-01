import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# 1. Load Data
data = pd.read_csv("weather.csv")

# 2. Fix: Drop the Date column as it's not suitable for the model as-is
if 'Date' in data.columns:
    data = data.drop('Date', axis=1)

data = data.fillna(0)

# 3. Simple encoding for text columns
for col in data.select_dtypes(include=['object', 'string', 'category']).columns:
    data[col] = data[col].astype('category').cat.codes

# 4. Prepare Features and Target
X = data.drop('RainTomorrow', axis=1)
y = data['RainTomorrow']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1993)

# 5. Grid Search
model = RandomForestClassifier()
param_grid = json.load(open("hp_config.json", "r"))

grid_search = GridSearchCV(model, param_grid, cv=2)
grid_search.fit(X_train, y_train)

# 6. Save Results
best_params = grid_search.best_params_
with open("rfc_best_params.json", "w") as outfile:
    json.dump(best_params, outfile)

print("Best params saved.")
