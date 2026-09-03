# Flask Azure Insights Lab — Simulating Migration & Monitoring


This project demonstrates a simple Flask API integrated with Azure Application Insights using OpenCensus.  
It logs custom messages and traces all incoming requests automatically.

## 📦 Setup

Clone the repository:
```bash
git clone https://github.com/<your-username>/flask_app.git
cd flask_app

Step 2: Add '.gitignore'
If you haven't already:

vim .gitignore

Then add:

venv/
__pycache__/
*.pyc

3-Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the App

4-Start the Flask server:

python api.py
Test endpoints with curl:

curl http://localhost:5000/hello
curl http://localhost:5000/error

/hello → Logs an INFO message (“Hello endpoint called”).

/error → Triggers a division by zero, logs an ERROR, and returns HTTP 500.

5-Monitor in Azure
Telemetry is sent to Application Insights (devops-monitor resource).
Open Logs (KQL) in the Azure Portal and run these queries:

Recent traces:

kusto
traces | order by timestamp desc
Requests per endpoint:

kusto
requests | summarize count() by name, resultCode
Exceptions:

kusto
exceptions | order by timestamp desc

##

<img width="1871" height="863" alt="image" src="https://github.com/user-attachments/assets/175a0201-4058-4996-a05e-eb347158b7d8" />


## Final Summary — What This Lab Demonstrates

This project is more than just a dummy Flask app. It shows how to connect a simple Python service to **Azure Application Insights** and use it as a playground for monitoring and migration concepts.

### What We Built
- A **Flask web server** with two endpoints:
  - `/hello` → behaves like a **new microservice**, stable and logging INFO messages.
  - `/error` → behaves like a **legacy service**, prone to failure, logging ERROR messages.
- **Custom logging** with `AzureLogHandler` → sends INFO/ERROR logs to the `traces` table.
- **Automatic request tracing** with `FlaskMiddleware` → every HTTP call is captured in the `requests` table.
- **Exception monitoring** → errors can be surfaced in the `exceptions` table.

### Migration Simulation
This setup mimics the **Strangler Fig pattern**:
- Old functionality (`/error`) continues to run but is clearly separated in telemetry.
- New functionality (`/hello`) is introduced alongside it, with its own clean logs.
- By querying telemetry, you can **see traffic split between old and new routes**, just like in a gradual migration.

### Practicing KQL
We used **KQL queries** to explore telemetry:
```kusto
traces | order by timestamp desc
requests | summarize count() by name, resultCode
exceptions | order by timestamp desc
