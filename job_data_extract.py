import json
import random
from google.cloud import storage

# Generate 100 job positions
def generate_job_positions(num_positions):
    job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "UX Designer", "Sales Engineer",
                  "Marketing Manager", "HR Specialist", "Customer Support", "DevOps Engineer", "Business Analyst"]
    companies = ["Company A", "Company B", "Company C", "Company D", "Company E"]
    locations = ["New York", "San Francisco", "Chicago", "Los Angeles", "Seattle"]

    positions = []
    for i in range(num_positions):
        position = {
            "id": i + 1,
            "title": random.choice(job_titles),
            "company": random.choice(companies),
            "location": random.choice(locations),
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "salary": f"${random.randint(60000, 120000)}"
        }
        positions.append(position)
    
    return positions

# Save the job positions to a JSON file
def save_to_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Upload the JSON file to Google Cloud Storage
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    # Initialize a client
    client = storage.Client()
    
    # Get the bucket
    bucket = client.bucket(bucket_name)
    
    # Create a blob object from the file
    blob = bucket.blob(destination_blob_name)
    
    # Upload the file
    blob.upload_from_filename(source_file_name)
    
    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

# Main function
def main():
    num_positions = 100
    filename = 'job_positions.json'
    
    # Generate data and save to file
    job_positions = generate_job_positions(num_positions)
    save_to_json_file(job_positions, filename)
    
    # Define GCS bucket name and destination path
    # bucket_name = 'your-gcs-bucket-name'
    # destination_blob_name = 'job_positions.json'
    
    # Upload to GCS
    # upload_to_gcs(bucket_name, filename, destination_blob_name)

if __name__ == "__main__":
    main()
