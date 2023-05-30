
# House Price Predictions
## A Predictive Analytics Project

This project is the final milestone project that has been completed during my time studying at Code Institute. I decided to take Predictive Analytics as my specialisation and that forms the subject of this project. 

The goal of this project was to use Machine Learning to produce a model that can predict the potential sales price of houses to a reliable degree of accuracy. Then to present the data, steps taking in producing the model, the working model itself as well as any evaluation conducted and my own findings on the data. All this information will then be presented in a user-friendly manner, utilising a simple dashboard produced using streamlit. 

A link to the deployed site can be find [here](https://ci-project-5.herokuapp.com/)
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
    * And have a reliable method to determine if the purchase of a future property is likely to yield a good return.

## Business Requirements
### Business Requirement 1:
  1. You may perform a correlation and/or PPS study to investigate the most relevant variables correlated to the sale price.
  2. You have to visualize these variables against the sale price, so you can summarize the insights.
  * The work done to answer this business requirement can be seen in the DataCollection and DataAnalysis jupyter notebooks. In the Readme I shall publish the results and summarise the findings.

### Business Requirement 2:
  1. You may deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
  2. You may use either conventional ML or Neural Networks to map the relationships between the features and the target.
  3. You may consider changing the ML task from Regression to Classification if you find a valid rationale for that.
  4. In case you are modelling using conventional ML, with packages like scikit-learn for example, you may conduct an extensive hyperparameter optimization for a given algorithm.
  * The work done to answer this business requirement can be seen in the DataCleaning, FeatureEnginnering and the Model and Evaluation jupyter notebooks. In the Readme I shall publish the results and summarise the findings.
___
## The Data
### Data Collection
The data used in this project was sourced from [Kaggle](https://www.kaggle.com/)
#### What is Kaggle?
* Kaggle is an online community based platform that promotes collaboration between data scientists, provides a variety of tools to aid new and experienced developers alike, as well as a blistering amount of public open datasets that can be freely applied to your own projects. One of these datasets is what we have utilised to train our model in this project.
### Data Content
* The Dataset used in this project contains data on housing built between 1872 and 2010 in the town of Ames, Iowa in the USA. 
* The link to this data was provided by Code Institute in the Assessment Handbook to aid in the production of this project.

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
3. A more recently built house of equivalent square footage and quality than an older house will have a higher Sales Price.
4. A house with a more recent remodel date will have a higher Sales Price.
    * Additionally, a recent remodel of an older house will have a higher Sales Price of an equivalent square footage and quality house that was built in the same time as the remodel, and has not undergone any remodelling.

### How to test the Hypothesis.
Correlation studies utilising Pearson and Spearmen tests can be used in order to test all our above hypothesis. PPS (Predictive Power Score), may also be used to test the relationships between the features in our data and test the hypothesis presented above.
___
## Development
### Crisp-DM
* In order to best maximise my time and efficiency, the CRISP-DM model was followed during all stages of development.
* What is Crisp-DM?
    * Crisp-DM stands for "Cross Industry Standard Process for Data Mining". It is essentially a model that describes the optimised work flow of a data mining project.
    By following the structure of the Crisp-DM workflow, we can ensure that we are giving ourselves the best chance to complete our project successfully within the given time frame.
* The model itself contains 6 stages:
    1. Business Understanding.
    2. Data Understanding.
    3. Data Preparation.
    4. Modelling.
    5. Evaluation.
    6. Deployment.
    * Below you will see a more in-depth look into these steps and an example of where these steps occurred in the development of this project.

    ![Crisp-dm](/static/images/crisp_dm.png)
    
    1. Business Understanding:
        * What is it? The business understanding step is the time when you sit down and clarify the goals of the project. You must have a clear understanding of what success 
        will look like for the given project. You must have a defined list of the required/must have features that constitute a successful project and, it is important to have a time frame so that you may plan how to use your time as effectively as possible.  
        * Where was it applied? In the case of this project, the Business understanding was done right away. The Business case and requirements were provided by Code Institute so were pre-defined from the get go. You may also see the Kanban Board linked in the repository where the steps to achieve the defined success were laid out.
    2. Data Understanding:
        * What is it? The data understanding step is where we behin to evaluate the data set or sets that we as data practitioners have been provided with. In this step we are looking to gain a firm grasp of what the data is showing and if it contains any issues that will need resolving before we can begin to use the data. Key things we want from this step are: What are the data types? Are there any null values in the data? Is there missing data within the data? But most importantly can the data provided answer the business requirements? If the answer is no, then we can go back to the Business understanding step and review our options.
        * Where was it applied? In the case of this project the data understanding was accomplished during the DataCollection and DataAnalysis Jupyter Notebooks.
    3. Data Preparation:
        * What is it? The data preparation step is the stage at which we organise and clean the data in preparation for modelling. It's in this step where we remove any null values, missing values, potentially adjust data types if needed and finally engineer our data so that we may best optimise the model. This step is arguably the most important as poor quality data will result in a poor quality model. For this reason it is often the case that this step takes up the majority of development time. There is no hard and fast rule to which methods for cleaning and engineering will work best for your data so it may take a lot of trail and error before a final pipeline for data cleaning is established.
        * Where was it applied? In the case of this project the data preparation was accomplished during the DataCleaning and FeatureEngineering Jupyter Notebooks.
    4. Modelling:
        * What is it? The modelling step is where we finally apply our data and attempt to find the most optimised way of answering our business requirement. In both our Business and data understanding steps we should of thought about what kind of model we will most likely need. Regression, Classification or a cluster. In any case it is likely that this step will again be trail and error as you tweak hyperparameters and try different models in order to find the best for your specific case. 
        * Where was it applied? In the case of this project the data modelling was accomplished during the Model and Evaluation Jupyter Notebook. 
    5. Evaluation:
        * What is it? With each attempt at a new model or each tweak of a hyperparameter you will want to evaluate the results. Simply, does this model answer the business requirement? if it does great, you may still choose to try new avenues to see if you can achieve a better result or it may come to pass that you are not able to successfully answer the business requirement. If thats the case you may go back to the Data preparation step and see if making some changes there helps to optimise the model. This and the previous two steps go hand in hand and as a data practitioner you are likely going to jump back and forth between them.
        * Where was it applied? In the case of this project the evaluation was accomplished during the Model and Evaluation Jupyter Notebook. 
    6. Deployment:
        * What is it? Finally if the business requirement has been met you may deploy the project. In the business understanding you should already know what the deployed project should look like. A dashboard or an API for example.
        * Where was it applied? This project was deployed to heroku, a step by step guide to the deployment can be seen at the end of this document. 

### Agile Development
* Alongside the Crisp-DM workflow that was followed through out this project I also kept the principles of Agile Development in order to help maximise my time and work as efficiently as possible. The Kanban board which was made in GitHub Projects was pivotal in guiding the development of this project.
* A link to the GitHub project can be seen [here](https://github.com/users/GeorgeOsborn97/projects/5/views/1)
![kanban](/static/images/kanban.png)
* The Kanban allowed a clear separation of jobs that meant we did not have to split focus over multiple jobs at once, furthermore it meant we can be sure that each job is 100% complete before we move on to the next, This is achieved by having clear acceptance criteria as defined below. The flow of the board is simple. When an Issue is defined it is placed in the 'To Do' column, when we begin to work on the tasks associated with it, it is moved to the 'In Progress' and finally when all acceptance criteria is met it is moved to the 'Done' column. You may see this process below.

|From 'To Do'|To 'In Prrogress'|All Issues 'Done'|
|---|---|---|
|![kanban](/static/images/progress.jpg)|![kanban](/static/images/more_progress.jpg)|![kanban](/static/images/kanban.png)|

* The Kanban is made up of 'Issues', each issue represents a step in the development process. They all follow the same template, the top sentence describes what feature needs implementing and the reason as to why. The second section describes the Acceptance Criteria, which tells us what needs to be done in order to mark the Issue as complete. Finally, there is the Tasks, this section describes the jobs that need completing in order to complete the acceptance criteria. 
* Each issue is also assigned a label that shows its importance, Priority 1 through 5 which tells us if it is a must have feature (Priority 1) or something we should only try to include if we finish everything else (Priority 5). 
![issues](/static/images/issues.jpg)

___
## Answering Business Requirement 1
* To reiterate the first requirement was:
    * Perform a correlation and/or PPS study to investigate the most relevant variables correlated to the sale price.
    * Visualize these variables against the sale price, so you can summarize the insights.
* Two correlation studies were conducted as part of the DataAnalysis notebook. Both Pearson and Spearmen correlation tests were performed on the data to view the correlation of the other variables to the Sales Price. If you would like to read up on these correlation tests you may follow the link [here](https://www.analyticsvidhya.com/blog/2021/03/comparison-of-pearson-and-spearman-correlation-coefficients/#:~:text=Pearson%20correlation%3A%20Pearson%20correlation%20evaluates,rather%20than%20the%20raw%20data.) 
* Concluding these tests we found these results: 
    1. A house with a high sales price typically has a large 1st floor square footage.
    2. A house with a high sales price typically has a large garage square footage.
    3. A house with a high sales price typically has a large above grade (ground) living area square footage.
    4. A house with a high sales price typically has a high overall quality.
    5. A house with a high sales price typically has a large basement square footage.
    6. A house with a high sales price typically was built more recently.
* To answer the second part of the business requirement we plotted these 6 variables against sales price.

|Variable|Graph|
|---|---|
|1stFlrSf against SalePrice|![corr_1](/static/images/corr_1.png)|
|GarageArea against SalePrice|![corr_2](/static/images/corr_2.png)|
|GrLivArea against SalePrice|![corr_3](/static/images/corr_3.png)|
|OverallQual against SalePrice|![corr_4](/static/images/corr_4.png)|
|TotalBsmtSF against SalePrice|![corr_5](/static/images/corr_5.png)|
|YearBuilt against SalePrice|![corr_6](/static/images/corr_6.png)|

## Answering Business Requirement 2
* To reiterate the second requirement was:
    * Deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
    * Use either conventional ML or Neural Networks to map the relationships between the features and the target.
    * Consider changing the ML task from Regression to Classification if you find a valid rationale for that.
    * In case you are modelling using conventional ML, with packages like scikit-learn for example, you may conduct an extensive hyperparameter optimization for a given algorithm.
* In preparation to answer this business requirement the data had to be cleaned and engineered, the process of which can be found in the DataCleaning and FeatureEngineering notebooks. Having completed this we can move on the answering the requirement. 
* The specific code that was ran in order to answer the requirement can be found in the Model and Evaluation notebook.
* In the end we found that the most optimal model was as an ExtraTreesRegressor with max_depth=32 and n_estimators=150 applied to the features that were flagged as high importance. The full Pipeline and work is viewable in the notebook if you would like to see the steps that lead to that conclusion.
* Utilising this model we were able to achieve an r2_score of 1.0 on the train set and 0.847 on the test set. The Business Case defined that an r2_score > 0.75 was required.
* You may see the plots below that help visualise the results of the model on the train and test sets as well as the results of our model.
* Train Set
    * R2 Score: 1.0
    * Mean Absolute Error: 138.289
    * Mean Squared Error: 947914.048
    * Root Mean Square Error: 973.609
* Test Set
    * R2 Score: 0.847
    * Mean Absolute Error: 21292.305
    * Mean Squared Error: 1053381483.713
    * Root Mean Square Error: 32455.839

![evaluation plots](/outputs/ml_pipeline/predict_saleprice/v1/regression_evaluation_plots.png)   

* Finally we want to prove our model can predict on unseen data. By visiting the link at the top of this page to the deployed site you will be able to try this out for yourself. However for clarity, below are two images, showing two predictions. The first on the first property presented in the Business Case, and the second on random unseen data created by myself. As we can see the model is able to predict a potential sales price for the properties.
![prediction 1](/static/images/predict_1.png)
![prediction 2](/static/images/predict_2.png)

___
## Dashboard Design
* It was agreed in the Business Case that the ideal end point of this project was a interactive dashboard that would display the findings and results.
* In designing the dashboard it became clear that five pages would be necessary to show all relevant and required information, below is a break down of all these pages.

1. Page 1: Quick Project Summary.
    * What's the purpose? To provide the reader with the information needed to understand the purpose of the dashboard and what it aims to achieve.
    * How does it achieve this? The summary page has a total of 3 sections that help to acheive the above purpose.
        * The Business Problem.
        * The Business Requirements.
        * The Data.
    * Each of these sections has a clear definition that tells the reader only what they need to know. The first two sections help outline the purpose / goal of the dashboard itself, whilst the final section is there to introduce the reader to the data set so that they may gain a better understanding of it, which will help them to understand the content of future pages.
![page 1](/static/images/page_1.png)

2. Page 2: Housing Sales Price Study.
    * What's the purpose? Answering the first business requirement.
    * How does it achieve this? The sales price study page has five distinct sections within it.
        * The business requirement.
        * Raw data.
        * A simple description of the correlation studies that were performed.
        * The singled out variables.
        * The study results.
    * The first section is self explanatory, it is simply there to remind the reader of the first requirement that will be being answered on the page.
    * The second section introduces the dataset, where as the previous section described the variables, the reader now has the chance to look through the actual data and gain a better understanding of it.
    * The third section introduces the reader to the studies that were performed, not much detail is provided however a link is provided if they wish to do further study on how these correlations are calculated and what they show.
    * The forth section shows the result of an initial investigation into the correlation, it shows the 6 variables that were isolated as the most correlated with sales price.
    * Finally the fifth section is the visualisation that was required in the requirement. Each correlation plot contains a scatter and box plot that can be investigated utilising plotly. 
![page 2](/static/images/page_2.png)
![page 2b](/static/images/page_2b.png)

3. Page 3: Sales Price Predictor.
    * What's the purpose? Answering the second business requirement.
    * How does it achieve this? This page is split into three sections that help to achieve the goal of the page.
        * The first section again is self explanatory, it is simply there to remind the reader of the second requirement that will be being answered on the page.
        * The second section answers the first part of the requirement, the client in this respect can go down the tick boxes and check the predicted sales price for each of her inherited houses.
        * The third section answers the second part of the requirement. The 6 key features are presented and are able to be adjusted to represent different potential houses in order to get a prospective sales price for any house in Armes Iowa.
![page 3](/static/images/page_3.png)
![page 3b](/static/images/page_3b.png)

4. Page 4: Project Hypothesis and Validation.
    * What's the purpose? Provide the reader with an insight into the assumptions made in regards to the business problem, allowing them to understand our thought process and how it influenced the work done when we attempted to validate these assumptions.
    * How does it achieve this? This page contains 2 sections but they may be considered as a single section.
        * This page simply outlines the assumptions made after the initial analysis of the data, it then goes on to say how these assumptions will be validated.
![page 4](/static/images/page_4.png)

5. Page 5: ML: Housing Sales Price Prediction.
    * What's the purpose? Provide a more in depth look at how the model is able to predict on sales price. For the more computer savvy reader they should be able to understand the methodology and the results.
    * How does it achieve this? This page contains three sections that help to achieve the goal of the page.
        * The first is a basic description of the model that was chosen, it describes other methods that were evaluated and the result of the best model which impacted our decision.
        * The second section is a simple bar chart that shows the features that were used to train the model based on their importance.
        * Finally we have the results of the model on our train and test sets. This section contains 4 different scores for each set and a plot for both sets in order to help visualise the results more clearly.
![page 5](/static/images/page_5.png)
![page 5](/static/images/page_5b.png)

### Additional pages post deployment.
* With some additional time before the deadline for this project I thought it would be a good addition to book end the project with a generalised introduction based around what a user may expect from the dashboard, as well as a simple yet thorough conclusion the wraps up the dashboard in a concise manner.

1. Page 1a: Introduction.
    * What's the purpose? Introduce the reader / user to dashboard and provide them with knowledge of what they can expect to gain from it.
    * How does it achieve this? The small paragraph that makes up this page sets out the 'journey' that the user will go on as they progress through the dashboard. It's simple syntax means that even those that are not well versed in Machine Learning or computer science should be able to digest and understand what the dashboard is here to do.
![page 1a](/static/images/intro.jpg)

2. Page 7: Conclusion.
    * What's the purpose? Summarise what the user has learnt as they progressed through the dashboard.
    * How does it achieve this? This page contains three sections that help to achieve the goal of the page.
        * The first section simply reminds the user of the business requirements that were set in the beginning of the project.
        * The second section breaks down how each of those business requirements have been fulfilled.
        * Finally we have a paragraph that concluded what the user has learnt and what the dashboard has achieved in a broader assessment.
![page 7](/static/images/conclusion.jpg)
___
## Testing
* As the dashboard is being produced by streamlit we only need to conduct basic testing on our features to ensure everything is working as expected.

|Feature being tested|How was it tested|Expected outcome|Actual Outcome|
|---|---|---|---|
|Navigation menu|Each of the five navigation buttons were clicked one at a time.|Each navigation button should take the user to the page they selected.|Each button successfully bought me to the correct page.|
|Inspect the Raw data|The button to reveal the raw data was clicked twice, once to open the raw data table, and again to close it.|The first click of the button opens the raw data in a table showing the first 10 rows, the second click closes it.|The table opened and closed as expected.|
|Reveal Correlation plots|The button to reveal the correlation plots was clicked twice, once to reveal the plots, and again to remove them.|The first click of the button reveals all 6 correlation plots, the second click closes them all.|The plots came and went as expected.|
|Price predictions of inherited houses|All four of the buttons that reveal the individual housing data and the predicted price were clicked twice, once to reveal the data and once to remove them.|The first click should reveal a single row of data relating to that house, as well as the sales price prediction for that house. The second click should remove both these bits of information.|The first click did reveal all expected information and the second successfully removed them.|
|Invalid inputs of price prediction widgets|text was typed into every numerical variable, incorrect text and numbers were typed into the drop down menu for KitchenQual.|Numerical inputs should not accept anything that is not a number, KitchenQual should not accept an input that is not in the drop down menu.|When an invalid input was placed in any widget it would return to its default value.|
|Price prediction of manual input|The 'Run Predictive analysis button was clicked with different input data being applied.|The button should reveal a Sales Price prediction that is displayed to the user.|Successfully displayed a predicted Sales Price to the user.|

* Testing was also carried on the Jupyter notebooks. In order to validate that the results found through out the notebooks were accurate and could be replicated the notebooks themselves were frequently cleared of all outputs and reset. The notebooks were then ran through cell by cell. we expected the out puts of our python code to remain the same each time. Luckily that is exactly what we found. 


### Known Bugs
* No known bugs exist in the dashboard.
___
## Future Additions
* There are several additional avenues that this project could be taken down to expand it's potential. Given more time these are the routes that I feel would add significant positive impact to the dashboard.
    * Review the correlation coefficients of the identified key features in order to review which has the greatest impact on Sales price. Cross reference this with the average cost of improving the key feature in order to see which of the key features is most cost effective when looking to gain the biggest return in investment.
    * Another obvious avenue to be explored would be to expand the locations to which the model is applied. If new datasets were sourced that contained property records in a new area we can start to predict their sales price to.  
___
## Deployment
* The deployment for this project was hindered by a mistake in the requirements.txt file, A wrong streamlit version was originally installed and when it came to deploying the dashboard this caused some errors. This was resolved in changing the requirements by uninstalling all packages and reisntalling only those that were required and of the correct verion. A note of this can be found in the commits in the repo. Below is a simple step guide to how the project was deployed to heroku. 
1. Log in to Heroku and create an App
2. Log into Heroku CLI using the command "heroku login -i" and enter your login information.
3. Run the command git init to re-initialise the Git repository
4. Run the command "heroku git:remote -a YOUR_APP_NAME" to connect the workspace and your Heroku app.
5. Set the app's stack to heroku-20 using the command "heroku stack:set heroku-20" this is needed to make the app compatible with Python 3.8.12.
6. Use git push heroku main to deploy the application to Heroku or navigate to the Deploy tab in the heroku dashboard and manually deploy.

___
## Packages and Technologies utilised.
* Technology that was utilised:
    * GitHub
    * GitPod
    * Heroku
    * Code Institute functions as defined in accompanying lessons.
* Languages used:
    * Python
    * Markdown
* Packages used: 
    * Numpy
    * Pandas
    * MatPlotLib
    * Plotly
    * seaborn
    * Pandas Profiling
    * PPS score
    * StreamLit
    * Feature Engine
    * Scikit Learn
    * xgboost
    * yellowbrick
    * Jinja2
    * MarkupSafe
    * Protobuf
    * ipywidgets
___
## Credits and Acknowledgments
* The Streamlit Docs were visited frequently when setting up the dashboard. They can be found [here](https://docs.streamlit.io/)
* StackOverflow was visited several times for assistance and understanding.
* The Predictive Analytics lessons and walkthrough projects were frequently refered back to throughout the whole development of this project.
* [https://github.com/Vasi012/PP5-Predictive-Analysis](https://github.com/Vasi012/PP5-Predictive-Analysis) was used as a reference throughout the project.
* I would also like to give a huge thank you to Marcel Mulders for their amazing support during this project.

___
