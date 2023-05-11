'''
This file and the contents have been taken from the
 Churnometer walk through Project 2 and customized for
 this project
'''
import streamlit as st


def summary_body_page():

    st.write("### Project Summary")

    # "Business Problem and Requirements" section
    """The Business Problem"""
    st.write("#### The Business Problem")
    st.info(
        f"* Lydia Doe, has received an inheritance from a deceased great-grandfather. "
        f"Included in the inheritance are four houses located in Ames, Iowa, USA. "
        f"Although Lydia has an excellent understanding of property prices in her home country of Belgium, "
        f"she fears that basing her estimates for property worth on her current knowledge of the Iowan market might lead to inaccurate appraisals. "
        f"What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa.\n"
        f"* Lydia needs help if she is to maximize the sales price for the inherited properties."
    )

    """The Business Requirements"""
    st.write("#### The Business Requirements")
    st.info(
        f"The project has 2 business requirements:\n"
        f"* 1 - Lydia is interested in discovering what features of a house "
        f"correlate with the sales price.\n"
        f"  * Lydia desires a visualization of the correlated "
        f"variables against the sale price and a summary of what these visalizations mean.\n"
        f"* 2 - Lydia desires to be able to predict the sales price "
        f"of her 4 inherited houses, "
        f"as well as any other house in Ames, Iowa, that she will consider to "
        f"buy or sell in the future."
        )

    # Link to README file, so the users can have access to
    # full project documentation
    """Readme file"""
    st.warning(
        f"* For additional information, please visit and **read** the "
        f"[Project README file.]"
        f"(https://github.com/GeorgeOsborn97/CI-Project-5-Predictive-Analytics#readme)"
        )

    """Dataset guidelines"""
    st.write("#### The Data")
    st.warning(
        f"* The dataset used during this project was extracted from Kaggle, a link to the dataset can be found "
        f"[here](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n"
        f"* Below you can see a table that covers the contents of the dataset."
    )
    st.info(
        f"**Dataset Content Guidelines**\n\n"
        f"|Variable|Meaning|Units|\n"
        f"|:----|:----|:----|\n"
        f"|1stFlrSF|First Floor square feet|(Min - Max > Sq. ft.) "
        f"334 - 4692|\n"
        f"|2ndFlrSF|Second floor square feet|(Min - Max > Sq. ft.) "
        f"0 - 2065|\n"
        f"|BedroomAbvGr|Bedrooms above grade (does NOT include "
        f"basement bedrooms)|(Min - Max > Bedrooms) 0 - 8|\n"
        f"|BsmtExposure|Refers to walkout or garden level walls|Gd: "
        f"Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; "
        f"No: No Exposure; None: No Basement|\n"
        f"|BsmtFinType1|Rating of basement finished area|GLQ: Good "
        f"Living Quarters; ALQ: Average Living Quarters; BLQ: Below "
        f"Average Living Quarters; Rec: Average Rec Room; LwQ: Low "
        f"Quality; Unf: Unfinshed; None: No Basement|\n"
        f"|BsmtFinSF1|Type 1 finished square feet|(Min - Max > Sq. ft.) "
        f"0 - 5644|\n"
        f"|BsmtUnfSF|Unfinished square feet of basement area|(Min - "
        f"Max > Sq. ft.) 0 - 2336|\n"
        f"|TotalBsmtSF|Total square feet of basement area|(Min - "
        f"Max > Sq. ft.) 0 - 6110|\n"
        f"|GarageArea|Size of garage in square feet|(Min - Max > "
        f"Sq. ft.) 0 - 1418|\n"
        f"|GarageFinish|Interior finish of the garage|Fin: Finished; "
        f"RFn: Rough Finished; Unf: Unfinished; None: No Garage|\n"
        f"|GarageYrBlt|Year garage was built|(Min - Max > Year) "
        f"1900 - 2010|\n"
        f"|GrLivArea|Above grade (ground) living area square feet|"
        f"(Min - Max > Sq. ft.) 334 - 5642|\n"
        f"|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: "
        f"Typical/Average; Fa: Fair; Po: Poor|\n"
        f"|LotArea| Lot size in square feet|(Min - Max > Sq. ft.) "
        f"1300 - 215245|\n"
        f"|LotFrontage| Linear feet of street connected to property|"
        f"(Min - Max > Lin. ft.) 21 - 313|\n"
        f"|MasVnrArea|Masonry veneer area in square feet|(Min - Max "
        f"> Sq. ft.) 0 - 1600|\n"
        f"|EnclosedPorch|Enclosed porch area in square feet|"
        f"(Min - Max > Sq. ft.) 0 - 286|\n"
        f"|OpenPorchSF|Open porch area in square feet|(Min - "
        f"Max > Sq. ft.) 0 - 547|\n"
        f"|OverallCond|Rates the overall condition of the house|"
        f"10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; "
        f"6: Above Average; 5: Average; 4: Below Average; 3: Fair; "
        f"2: Poor; 1: Very Poor|\n"
        f"|OverallQual|Rates the overall material and finish of the "
        f"house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: "
        f"Good; 6: Above Average; 5: Average; 4: Below Average; 3: "
        f"Fair; 2: Poor; 1: Very Poor|\n"
        f"|WoodDeckSF|Wood deck area in square feet|(Min - Max > "
        f"Sq. ft.) 0 - 736|\n"
        f"|YearBuilt|Original construction date|(Min - Max > Year) "
        f"1872 - 2010|\n"
        f"|YearRemodAdd|Remodel date (same as construction date "
        f"if no remodeling or additions)|(Min - Max > Year) 1950 - 2010|\n"
        f"|SalePrice|Sale Price|(Min - Max > Price in $) 34900 - 755000|\n"
        )