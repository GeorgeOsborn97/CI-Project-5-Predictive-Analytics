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
    st.info(
        f"* How did we get to these results?\n"
        f"    * These results were generated by running a clean version of the raw data through an ExtraTreesRegressor model. "
        f"Where the max_depth = 32 n_estimators = 150. With these hyper parameters set within the model "
        f"we ran a custum function to determine the features of imprtance.\n"
        f"* If you wish to look at this in more detail please view the Jupyter notebook in the readme file on github, "
        f" found [here](https://github.com/GeorgeOsborn97/CI-Project-5-Predictive-Analytics/blob/main/jupyter_notebooks/05%20-%20Model%20and%20Evaluation%20-%20Predict%20Sales%20Price.ipynb)\n"
        f"* What do these results mean?\n"
        f"    * What this tells us is that the six features identified are what impacts the Sales price of a property. "
        f"Knowing this we are able to refine our pipeline by only using these six features increasing efficiency and readability. "
        f"It is this refined pipeline and model that this dashboard uses to predict on data."
    )
    st.write("---")

    # evaluate pipeline performance
    st.write("### Evaluating the Pipeline Performance.")
    rgs_performance(X_train, y_train, X_test, y_test, sale_price_pipe)
    regr_eval_plots = plt.imread(f"{path}/regression_evaluation_plots.png")
    st.image(regr_eval_plots)
    st.info(
        f"* How did we get to these results?\n"
        f"    * These scores and accompanying plots came are the results of training the model defined above. "
        f" They refer to the train set and test set respectivly, again if you wish to view the process taht lead to these results, "
        f" please follow the link to the jupyter notebook above.\n"
        f"* What do these results mean?\n"
        f"    * As defined in our business case the target and therefore what we can consider a success is an R2 Score of 0.75 or above. "
        f"As we can see both the train and test sets exceed this criteria. As such we may consider our model a success and trust its predicions.\n"
    )
    st.write("---")
