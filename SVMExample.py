########## Simple Example
# Importing required libraries

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Loading and exploring our dataset
iris = datasets.load_iris()
#print(iris) #Not use head()

# Splitting our data
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42)

# Model SVM
clf = svm.SVC(kernel='linear')

# Traing modelpre
clf.fit(X_train, y_train)

# Predict
predictions = clf.predict(X_test)

# Measure the accuracy
print("Precisión:", accuracy_score(y_test, predictions))