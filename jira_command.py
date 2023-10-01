import streamlit as st
import requests
import pandas as pd
import json

# Outerbase Command URL
OUTERBASE_API_URL = "https://arbitrary-fuchsia.cmd.outerbase.io/issues"

# Function to fetch Jira issues
def fetch_jira_issues():
    try:
        response = requests.get(OUTERBASE_API_URL)
        response.raise_for_status()
        issues = response.json()
        return issues
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching Jira issues: {e}")
        return []

# Main Streamlit app
def main():
    st.title("Jira Issues Viewer - Outerbase")

    st.write("This app fetches Jira issues from the Outerbase Integrations URL.")
    if st.button("Fetch Jira Issues"):
        # Fetch and display Jira issues
        results = fetch_jira_issues()
        data = json.loads(results)
        fields = ["key", "fields.summary","fields.status.name", "fields.reporter.name","fields.assignee.name","fields.priority.name"]
        df = pd.json_normalize(data['issues'])
        df = df[fields]
        st.dataframe(df)
      
if __name__ == "__main__":
    main()
