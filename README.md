![]()

# House Price Predictions
## A Predictive Analytics Project

This project is the final milestone project that has been completed during my time studying at Code Institute. I decided to take Predictive Analytics as my specialistation and that forms the subject of this project. 

The goal of this project was to use Machine Learning to produce a model that can predict the potential sales price of houses to a reliable degree of accuracy. Then to present the data, steps taking in producing the model, the working model itself as well as the any evaluation conducted and my own findings on the the data. All this information will then be presented in a user friendly manner utilising a simple dashboard produced using streamlit. 

(additional info?)
___
mock up image
___
## Contents
1. [The Business Problem](#the-business-problem)
2. [Business Case](#business-case)
3. [business-requirements](#business-requirements)
    * [business-requirement-1](#business-requirement-1)
    * [business-requirement-2](#business-requirement-2)
4. [The Data](#the-data)
    * [Data Collection](#data-collection)
        * [What is Kaggle?](#what-is-kaggle)
    * [Data Content](#data-content)
    * [Data Table](#data-table)
___
## The Business Problem
A fictional individual, Lydia Doe, has received an inheritance from a deceased great-grandfather. Included in the inheritance are four houses located in Ames, Iowa, USA. Although Lydia has an excellent understanding of property prices in her home country of Belgium, she fears that basing her estimates for property worth on her current knowledge of the Iowan market might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa.

Lydia needs help if she is to maximize the sales price for the inherited properties. She decides to ask a Data Practitioner for help. Her reasons for doing so are:

* She doesn't know the worth of the properties and does not want to take the risk of inaccurate pricing estimation, since there is potentially a reasonable amount of money to be made or lost when selling the four properties.
* She is also interested in predicting the sale price from any house in Ames, Iowa in case of future property ownership in that area.

From searching the Internet, Lydia found a public dataset with house prices for Ames, Iowa, and will provide you with that. You will build a Data Web App to predict the sales price from the four houses based on the house attributes. The business requirements are:

* The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

Deliver a dashboard that meets the above requirements.
## Business Case
1. What are the business requirements?
    * The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
    * The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.
2. Is there any business requirement that can be answered with conventional data analysis? 
    * Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.
3. Does the client need a dashboard or an API endpoint?
    * The client needs a dashboard
4. What does the client consider as a successful project outcome? 
    * A study showing the most relevant variables correlated to sale price. 
    * Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.
5. Can you break down the project into Epics and User Stories? 
    * Information gathering and data collection.
    * Data visualization, cleaning, and preparation.
    * Model training, optimization and validation
    * Dashboard planning, designing, and development.
    * Dashboard deployment and release.
6. Ethical or Privacy concerns?
    * No. The client found a public dataset.
7. Does the data suggest a particular model?
    * The data suggests a regressor where the target is the sale price.
8. What are the model's inputs and intended outputs?
    * The inputs are house attribute information and the output is the predicted sale price.
9. What are the criteria for the performance goal of the predictions?
    * We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.
10. How will the client benefit? 
    * The client will maximize the sales price for the inherited properties.

## Business Requirements
### Business Requirement 1:
  * You may perform a correlation and/or PPS study to investigate the most relevant variables correlated to the sale price.
  * You have to visualize these variables against the sale price, so you can summarize the insights.
### Business Requirement 2:
  * You may deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
  * You may use either conventional ML or Neural Networks to map the relationships between the features and the target.
  * You may consider changing the ML task from Regression to Classification if you find a valid rationale for that.
  * In case you are modelling using conventional ML, with packages like scikit-learn for example, you may conduct an extensive hyperparameter optimization for a given algorithm. You can refer back to the Scikit-learn lesson, Unit Notebook 6: Cross-Validation Search Part 2. At the end of the notebook, you will find a list of hyperparameter options and values to start with, for the family of algorithms we covered in the course.
___
## The Data
### Data Collection
The data used in this project was sourced from [Kaggle](https://www.kaggle.com/)
#### What is Kaggle?
* Kaggle is an online community based platform that promotes collaberation between data scientists, provides a verity of tools to aid new and experinaces deelopers alike, as well as a blistering amount of public open datasets that can be freely applied to your own projects. One of these datasets is what we have utilised to train our model in this project.
### Data Content
* The Dataset used in this project contains data on housing built between 1872 and 2010 in the town of Ames, Iowa in the USA. 
* The link to this data was provided by Code Institute in the Assesment Handbook to aid in the production of this project. And was downloaded from Kaggle.

The Dataset used in this project to train the model contains 23 columns, and 1460 rows, a summary of the variables, meanings and units for each of these columns can be seen in the table below.
___
### Data Table
|Variable|Meaning|Units|
|---|---|---|
|1stFlrSF|First Floor square feet|334 - 4692 - (Min - Max > Sq. ft.)|
|2ndFlrSF|Second floor square feet|0 - 2065 - (Min - Max > Sq. ft.)|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8 - (Min - Max > Bedrooms)|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644 - (Min - Max > Sq. ft.)|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336 - (Min - Max > Sq. ft.)|
|TotalBsmtSF|Total square feet of basement area|0 - 6110 - (Min - Max > Sq. ft.)|
|GarageArea|Size of garage in square feet|0 - 1418 - (Min - Max > Sq. ft.)|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010 - (Min - Max > Year Built)|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642 - (Min - Max > Sq. ft.)|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245 - (Min - Max > Sq. ft.)|
|LotFrontage| Linear feet of street connected to property|21 - 313 - (Min - Max > Lin. ft.)|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600 - (Min - Max > Sq. ft.)|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286 - (Min - Max > Sq. ft.)|
|OpenPorchSF|Open porch area in square feet|0 - 547 - (Min - Max > Sq. ft.)|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736 - (Min - Max > Sq. ft.)|
|YearBuilt|Original construction date|1872 - 2010 - (Min - Max > Year Built)|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010 - (Min - Max > Remodel Year)|
|SalePrice|Sale Price|34.900 - 755.000 - (Min - Max > Sale price in $)|
