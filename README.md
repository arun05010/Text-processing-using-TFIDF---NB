# Text processing using TFIDF

The 20 newsgroups basically contain 7505 articles categorized into 20 different fields. Train has all the 20 topics and its respective ids. Train label contains the class label of all the 7505 documents. Train data contains document id, word id and word count. Similar data are available in test map, label and data, which are used to test the classifier, while the previous is used to train the classifier.

Here TFIDF and Multimodal Naive Bayes are used to text processing.

In Text Processing, TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection.

A sparse matrix is created and the matrix is fed as input to Tfidftransformer() fuction. Now the document is represented interm of TFIDF.

Naive Bayes classifier is now applied to predict the labels.
