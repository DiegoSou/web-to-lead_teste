import streamlit as st
import requests

st.write('Hello World now')
st.write('Your public secret is: ' + st.secrets["PUBLIC_API_KEY"])


with st.form("web_to_lead_form"):
    st.write('Testing salesforce web-to-lead form')
    
    # forms
    first_name = st.text_input("first_name", value="")
    last_name = st.text_input("last_name", value="")
    email = st.text_input("email", value="")
    company = st.text_input("company", value="")
    city = st.text_input("city", value="")
    state = st.text_input("state", value="")
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        requestUrl = st.secrets["WEB_TO_LEAD_URL"]
        body = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "company": company,
            "city": city,
            "state": state
        }
        for key in body:
            requestUrl += "&" + key + "=" + body[key]
            
        response = requests.get(requestUrl)
        st.write("Submitted", response)
        st.write("Submitted", requestUrl)

       