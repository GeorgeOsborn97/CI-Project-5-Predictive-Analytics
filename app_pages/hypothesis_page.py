'''
This file and the contents have been taken from the
 Churnometer walk through Project 2 and customized for
 this project
'''
import streamlit as st


def hypothesis_page_body():

    st.write("### Project Hypothesis")

    st.info(
        f"* Upon completion of the intitail data anlysis "
        f"we were able to define a number of hypothesis that could be tested.\n"
    )

    st.write("#### These are what we considered:")

    st.info(
        f"1. A house with a 'Larger' surface area will have a higher Sales Price.\n"
        f"2. A house with better Overall Quality will have a higher Sales Price.\n"
        f"3. A more recently built house of equivalint square footage and quality compared to an older house will have a a higher Sales Price.\n"
        f"4. A house with a more recent re model date will have a higher Sales Price.\n"
        f"    * Additionally a recent remodel of an older house will have a higher Sales Price when compared to an equivelent square footage and quality"
        f" house that was built in the same time as the remodel, and has not undergone any remodelling.\n"
    )

    st.write("#### This is how we decided to validate them:")

    st.info(
        f"* Correlation studies utilising Pearson and Spearmen tests "
        f"can be used in order to test all of our above hypothesis. "
        f"PPS (Predictive Power Score), may also be used to test the relationships between "
        f"the features in our data and test the hypothesis presented above."
    )
