import streamlit as st

from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.summary_page import summary_body_page
from app_pages.sales_price_study_page import sales_price_study_page_body
from app_pages.sales_price_predictor_page import sales_price_predictor_page_body
from app_pages.hypothesis_page import hypothesis_page_body
from app_pages.ml_predict_sales_price_page import ml_predict_sales_price_page_body

# Create an instance of the app
app = MultiPage(app_name="Housing Sales Price Price Predictor")

# Add your app pages here using .add_page()
app.add_page(
    "Quick Project Summary", summary_body_page
    )
app.add_page(
    "Housing Sales Price Study", sales_price_study_page_body
    )
app.add_page(
    "Sales Price Predictor", sales_price_predictor_page_body
    )
app.add_page(
    "Project Hypothesis and Validation", hypothesis_page_body
    )
app.add_page(
    "ML: Housing Sales Price Prediction", ml_predict_sales_price_page_body
    )

app.run()
