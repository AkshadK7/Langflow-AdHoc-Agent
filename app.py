import streamlit as st
import sqlite3
import pandas as pd
from langflow.load import run_flow_from_json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def t2sql_agent(input_query, input_schema):
    TWEAKS = {
        "TextInput-xeeGE": {
            "input_value": input_query
        },
        "TextInput-CmrfW": {
            "input_value": input_schema
        },
        "Prompt-zv0HU": {},
        "GoogleGenerativeAIModel-GV3Qc": {},
        "TextOutput-EJvKP": {}
    }

    result = run_flow_from_json(
        flow="T2SQL_Flow.json",
        input_value="message",
        session_id="",  # Provide a session id if you want to use session state
        fallback_to_env_vars=True,  # False by default
        tweaks=TWEAKS
    )

    raw_sql_output = result[0].outputs[0].results["text"].data["text"]

    # Remove 'sql' directive, backticks and any surrounding whitespace
    formatted_sql = raw_sql_output.replace("sql\n", "").strip("`").strip()

    return formatted_sql



def execute_query(database, query):
    """Executes a SQL query on the given SQLite database."""
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()
        return results, columns
    except Exception as e:
        return str(e), []

# Streamlit UI Header
st.title("Ad-Hoc Agent")

# Input Fields
input_query = st.text_area("Ad-Hoc Question:", placeholder="Enter your question here")
input_schema = st.text_area("Table Schema:", placeholder="Enter your table schema here")

# Output Field
if st.button("Generate SQL Query"):
    if input_query and input_schema:
        try:
            output_sql_query = t2sql_agent(input_query, input_schema)
            st.success("SQL Query Generated Successfully!")
            st.text_area("Result:", output_sql_query, height=200)

            # Query Execution
            # database = st.text_input("SQLite Database Path:", placeholder="Enter the path to your SQLite database")
            database = "./user_db.sqlite"
            if database:
                query_results, columns = execute_query(database, output_sql_query)
                if isinstance(query_results, str):
                    st.error(f"Query Execution Error: {query_results}")
                else:
                    st.write("Query Results:")
                    if query_results:
                        st.dataframe(pd.DataFrame(query_results, columns=columns))
                    else:
                        st.write("No data returned from the query.")
            else:
                st.warning("Please provide the path to the SQLite database to execute the query")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in both the Ad-Hoc Question and Table Schema fields.")
