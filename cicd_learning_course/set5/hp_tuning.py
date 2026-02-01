import pandas as pd
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

# 1. Load Data
data = pd.read_csv("weather.csv")

# --- FIX: DROP THE DATE COLUMN ---
# This removes the column causing the "could not convert string to float" error
if 'Date' in data.columns:
    data = data.drop('Date', axis=1)
# ---------------------------------

data = data.fillna(0)

# 2. Simple encoding for other text columns (Location, WindDir, etc.)
for col in data.columns:
    if data[col].dtype == 'object' or data[col].dtype == 'string':
        data[col] = data[col].astype('category').cat.codes

# 3. Prepare Features and Target
X = data.drop('RainTomorrow', axis=1)
y = data['RainTomorrow']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1993)

# 4. Load Config
model = RandomForestClassifier()
param_grid = json.load(open("hp_config.json", "r"))

# 5. Perform GridSearch
grid_search = GridSearchCV(model, param_grid, cv=2)
grid_search.fit(X_train, y_train)

# 6. Save Results
best_params = grid_search.best_params_
with open("rfc_best_params.json", "w") as outfile:
    json.dump(best_params, outfile)

print("Best params saved.")
