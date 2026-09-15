# API ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that retrieves data from an external API, processes and transforms the data using Python, and loads the final dataset into a SQL Server database.

This project demonstrates a practical data engineering workflow involving **API integration, data transformation, database connectivity, and automated data loading**.

## Architecture

```text
External API
     ↓
   Extract
     ↓
Python ETL Pipeline
     ↓
  Transform
     ↓
Processed Data
     ↓
     Load
     ↓
SQL Server Database
```

## Project Workflow

### 1. Extract

The pipeline connects to an external API using Python and retrieves the required data.

* API requests are handled using the `requests` library.
* JSON responses are received from the API.
* The required fields are extracted from the API response.

### 2. Transform

The extracted JSON data is processed and prepared for database storage.

The transformation process includes:

* Parsing JSON responses
* Extracting relevant fields
* Structuring the data
* Handling the retrieved values
* Preparing the data for SQL insertion

### 3. Load

The transformed data is loaded into a **SQL Server** database.

Python establishes the database connection and inserts the processed records into the appropriate SQL table.

## Technologies Used

* **Python**
* **REST API**
* **JSON**
* **Requests**
* **SQL Server**
* **T-SQL**
* **Python Database Connectivity**

## Project Structure

```text
api-etl-pipeline/
│
├── api_pipeline.py       # Extracts data from the API and processes it
├── load_sql.py            # Loads processed data into SQL Server
├── sql_connection.py      # Handles SQL Server database connection
├── requirements.txt       # Python dependencies
├── .gitignore             # Files excluded from Git
└── README.md              # Project documentation
```

## Prerequisites

Before running the project, make sure you have:

* Python 3.x
* SQL Server
* SQL Server Management Studio (SSMS)
* An active internet connection
* Required Python packages

## Installation

Clone the repository:

```bash
git clone https://github.com/rohitshinde15/api-etl-pipeline.git
```

Navigate to the project directory:

```bash
cd api-etl-pipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Database Configuration

Create the required database and table in SQL Server.

Update the database connection configuration in the project according to your local SQL Server environment.

**Do not commit passwords, API keys, connection strings, or other sensitive credentials to GitHub.**

For production-style projects, environment variables or a `.env` file should be used for sensitive configuration.

## Running the Pipeline

Run the main pipeline:

```bash
python api_pipeline.py
```

The pipeline will:

1. Connect to the external API
2. Retrieve the data
3. Process the API response
4. Prepare the transformed data
5. Connect to SQL Server
6. Load the data into the database

## Key Data Engineering Concepts Demonstrated

This project demonstrates several concepts relevant to entry-level Data Engineering roles:

* REST API integration
* Data extraction
* JSON data processing
* ETL pipeline development
* Data transformation
* SQL Server integration
* Python database connectivity
* Error handling
* Modular Python programming
* Virtual environment and dependency management

## Future Improvements

Possible improvements to the pipeline include:

* Add logging using Python's `logging` module
* Move credentials to environment variables
* Add data validation
* Implement retry logic for failed API requests
* Add incremental data loading
* Add automated scheduling using Apache Airflow
* Containerize the pipeline using Docker
* Add unit and integration tests
* Store pipeline configuration separately from the application code

## Author

**Rohit Shinde**

Aspiring Data Engineer focused on **Python, SQL, ETL pipelines, and data engineering technologies**.

GitHub: [rohitshinde15](https://github.com/rohitshinde15)

