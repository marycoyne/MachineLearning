import numpy as np
import jsonlines

reviewTexts = []
posiRev = []
eaRev = []

with open("reviews_36.jl.txt", "rb") as f:
    for item in jsonlines.Reader(f):
        reviewTexts.append(item["text"])
        posiRev.append(item["voted_up"])
        eaRev.append(item["early_access"])

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

#part i
# kNN

X = vectorizer.fit_transform(reviewTexts)
X = np.array(X.toarray())
y = np.array(posiRev)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold

kf = KFold(n_splits=5)

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    neigh = KNeighborsClassifier(n_neighbors=6)
    neigh.fit(X_train, y_train)
    print(neigh.score(X_test, y_test))

# logistic regression
    
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression

kf = KFold(n_splits=5)
logmodel = LogisticRegression()

for train_index, test_index in kf.split(X):
    print("Train Index: ", train_index, "\n")
    print("Test Index: ", test_index)
    
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    logmodel.fit(X_train,y_train)
    score = logmodel.score(X_test, y_test)
    
    print("Score: ", score)
    print("\n")
    
#predictions = logmodel.predict(X_test)
