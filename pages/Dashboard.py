'''
    Coal Thermal Power Plant Use Cases
        1. Prediction of Turbine Load 
        2. Prediction of Turbine Maintenance needed or not
        3. Prediction of Boiler Maintenance needed or not
        4. Prediction of Generator Maintenance needed or not

'''
# Import All the libraries in intro file
from intro import *


# Import the CSV file which contain Dummy data
df1 = pd.read_csv("data/turbine_data_thermal.csv")


# Styles to remove unncessary things created by Streamlit
remove_header = """
<style>
    header{
        display: none;
    }
    .st-emotion-cache-gqgagh {
        display: none;
    }
    .st-emotion-cache-wa2l1v {
        display: none;
    }
    .st-emotion-cache-10oheav {
        padding: 3rem 1rem;
    }


</style>

"""

st.markdown(remove_header, unsafe_allow_html=True)

add_template = st.button("Add Template")

if add_template:
    equipment_name = st.text_input("Equipment Name: ")
    use_case = st.text_input("Use case: ")
    no_of_features = st.number_input("Number of Features: ")
    index = 1
    for feature in no_of_features:
        st.text("Enter Feature")
        feature= st.text_input
        index += 1

predict =  st.selectbox("Select Usecase",
                        ('Turbine Load Prediction','Turbine Maintenance')
                        )

# User will select one specific date and
# we will only display the data & graphs only specific to that date
unique_dates = df1['Timestamp'].str.split(' ').str[0].unique()
print(unique_dates, type(unique_dates))
user_selected_date = st.selectbox("Select Date: ", unique_dates)


# User selects whether he wants to see the data in visual format / text format
option = st.radio("select How you want to See Data",
                  ["Graphs", "Table"]
                  )
# ----------------------Streamlit Sidebar things end here-----------------------

# if option == "Graphs":
#     profile = ProfileReport(df1)
#     st_profile_report(profile)

