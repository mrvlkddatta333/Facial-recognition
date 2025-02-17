from preprocessing import *
import numpy as np
from sklearn.preprocessing import Normalizer, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle


root_url = os.path.join(os.path.abspath(os.path.dirname(__file__)),'MTCNN') #Change root_url according to computer directory

# data  = np.load(os.path.join(root_url,"model/Face-dataset-embedding.npz"))

# X_train , y_train , X_test, y_test = data["a"], data["b"], data["c"], data["d"]
def encoder(X_train , y_train , X_test, y_test):
    """
    Encoder dataset loaded from npz for classifing
    """
    in_encoder = Normalizer(norm='l2')
    X_train_encode = in_encoder.transform(X_train)
    X_test_encode = in_encoder.transform(X_test)
    
    out_encoder = LabelEncoder()
    out_encoder.fit(y_train)
    y_train_encode = out_encoder.transform(y_train)
    y_test_encode = out_encoder.transform(y_test)
    return X_train_encode, y_train_encode, X_test_encode, y_test_encode

# if __name__ == "__main__":
    # X_train_encode, y_train_encode, X_test_encode, y_test_encode = encoder()
    # #SVM classifier
    # model = SVC(kernel='linear', probability= True, random_state = 42)
    # model.fit(X_train_encode, y_train_encode)

    # yhat_train = model.predict(X_train_encode)
    # yhat_test = model.predict(X_test_encode)

    # # print(yhat_train)
    # # print(yhat_test)

    # score_train = accuracy_score(y_train_encode, yhat_train)
    # score_test = accuracy_score(y_test_encode, yhat_test)

    # print("Accuracy on train set: {}".format(score_train))
    # print("Accuracy on test set: {}".format(score_test))
    # #Save model
    # filename = os.path.join(root_url,"model/classify.sav")
    # pickle.dump(model, open(filename, 'wb'))



