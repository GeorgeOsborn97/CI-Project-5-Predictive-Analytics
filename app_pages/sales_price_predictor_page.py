'''
This file's contents were taken from the
 Churnometer walk through Project 2 and customized for
 this project
'''
import streamlit as st
import pandas as pd
from src.file_management import load_clean_data, load_pkl_file
from src.predictive_analysis_ui import predict_sale_price


def sales_price_predictor_page_body():

    # Load all the neccessey files

    ver = 'v1'
    file_path = f"outputs/ml_pipeline/predict_saleprice/{ver}"

    prediction_pipeline = load_pkl_file(
        f"{file_path}/best_regressor_pipeline.pkl"
        )
    price_features = (
        pd.read_csv(f"{file_path}/X_train.csv")
        .columns
        .to_list()
        )
    feature_importance = list(
        pd.read_csv(f"{file_path}/feature_importance.csv")['Feature']
        )

    st.write("### Sales Price Prediction")
    st.info(
        f"* Here we are looking to solve the second business requirement.\n"
        f"* To reiterate the requirement is as follows:"
    )
    st.info(
        f"* Lydia desires to be able to predict the sales price"
        f" of her 4 inherited houses,"
        f" as well as any other house in Ames, Iowa, that she will consider to"
        f" buy or sell in the future."
    )

    st.success(
        "##### Below is the results of the work done in order to answer the above business requirement:"
    )
##################
    total_price = predict_inherited_house_price(prediction_pipeline, price_features)
    total_price = "%.2f" % total_price
    st.success(
        f"**The total predicted Sales Price, if all properties were to be sold is: "
        f":blue[\u0024{total_price}].**"
        )
##################
    check_var = False
    if check_var:
        check_variables_for_UI(price_features)

    st.write("### Houses Price Predictor")
    st.warning(
        f"* Enter your values for the property for "
        f"which you require a **price prediction**.\n\n"
        f"Legend: \n\n"
        f"* 1stFlrSF - First Floor measured in square feet.\n"
        f"* GrLivArea - Above grade (ground) living area square feet.\n"
        f"* GarageArea - Size of garage in square feet.\n"
        f"* KitchenQual - Kitchen quality.\n"
        f"    * 	Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair\n"
        f"* YearRemodAdd - Remodel date (same as construction date if no remodeling or additions)\n"
        f"* YearBuilt - Original construction date."
        )
    X_live = DrawInputsWidgets()

    if st.button("Run Predictive Analysis"):
        price_prediction = predict_sale_price(X_live,
                                              price_features,
                                              prediction_pipeline)
        statement = (
            f"The predicted selling price for this property "
            f"is \u0024{price_prediction}"
            )

        st.success(statement)

##################


def predict_inherited_house_price(prediction_pipeline, price_features):
    inherited = load_clean_data("inherited")
    row_count = len(inherited)
    inherited.index = range(1, row_count+1)
    total_price = 0
    u_key = 0
    for x in range(row_count):
        u_key += 1
        X_live = inherited.iloc[[x]]
        price_prediction = predict_sale_price(X_live, price_features, prediction_pipeline)
        price_prediction = "%.2f" % price_prediction
        if st.checkbox(f"Check the box to view the data and individual Sales Price of property {x+1}", key=u_key,):
            st.write(X_live)
            statement = (
                f"* The predicted Sales Price for this property: "
                f":blue[\u0024{price_prediction}]"
            )
            st.success(statement)
        total_price += float(price_prediction)
        st.write("---")

    return total_price
####################


def check_variables_for_UI(price_features):
    import itertools

    combined_features = set(
        list(
            itertools.chain(price_features)
            )
        )
    st.write(f"* There are {len(combined_features)} features "
             f"for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    df = load_clean_data("clean")
    percentageMin, percentageMax = 0.2, 2.0

    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    X_live = pd.DataFrame([], index=[0])

    with col1:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col2:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col4:
        feature = "KitchenQual"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
            )
        X_live[feature] = st_widget

    with col5:
        feature = "YearRemodAdd"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col6:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    st.write(X_live)

    return X_live
####################