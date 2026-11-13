# Locust Practice Scripts

A collection of small Python examples for learning Locust load testing and related concepts.

## Setup

Requires Python 3 and Git. From this folder, create and activate a virtual environment, then install Locust:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install locust
```

Run a Locust example with:

```powershell
locust -f <script-name>.py
```

Replace `<script-name>.py` with the example you want to run. Check the script's host and settings before starting a test, and only send load to systems you own or are authorized to test.

## Data parameterization example

`dataParameterization.py` reads `cust-data.csv`. That local file is excluded from Git because it may contain personal data. To use the example, copy the sanitized template and edit it with test data:

```powershell
Copy-Item cust-data.example.csv cust-data.csv
```

Do not commit real names, phone numbers, email addresses, credentials, or other private data.
