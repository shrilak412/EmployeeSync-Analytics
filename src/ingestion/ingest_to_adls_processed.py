from azure.storage.blob import BlobServiceClient, ContentSettings
import os
from dotenv import load_dotenv
load_dotenv()
# Replace with your Azure Storage connection string
CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "processed-data"

def upload_folder_to_adls(local_folder_path, remote_folder_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Create container if it doesn't exist
        try:
            container_client.create_container()
            print(f"Container '{CONTAINER_NAME}' created.")
        except Exception:
            pass  # Container likely already exists

        for root, _, files in os.walk(local_folder_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                # Create blob name with remote folder path
                relative_path = os.path.relpath(local_file_path, local_folder_path)
                blob_path = os.path.join(remote_folder_name, relative_path).replace("\\", "/")

                with open(local_file_path, "rb") as data:
                    container_client.upload_blob(
                        name=blob_path,
                        data=data,
                        overwrite=True,
                        content_settings=ContentSettings(content_type="application/octet-stream")
                    )
                print(f"Uploaded '{blob_path}'")

        print("\n✅ Upload complete.")
    except Exception as e:
        print("❌ Error during upload:", e)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder_to_upload = os.path.join(current_dir, "..", "..", "data", "processed_hr_data")
    upload_folder_to_adls(folder_to_upload, "processed_hr_data")
