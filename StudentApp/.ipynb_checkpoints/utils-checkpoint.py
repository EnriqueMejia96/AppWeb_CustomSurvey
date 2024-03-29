from google.cloud import storage
from typing import Tuple, Any

def split_gcs_path(gcs_path:str) -> Tuple[str, str]:
    from urllib.parse import urlsplit
    # Split the URL components
    url_parts = urlsplit(gcs_path.replace('/gcs/','gs://')) #Replace some inconsistency
    # Extract the bucket name
    bucket_name = url_parts.netloc
    # Extract the blob_name (excluding the leading '/')
    blob_name = url_parts.path[1:]
    
    return bucket_name, blob_name

def upload_file(source_local:str, destination_gcs:str) -> None:
    # Initialize the GCS client
    storage_client = storage.Client()
    #Split gcs path
    bucket_name, blob_name = split_gcs_path(destination_gcs)
    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    # Upload file
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(source_local)
