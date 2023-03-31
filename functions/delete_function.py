from google.cloud.functions_v1 import CloudFunctionsServiceClient
import google.oauth2.credentials

def delete_function(access_token, project_id, location, function_name):
    credentials = google.oauth2.credentials.Credentials(access_token)
    client = CloudFunctionsServiceClient(credentials=credentials)

    function_path = f"projects/{project_id}/locations/{location}/functions/{function_name}"

    print("\n[+] Cloud Function Delete (--delete)")
    try:
        response = client.delete_function(name=function_path)
        print(f"    - Deleting Cloud Function: {function_name}")
        response.result()
        print(f"    - Cloud Function {function_name} deleted successfully")

    except Exception as e:
        if "cloudfunctions.googleapis.com" in str(e):
            print("     - Cloud Function API is disabled, please enable it and try again.") 
            print("     - Run 'gcloud services enable cloudfunctions.googleapis.com' to enable Cloud Function API")
       
        elif "'cloudfunctions.functions.delete' denied" in str(e):
            print(f"    - You can't delete the Cloud Function {function_name} since you don't have the 'cloudfunctions.functions.delete' permission")
        else:
            print(f"    - Error: {str(e)}")
