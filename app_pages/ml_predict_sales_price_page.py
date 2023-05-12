import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.file_management import load_clean_data, load_pkl_file
from src.eval_pipeline_perf import rgs_performance
from src.eval_pipeline_perf import rgs_evaluation_plots


def ml_predict_sales_price_page_body():

    ver = 'v1'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"
    sale_price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    feat_importance = pd.read_csv(f"{path}/feature_importance.csv")
    feat_importance_plot = plt.imread(f"{path}/feature_importance.png")
    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")
    y_train = pd.read_csv(f"{path}/y_train.csv")
    y_test = pd.read_csv(f"{path}/y_test.csv")

    st.write("### ML Pipeline: Predict House Sale Price")

    st.info(
        f"The Regressor model was been chosen to predict the sales price "
        f"for the inherited property as requested by the client."
        f"As well as for the prediction of other unseen data.\n"
        f"* Both feature selection and PCA (Principle Component Analysis) "
        f"were tested to see which would yield the best results.\n"
        f"* Upon evaluation it became clear that feature selection was "
        f"the superior step in the pipeline. The PCA did not achieve the "
        f"business requirement for the test set of an r2 score of atleast 0.75."
        f"* Feature selection achieved an R2 Score: 1.00 on the train set and "
        f"an R2 Score: 0.847 on the test set.\n"
    )

    # show best features
    st.write("### The features used to train the model and their importance:")
    cnt = 0
    for feat_str in feat_importance['Feature'].sort_values():
        if cnt == 0:
            new_str = feat_str
            cnt = 1
        else:
            new_str = new_str + ', ' + feat_str

    st.write(new_str)
    st.image(feat_importance_plot)
    st.write("---")

    # evaluate pipeline performance
    st.write("### Evaluating the Pipeline Performance.")
    rgs_performance(X_train, y_train, X_test, y_test, sale_price_pipe)
    regr_eval_plots = plt.imread(f"{path}/regression_evaluation_plots.png")
    st.image(regr_eval_plots)
    st.write("---")
