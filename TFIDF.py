import numpy as np
from scipy import sparse as sp
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
import matplotlib.pyplot as plt

# Storing the training data as features and lables
train_X = np.loadtxt("/Users/Arun/Desktop/BDAssign2/train.data")
train_Y = np.loadtxt("/Users/Arun/Desktop/BDAssign2/train.label")

# Storing the test data as features and lables
test_X = np.loadtxt("/Users/Arun/Desktop/BDAssign2/test.data")
test_Y = np.loadtxt("/Users/Arun/Desktop/BDAssign2/test.label")

# Splitting train.data file into document id, word id and word count.
k=11269
l=61188
doc = train_X[:,0]-1
word = train_X[:,1]-1
count = train_X[:,2]
print max(doc)
print max(word)
print max(count)

# Splitting test.data file into document id, word id and word count.
doc_t = test_X[:,0]-1
word_t = test_X[:,1]-1
count_t = test_X[:,2]
print max(doc_t)
print max(word_t)
print max(count_t)

# Creating sparse matrix with maximum dimension, to avoid dimension miss-match error
sp_mat = sp.coo_matrix((count,(doc,word)),(k, l))
sp_mat = sp_mat.tocsr()
sp_mat_t = sp.coo_matrix((count_t, (doc_t, word_t)))
sp_mat_t = sp_mat_t.tocsr()

# Conveting the sparse matrix of train data into TFIDF values
tfidf = TfidfTransformer()
tfidf_res = tfidf.fit_transform(sp_mat)

# Conveting the sparse matrix of test data into TFIDF values
tfidf_t = TfidfTransformer()
tfidf_res_t = tfidf_t.fit_transform(sp_mat_t)

# Training and predicting using Multimodal Naive Bayes as the TFIDF values are continuous
clf = MultinomialNB()
clf.fit(tfidf_res, train_Y)
pred = clf.predict(tfidf_res_t)
print pred

# Calculating accuracy score and displaying confusion matrix
print "Accuracy Score"
print(accuracy_score(test_Y, pred))
print confusion_matrix(test_Y, pred)

# ROC and AUC
fpr, tpr, thresholds = metrics.roc_curve(test_Y, pred, pos_label=20)
print metrics.auc(fpr, tpr)
plt.plot(fpr, tpr, color='darkorange',lw = 2, label = "ROC")
plt.plot([0,1],[0,1],color = 'navy', lw = 2, linestyle = '--')
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC')
plt.legend(loc="lower right")
plt.show()
