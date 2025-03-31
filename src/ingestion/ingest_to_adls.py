from azure.storage.blob import BlobServiceClient
import os
from pathlib import Path
from dotenv import load_dotenv
dotenv_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(dotenv_path)

# Replace with your actual Azure Storage connection string
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
# Specify the container name where you want to upload the file
CONTAINER_NAME = "raw-data"

def upload_to_adls(file_path, blob_name):
    try:
        # Create a BlobServiceClient object using the connection string.
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        # Get a container client to interact with the specified container.
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        
        # Optionally, create the container if it doesn't exist.
        try:
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' created.")
        except Exception as e:
            # If the container already exists, this exception can be safely ignored.
            pass
        
        # Open the file and upload its content as a blob.
        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
        print(f"Uploaded '{blob_name}' to ADLS successfully.")
    except Exception as e:
        print("Error during upload:", e)

if __name__ == "__main__":
    # Construct the path to your cleaned Kaggle CSV file located in the data folder.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "..", "data", "HRDataset_v14.csv")
    blob_name = "HRDataset_v14.csv"  # Change to "kaggle_cleaned.csv" if that is your intended name.
    
    # Call the function to upload the file.
    upload_to_adls(file_path, blob_name)
