from intro import *

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

st.title("Thermal Power plants")

st.text('''
    Thermal power plants are the most common type of power plant in the world, 
    accounting for about 60% of global Electricity Generation 


''')


