'''
This file and the contents have been taken from the
 Churnometer walk through Project 2 and customized for
 this project
'''
import streamlit as st
from src.file_management import load_housing_price_data, load_clean_data

import plotly.express as px
import seaborn as sns
sns.set_style("whitegrid")


def sales_price_study_page_body():

    # load data
    dataset = 0
    df = load_housing_price_data()

    target_variables = ['1stFlrSF', 'GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']

    st.write("### Housing Sales Price Study")

    st.info(
        f"* To reitterate the first business requirement was:\n"
        f"  * Lydia is interested in discovering what features of a house "
        f"correlate with the sales price.\n"
        f"  * Lydia desires a visualization of the correlated "
        f"variables against the sale price and a summary of what these visalizations mean.\n"
    )

    # inspect the data

    if st.checkbox("Inspect the raw dataset"):
        st.write(
            f"The data set as a whole has {df.shape[0]} rows and {df.shape[1]} columns,"
        )
        st.write(df.head(10))

    st.info(
        f"* Correlation studies were performed on the data to get a batter understanding of the what the data contained, "
        f"whilst also answering the first business requirement.\n"
        f"* The correlation studies ustilised spearman and pearson methods in order to review the correlation between all variables "
        F"and the Sales Price. If you wish to read up on these methods and how they calculate correlation follow this "
        f"[link](https://towardsdatascience.com/clearly-explained-pearson-v-s-spearman-correlation-coefficient-ada2f473b8)\n"
    )

    st.success(
        f"* Upon an initial investigation of the data we found that these variables were the most correlated to Sales Price: \n"
        f"  * 1stFlrSF - First Floor square feet\n"
        f"  * GarageArea - Size of garage in square feet\n"
        f"  * GrLivArea - Above grade (ground) living area square feet\n"
        f"  * OverallQual - Rates the overall material and finish of the house\n"
        f"  * TotalBsmtSF - Total square feet of basement area\n"
        f"  * YearBuilt - Original construction date\n"
    )
    st.warning(
        f"* we can visualise this correlation with the following plots:"
    )

    df_eda = df.filter(target_variables + ['SalePrice'])

    if st.checkbox("View the correlation plot"):
        st.info(
            f"* Below you will 6 plots that refer to each of the traget varibales defined above.\n"
            f"* If you remember these varibales are the ones that showed the greatest correlation with SalesPrice"
        )
        st.info(
            f"* Each plot contains a scatter graph as well as an accompaning box plot.\n"
            f"* The scatter graph shows the trend the center of which is highlited by the red trendline.\n"
            F"* The box plots are presnt to show a clear visual indication where the majority of the data sits along with the median."
            f" as well as any data points which may be considered outliers."
        )
        st.success(
            f"* These plots are made using Plotly as such they are fully responsive.\n"
            f"* you can find teh Plotly documentation [here](https://plotly.com/python/) "
            f"if you want to know more."
        )

        def plot_numerical(df, col, target_var):
            fig = px.scatter(
                data_frame=df_eda, x=col, y=target_var,
                marginal_x='box', trendline='ols',
                trendline_color_override='red',
                title=f'{col} against {target_var}',
                width=1000, height=800
            )
            st.plotly_chart(fig)

        target_var = 'SalePrice'
        for col in target_variables:
            plot_numerical(df_eda, col, target_var)
            st.write("\n\n")
