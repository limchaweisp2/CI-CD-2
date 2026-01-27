import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Source: PDF 3, Page 2 (Dataset Description)
data = pd.read_csv("weather.csv")

# Source: PDF 3, Page 4 (Data Preprocessing logic simplified)
# We fill NA and encode for the sake of the example to make it run
data = data.fillna(0)
le = LabelEncoder()
data['RainToday'] = le.fit_transform(data['RainToday'].astype(str))
data['RainTomorrow'] = le.fit_transform(data['RainTomorrow'].astype(str))

# selecting a few features mentioned in PDF 3, Page 2
features = ['MinTemp', 'MaxTemp', 'Rainfall', 'Humidity9am', 'Humidity3pm']
X = data[features]
y = data['RainTomorrow']

# Source: PDF 3, Page 6 (Train/Test Split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=1993
)

# Source: PDF 3, Page 6 (Random Forest Classifier)
clf = RandomForestClassifier(
    max_depth=2, n_estimators=50, random_state=1993
)
clf.fit(X_train, y_train)

# Source: PDF 3, Page 7 (Metrics)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
