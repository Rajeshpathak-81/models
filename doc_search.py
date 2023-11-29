

import streamlit as st
import requests
import json
url = 'http://127.0.0.1:8000/answers'
headers = {
    'accept': 'application/json'
}


# Streamlit UI
# ===============
st.set_page_config(page_title="Doc Searcher", page_icon=":robot:")
st.header("Query PDF Source")

form_input = st.text_input('Enter Query')
submit = st.button("Generate")

if submit:
        params = {
        'query': form_input       
    }

        response = requests.post(url, headers=headers, data=json.dumps(params))

        res=response.json()
        st.write(res['answer'])