
# House Price Predictions
## A Predictive Analytics Project

This project is the final milestone project that has been completed during my time studying at Code Institute. I decided to take Predictive Analytics as my specialistation and that forms the subject of this project. 

The goal of this project was to use Machine Learning to produce a model that can predict the potential sales price of houses to a reliable degree of accuracy. Then to present the data, steps taking in producing the model, the working model itself as well as the any evaluation conducted and my own findings on the the data. All this information will then be presented in a user friendly manner utilising a simple dashboard produced using streamlit. 

A link to the deployed sitye can be find [here](https://ci-project-5.herokuapp.com/)
___
![full mockup](/static/images/full_mockup.png)
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
5. [Development](#development)
    * [Crisp-DM](#crisp-dm)
    * [Agile Development](#agile-development)
6. [Answering Business Requirement 1](#answering-business-requirement-1)
7. [Answering Business Requirement 2](#answering-business-requirement-2)
8. [Conclusions](#conclusions)
9. [Dashboard Design](#dashboard-design)
10. [Testing](#testing)
    * [Known Bugs](#known-bugs)
11. [Future Additions](#future-additions)
12. [Deployment](#deployment)
13. [Credits and Acknowledgments](#credits-and-acknowledgments)
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
___
## The Hypothesis (based on the Data collected).
1. A house with a 'Larger' surface area will have a higher Sales Price.
2. A house with better Overall Quality will have a higher Sales Price.
3. A more recently built house house of equivalint square footage and quality then an older house will have a a higher Sales Price.
4. A house with a more recent re model date will have a higher Sales Price.
    * Additionally a recent remodel of an older house will have a higher Sales Price of an equivelent square footage and quality house that was built in the same time as the remodel, and has not undergone any remodelling.
5. Additional hypothesis to be added later to consider if i have time.

### How to test the Hypothesis.
Correlation studies utilising Pearson and Spearmen tests can be used in order to test all our above hypothesis. PPS (Predictive Power Score), may also be used to test the relationships between the features in our data and test the hypothesis presented above.
___
## Development
### Crisp-DM
* In order to best maximise my time and efficiency the CRISP-DM model was followed during all stages of development.
* What is Crisp-DM?
    * Crisp-DM stands for "Cross Industry Standard Process for Data Mining". It is essentailly a model taht describes the optimised work flow of a data mining project.
    By following the structure of the Crisp-DM workflow we can ensure that we are giving ourselves the best chance to complete our project successfully within the given time frame.
    * The model itself contains 6 stages:
        1. Business Understanding.
        2. Data Understanding.
        3. Data Preparation.
        4. Modelling.
        5. Evaluation.
        6. Deployment.
        * Below you will see a more in-depth look into these steps and an example of where these steps occured in the development of this project.

    ![Crisp-dm](/static/images/crisp_dm.png)
    
    1. Business Understanding:
        * What is it? The business understanding step is the time where you sit down and clarify the goals of the project. You must have a clear understanding of what success 
        will look like for the given project. You must have a defined list of the required/must have features taht constitute a successful project and you must have a tuime frame so that you may plan how to use your time effectively.  
        * Where was it applied? In the case of this project the Business understanding was done right away. The Business case and requirements were provided by Code Institute so were pre-defined from the get go. You may also see the Kanban Board linked in the repository where the steps to achieve the defined success were laid out.
    2. Data Understanding:
        * What is it? The data understanding step is where we bein to evalutate the data set or sets that we as data practitioners have been provided with. In this step we are looking to gain a firm grasp of what the data is showing and if it contains any issues that will need resolving before we can begin to use the data. Key things we want from this step are: What are the data types? Are there any null values in the data? Is there missing data within the data? But most importantly can the data provided answer the business requirments? If the answer is no, then we can go back to the Business understanding step and review our options.
        * Where was it applied? In the case of this project the data understanding was accomplished during the DataCollection and DataAnalysis Jupyter Notebooks.
    3. Data Preparation:
        * What is it? The data preparation step is the stage at which we organise and clean the data in preparation for modelling. It's in this step where we remove any null values, missing values, potentailly adjust data types if needed and finally engineer our data so that we may best optimse the model. This step is arguably the most important as poor quality data will result in a poor quality model. For this reason it is often the case that this step takes up the majority of development time. There is no hard and fast rule to which methods for cleaning and engineering will work best for your data so it may take a lot of trail and error before a final pipeline for data cleaning is established.
        * Where was it applied? In the case of this project the data understanding was accomplished during the DataCleaning and FeatureEngineering Jupyter Notebooks.
    4. Modelling:
        * What is it? The modelling step is where we finaly apply our data and attempt to find the most optimised way of answering our business requirement. In both our Business and data understanding steps we should of thought about what kind of model we will most liekly need. Regression, Classification or a cluster. In any case it is likely that this step will again be trail and error as you tweak hyperparameters and try different models in order to find the best for your specific case. 
        * Where was it applied? In the case of this project the data understanding was accomplished during the Model and Evaluation Jupyter Notebook. 
    5. Evaluation:
        * What is it? With each attempt at a new model or each tweak of a hyperparameter you will want to evaluate the results. Simply, does this model answer the business requirement? if it does great, you may still choose to try new avenues to see if you can acheive a better result or it may come to pass that you are not able to successfully answer the business requirement. If thats the case you may go back to the Data preparation step and see if making some changes there helps to optimsise the model. This and the previous two steps go hand in hand and as a data practioner you are likely going to jump back and forth between them.
        * Where was it applied? In the case of this project the data understanding was accomplished during the Model and Evaluation Jupyter Notebook. 
    6. Deployment:
        * What is it? Finally if the business requiremnt has been met you may deploy the project. In the business understanding you should already know what the deployed project should look like. A dashboard or an API for example.
        * Where was it applied? This project was deployed to heroku, a step by step guide to the deployment can be seen at the end of this document. 

### Agile Development
* Alongside the Crisp-DM workflow that was followed through out this project I aslo kept the principles of Agile Development in order to help maximise my time and work as effciently as possible. The Kanban board which was made in GitHub Projects was pivitol in guuiding the development of this project.
* A link to the GitHub project can be seen [here](https://github.com/users/GeorgeOsborn97/projects/5/views/1)
![kanban](/static/images/kanban.png)

___
## Answering Business Requirement 1
## Answering Business Requirement 2
## Conclusions
___
## Dashboard Design
___
## Testing
### Known Bugs
___
## Future Additions
___
## Deployment
___
## Credits and Acknowledgments
___
