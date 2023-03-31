from google.cloud.functions_v1 import CloudFunctionsServiceClient, CloudFunction, CreateFunctionRequest
import google.oauth2.credentials
#from service_status.cloudbuild_status import cloudbuild_status

def deploy_function(access_token, project_id, location, function_name, gsutil_uri, function_entry_point, service_account):
    credentials = google.oauth2.credentials.Credentials(access_token)
    client = CloudFunctionsServiceClient(credentials=credentials)

    url = "https://{}-{}.cloudfunctions.net/{}".format(location, project_id, function_name)

    function = CloudFunction(
        name="projects/{}/locations/{}/functions/{}".format(project_id, location, function_name),
        source_archive_url="{}".format(gsutil_uri),
        entry_point=function_entry_point,
        runtime="python38",
        service_account_email=service_account,
        https_trigger={},
    )

    request = CreateFunctionRequest(location="projects/{}/locations/{}".format(project_id, location), function=function)
    print("\n[+] Cloud Function Deploy (--deploy)")
    try:
        response = client.create_function(request=request)
        print("    - Cloud Function creation has started")
        print("    - Takes 1-2 minutes to create")
        result = response.result()
        print(f"    - Function Invocation URL: {url}")

    except Exception as e:
        if "cloudfunctions.googleapis.com" in str(e):
            #print(f"    - Error: {str(e)}")
            print("    - Cloud Function API is disabled, please enable it and try again.")
            print("    - Function can't be Deployed/Updated.")
            print("    - Run 'gcloud services enable cloudfunctions.googleapis.com' to enable Cloud Function API")
        elif "cloudfunctions.operations.get" in str(e):
            print("    - Permission cloudfunctions.operations.get denied (Not an Issue)")
            print(f"    - Function Invocation URL: {url}")
        else:
            print(f"    - Error: {str(e)}")
        #cloudbuild_status(project_id, access_token)
