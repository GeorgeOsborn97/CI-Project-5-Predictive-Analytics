import streamlit as st


def conclusion_page_body():

    st.info(
        f"To reitterate, the business requirements set out in the beginning of this project were:\n"
        f"* Lydia is interested in discovering what features of a house "
        f"correlate with the sales price.\n"
        f"    * Lydia desires a visualization of the correlated "
        f"variables against the sale price and a summary of what these visalizations mean.\n"
        f"* Lydia desires to be able to predict the sales price "
        f"of her 4 inherited houses, "
        f"as well as any other house in Ames, Iowa, that she will consider to "
        f"buy or sell in the future. The criteria for this is trained model with an R2 Score equal to or greater than 0.75."
    )
    st.info(
        f"By the end of this project. We can confidently say that all requirements have been met.\n"
        f"* We have successfully identified which features correlate to the Sales Price.\n"
        f"* We have created plots to help visualise these variables and between the Sales Price study page and the ML page, "
        f"we have summerised what these findings mean.\n"
        f"* We have been succesful in creating predictions of the Sales Price for the clients 4 inherited houses.\n"
        f"* And we have been successfully in using a model with the required accuracy to predict on any unseen data for potentail future housing purchases."
    )

    st.info(
        f"In conclusion, our project successfully utilized a regression model to predict the sales price of houses within the area of Ames, Iowa with a high degree of accuracy. "
        f"By incorporating a variety of features such as Square Footage, Kitchen Quality, Year Built, and other relevant factors, "
        f"we were able to build a model that could accurately predict housing sales price. "
        f"We validated our model extensively and found that it consistently outperformed other models in terms of accuracy. "
        f"The project has significant practical applications for anyone looking to get into the real estate industry, "
        f"as it can help buyers and sellers make informed decisions based on reliable price predictions. "
        f"This project has demonstrated the effectiveness of machine learning techniques in solving real-world problems."
    )
