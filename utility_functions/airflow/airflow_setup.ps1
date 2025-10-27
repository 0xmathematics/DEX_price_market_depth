# Setup Airflow in a Miniconda environment on Windows



# 2. Set version variables
set AIRFLOW_VERSION = 3.0.0
set PYTHON_VERSION = 3.12
set CONSTRAINT_URL = https://raw.githubusercontent.com/apache/airflow/constraints-%AIRFLOW_VERSION%/constraints-%PYTHON_VERSION%.txt

# 3. Install Airflow using constraints
pip install apache-airflow==%AIRFLOW_VERSION% --constraint %CONSTRAINT_URL%


pip install "apache-airflow==3.0.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.0/constraints-3.12.txt"