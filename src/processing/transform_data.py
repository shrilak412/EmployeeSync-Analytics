from pyspark.sql import SparkSession
import os

# Create Spark session
spark = SparkSession.builder.appName("EmployeeSync").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")  # Reduce verbosity

# Construct absolute file path to CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "..", "..", "data", "HRDataset_v14.csv")
csv_file_uri = f"file:///{os.path.abspath(csv_file_path).replace(os.sep, '/')}"

print("📥 Reading CSV from:", csv_file_uri)

# Load CSV into Spark DataFrame
df = spark.read.csv(csv_file_uri, header=True, inferSchema=True)

# Rename column
df = df.withColumnRenamed("EmpID", "employee_id")

# Select necessary columns
df_selected = df.select("employee_id", "Employee_Name", "Department", "Position", "Salary")

# Group by Department and get average salary
df_grouped = df_selected.groupBy("Department").avg("Salary") \
    .withColumnRenamed("avg(Salary)", "avg_salary")

# Output directory for parquet
output_path = os.path.join(current_dir, "..", "..", "data", "processed_hr_data")
output_uri = f"file:///{os.path.abspath(output_path).replace(os.sep, '/')}"

print("📤 Saving output to:", output_uri)

# Write the data safely
try:
    df_grouped.write.parquet(output_uri, mode="overwrite")
    print("✅ Processed data saved at:", output_uri)
except Exception as e:
    print("❌ Error during Parquet write:\n", e)

# Stop Spark session
spark.stop()

