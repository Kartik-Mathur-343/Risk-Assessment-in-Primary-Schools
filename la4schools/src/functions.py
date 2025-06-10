
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

from imblearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import LearningCurveDisplay, ShuffleSplit
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import recall_score
import warnings

warnings.filterwarnings("ignore", category=UserWarning)



def gen_tsne(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    X_embedded = tsne.fit_transform(X_scaled)

    plt.scatter(X_embedded[:, 0], X_embedded[:, 1], alpha=0.7, c=(y==0), label="Not at Risk")
    plt.scatter(X_embedded[:, 0], X_embedded[:, 1], alpha=0.7, c=(y==1), label="At Risk")
    plt.title("t-SNE Visualization of High-Dimensional Data")
    plt.legend()
    plt.show()

def test_classifiers(X, 
                     y, 
                     print_res=False, 
                     scoring=f1_score, 
                     resampler=None, 
                     scaler=StandardScaler(), 
                     pca_ncomponents=None,
                     classifiers = None
                     ):
    if not pca_ncomponents:
        pca_ncomponents = len(X.columns)
    if not classifiers:
        classifiers = {
            "LogisiticRegression": LogisticRegression(random_state=42),
            "KNearest": KNeighborsClassifier(),
            "Support Vector Classifier": SVC(random_state=42),
            "Random Forest": RandomForestClassifier(random_state=42),
            "XG Boost": XGBClassifier(random_state=42),
            "Gaussian Naive Bayes": GaussianNB(),
        }
    scorer = make_scorer(scoring)
    scores = {}
    for key, classifier in classifiers.items():
        pipeline = Pipeline(
            [
                ("resample", resampler),
                ("scaling", scaler),
                ("pca", PCA(n_components=pca_ncomponents, random_state=42)),
                ("classifier", classifier)
            ]
        )
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        training_score = cross_val_score(pipeline, X, y, cv=cv, scoring=scorer)
        avg_score = round(np.mean(training_score), 2)
        if print_res:    
            print(
                "Classifiers: ", 
                classifier.__class__.__name__, 
                "Has a training score of", 
                avg_score
                
            )
        if not print_res:
            scores.update({classifier.__class__.__name__ : avg_score})
    if scores:
        return scores
    
def plot_pca_components(
        X, 
        y, 
        n_comp_list,
        resampler=SMOTE(random_state=42),
        scaler=StandardScaler(),
        scoring=f1_score
):
    d = {}
    for i in n_comp_list:
        accs = test_classifiers(
            X, 
            y,  
            print_res=False,
            resampler=resampler, 
            scaler=scaler,
            scoring=scoring, 
            pca_ncomponents=i
        )
        if d:
            for key in d:
                d[key].extend([accs[key]])
            
        if not d:
            d = accs
            for key in d:
                d[key] = [d[key]]
    return d

def plot_learningcurve(
        estimator, 
        X, 
        y, 
        pca_comp,
        resampler=SMOTE(random_state=42),
        cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42), 
        scaler=StandardScaler(), 
        scoring=f1_score
):
    scorer = make_scorer(scoring)
    
    common_params = {
    "X": X,
    "y": y,
    "train_sizes": np.linspace(0.1, 1.0, 5),
    "cv": cv,
    "score_type": "both",
    "n_jobs": 4,
    "line_kw": {"marker": "o"},
    "std_display_style": "fill_between",
    "score_name": "f1",
    "scoring": scorer
    }
    pipeline = Pipeline(
        [
            ("resample", resampler),
            ("scaling", scaler),
            ("pca", PCA(n_components=pca_comp, random_state=42)),
            ("classifier", estimator)
        ]
    )
    
    LearningCurveDisplay.from_estimator(pipeline, **common_params)
    plt.legend(["Training Score", "Test Score"])
    plt.title(f"Learning Curve for {estimator.__class__.__name__}")

def show_classifier_metrics(
        y,
        y_pred,
        prob_threshold=0.5,
):
    
    y_pred_thresholded = (y_pred >= prob_threshold).astype(int)
    print("accuracy_score: ", accuracy_score(y, y_pred_thresholded))
    print("recall_score: ", recall_score(y, y_pred_thresholded))
    print("f1_score: ", f1_score(y, y_pred_thresholded))
    print("classification_report: \n", classification_report(y, y_pred_thresholded))
    confusion = confusion_matrix(y, y_pred_thresholded)
    ConfusionMatrixDisplay(confusion).plot()
    plt.show()



