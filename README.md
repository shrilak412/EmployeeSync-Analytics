📊 Employee Sync Analytics
A modern data engineering pipeline that ingests, transforms, and visualizes HR metrics using Azure Data Lake, PySpark, and Synapse Analytics.
A scalable, cloud-based HR analytics pipeline that ingests, transforms, and visualizes employee data using Azure Data Lake, PySpark, and Synapse Analytics.
🚀 Project Overview
This project simulates an end-to-end data pipeline designed to:

✅ Ingest HR datasets from local sources to Azure Data Lake Gen2.

🔁 Transform raw CSV and JSON files using PySpark.

📦 Store processed data in Parquet format.

📊 Analyze insights using Power BI and Synapse SQL.

🔁 Prepare for CI/CD with Azure DevOps YAML pipelines.

🧱 Tech Stack
Layer	Tools & Services Used
💻 Development:	Python, VS Code, Git
☁️ Cloud:	Azure Blob Storage, Azure Synapse, Power BI
⚙️ Processing:	PySpark, Pandas, Scikit-learn (for AI models)
🔁 CI/CD:	Azure Pipelines (YAML)

📁 Project Structure
EmployeeSync-Analytics/
│
├── data/                    # Raw and processed data
│   ├── HRDataset_v14.csv
│   └── processed_hr_data/
│
├── src/
│   ├── ingestion/           # Upload to Azure Blob
│   ├── processing/          # Spark transformation scripts
│   ├── analytics/           # Synapse SQL queries
│   ├── ai/                  # (Optional) ML model scripts
│   └── visualization/       # Power BI .pbix dashboards
│
├── pipelines/               # Azure DevOps CI/CD YAML
├── .gitignore
├── README.md
└── requirements.txt

![spark](https://github.com/user-attachments/assets/75abe345-46da-4a03-b852-f75da3228e99)

