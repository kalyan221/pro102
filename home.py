# Create the Page Navigator for 'Home', 'Predict Diabetes' and 'Visualise Decision Tree' web pages in 'diabetes_main.py'
# Import the 'diabetes_predict' 'diabetes_home', 'diabetes_plots' Python files
import diabetes_home
import diabetes_predict
import diabetes_plots


# Adding a navigation in the sidebar using radio buttons
# Create the 'pages_dict' dictionary to navigate.
pages_dict = {"Home": diabetes_home, 
           "Predict Diabetes": diabetes_predict, 
           "Visualise Decision Tree": diabetes_plots}
# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.title("Navigation")
user_choice = st.sidebar.radio("Go to",tuple(pages_dict.keys()))

if user_choice =="Home":
    diabetes_home.app()
else:
    selected_page = pages_dict[user_choice]
    selected_page.app(diabetes_df)



# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    st.title("Early Diabetes Prediction Web App")
    # Provide a brief description for the web app.
    st.markdown("""<p style='color:red;font-size:25px'> Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
                There is not a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
                This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier. </p>""",
                unsafe_allow_html = True)

    # Add the 'beta_expander' to view full dataset 
    st.header("View Data")
    with st.beta_expander("View Dataset"):
        st.table(diabetes_df)

    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
    
    st.subheader("Columns description")
    if st.checkbox("Show Summary"):
        st.table(diabetes_df.describe())
        
    col1,col2,col3 = st.beta_columns(3)

   
    with col1:
        if st.checkbox("Show all columns names"):
            st.table(list(diabetes_df.columns))

    # Add a checkbox in the second column. Display the column data-types of 'diabetes_df' on the click of checkbox.
    with col2:
        if st.checkbox("Show all columns data-types"):
            st.table(diabetes_df.dtypes)

    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with col3:
        if st.checkbox("View columns Data"):
            st.table(diabetes_df.columns)
            columns_data = st.checkbox(("Select Columns",tuple(diabetes_df.columns)))
            st.write(diabetes_df[columns_data])    