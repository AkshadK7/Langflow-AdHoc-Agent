# Langflow-AdHoc-Agent

An interactive application leveraging Langflow for dynamic SQL query generation and execution on user-provided datasets.

## Overview

The **Langflow-AdHoc-Agent** allows users to generate and execute SQL queries dynamically on their datasets through a simple and interactive interface. The project utilizes **Langflow**, **Streamlit**, and **SQLite** to streamline ad-hoc querying of structured data. 

With **Retrieval-Augmented Generation (RAG)**, the application enhances query formulation and execution, making it accessible to both technical and non-technical users.

---

## Features

- **Ad-Hoc SQL Querying**  
  Automatically generate and execute SQL queries on structured data using Langflow.
- **Interactive User Interface**  
  A simple and intuitive Streamlit UI to upload, process, and query datasets.
- **Automated Schema Generation**  
  Convert user-provided CSV files into an SQLite database with structured tables.
- **Natural Language Processing**  
  Allows users to ask questions in natural language, which is then converted into SQL queries.
- **Example Queries and Schema**  
  Sample queries and dataset schema for reference and testing.

---

## Requirements

- **Python**: 3.11.4
- **pip**: 24.0
- **Libraries**:
  - `sqlite3`
  - `pandas`
  - `streamlit`
  - `langflow`
  - `python-dotenv`

---

## Setup Instructions

### **1. Clone the Repository**
```bash
git clone https://github.com/AkshadK7/Langflow-AdHoc-Agent.git
cd Langflow-AdHoc-Agent
```

### **2. Create Environment Variables**
Create a `.env` file in the project root and add your **Google Gemini API credentials**.

### **3. Prepare Langflow Configuration**
Create a `T2SQL_Flow.json` file and copy the JSON flow from **Langflow** into it.

### **4. Insert Your Dataset**
Place your CSV file in the `/data` directory.

### **5. Set Up Virtual Environment**
```bash
conda create --name env_name
conda activate env_name
```

### **6. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **7. Install Langflow (if not installed)**
```bash
pip install langflow
```
*If the installation is slow, use:*
```bash
pip install uv
uv pip install langflow
```

### **8. Convert CSV to Database**
```bash
python create_db.py
```

### **9. Run the Application**
```bash
streamlit run app.py
```

---

## Example Usage

### **Sample Dataset (`user_data.csv`)**
| user_id | first_name | last_name | email | city | country | age | annual_income | job_title | department |
|---------|------------|-----------|-----------------|---------------|---------|-----|--------------|------------------|-----------|
| 1       | John       | Doe       | john.doe@example.com | New York    | USA     | 34  | 85000        | Software Engineer | IT        |
| 6       | Sarah      | Lewis     | sarah.lewis@example.com | Berlin      | Germany | 27  | 72000        | UI/UX Designer    | Design    |
| 17      | Mason      | Phillips  | mason.phillips@example.com | Shanghai   | China   | 32  | 83000        | AI Engineer       | AI        |
| 25      | Alexander  | Carter    | alexander.carter@example.com | Helsinki   | Finland | 38  | 84000        | Product Designer  | Design    |

### **Ad-Hoc Query Example**
#### **Question:**
*"Can I get the list of people working in the Design Department?"*

#### **Generated SQL Query**
```sql
SELECT first_name, last_name, email, job_title
FROM user_data
WHERE department = 'Design';
```

#### **Result**
| first_name | last_name | email                       | job_title         |
|------------|----------|----------------------------|-------------------|
| Sarah      | Lewis    | sarah.lewis@example.com    | UI/UX Designer   |
| Alexander  | Carter   | alexander.carter@example.com | Product Designer |

---

## Future Enhancements
- **Integration with More Databases**: Support for PostgreSQL and MySQL.
- **Advanced NLP Models**: Improve SQL generation accuracy using GPT-4 or Transformer-based models.
- **Multi-Language Support**: Process queries in multiple languages.
- **Data Visualization**: Generate charts and graphs for better insights.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/AkshadK7/Langflow-AdHoc-Agent/blob/master/LICENSE) file for details.

---

## Acknowledgements

Special thanks to the **Langflow** team and the **open-source community** for their contributions.

---
🚀 **Enhance your SQL querying experience with Langflow-AdHoc-Agent!** 🚀

