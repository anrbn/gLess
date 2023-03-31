import google.oauth2.credentials
from googleapiclient import discovery, errors

def cloudbuild_status(project_id, access_token):
    try:
        credentials = google.oauth2.credentials.Credentials(access_token)
        cloudbuild = discovery.build('cloudbuild', 'v1', credentials=credentials, cache_discovery=False)
        request = cloudbuild.projects().triggers().list(projectId=project_id)
        request.execute()
        print("     - Cloud Build API is enabled.")
    except errors.HttpError as error:
        if error.resp.status == 403 and 'cloudbuild.googleapis.com' in str(error):
            print("    - Cloud Build API is disabled, please enable it and try again.")
            print("    - Function Deploy/Update will Fail.")
            print("    - Run 'gcloud services enable cloudbuild.googleapis.com' to enable Cloud Build API")
        else:
            raise error
    