from google.cloud.functions_v1 import CloudFunctionsServiceClient, ListFunctionsRequest
import google.oauth2.credentials

def list_functions(access_token, project_id):

    credentials = google.oauth2.credentials.Credentials(access_token)
    client = CloudFunctionsServiceClient(credentials=credentials)
    parent = f"projects/{project_id}/locations/-"
 
    print("\n[+] List Cloud Functions (--list)")

    try:
        functions = client.list_functions(request={"parent": parent})
        any_functions_present = False
        for function in functions:
            any_functions_present = True
            trigger_type = "HTTP Trigger"
            if function.event_trigger:
                trigger_type = function.event_trigger.event_type
            docker_registry = "0"
            if function.source_repository and "docker" in function.source_repository.url:
                docker_registry = "1"
            ingress_settings = "ALLOW_ALL" if function.ingress_settings == 1 else ("ALLOW_INTERNAL_AND_GCLB" if function.ingress_settings == 3 else "ALLOW_INTERNAL_ONLY")
            function_status = "ACTIVE" if function.status == 1 else ("UPDATE_IN_PROGRESS" if function.status == 2 else ("DEPLOY_IN_PROGRESS" if function.status == 3 else ("DELETE_IN_PROGRESS" if function.status == 4 else "ERROR")))
            sec_level = "SECURE_ALWAYS" if function.https_trigger.security_level == 1 else "SECURE_OPTIONAL"
            dockreg = "CONTAINER_REGISTRY" if function.docker_registry == 1 else "ARTIFACT_REGISTRY"
            deployment_tool = function.labels.get('deployment-tool', '')

            print(f"    Name: {function.name}")
            print(f"        Trigger Type: {trigger_type}")
            print(f"            URL: {function.https_trigger.url}")
            print(f"            Security Level: {sec_level}")
            print(f"        Status: {function_status}")
            print(f"        Entry Point: {function.entry_point}")
            print(f"        Timeout: {function.timeout.seconds} second(s)")
            print(f"        Available Memory: {function.available_memory_mb} MB")
            print(f"        Service Account Email: {function.service_account_email}")
            print(f"        Update Time: {function.update_time}")
            print(f"        Version ID: {function.version_id}")
            #print(f"    Labels: {function.labels}")
            print(f"        Deployment Tool: {deployment_tool}")
            print(f"        Source Upload URL: {function.source_upload_url}")
            print(f"        Source Archive URL: {function.source_archive_url}")
            print(f"        Source Repo:")
            print(f"            URL: {function.source_repository.url}")
            print(f"            Deployed URL: {function.source_repository.deployed_url}")
            print(f"        Runtime: {function.runtime}")
            print(f"        Ingress Settings: {ingress_settings}")
            print(f"        Build ID: {function.build_id}")
            print(f"        Build Name: {function.build_name}")
            print(f"        Docker Registry: {dockreg}")
            print()

        if not any_functions_present:
            print("    No cloud functions present.")
            
    except Exception as e:
        if "cloudfunctions.googleapis.com" in str(e):
            print("     - Cloud Function API is disabled, please enable it and try again.")
        else:
            print(f"    - Error: {str(e)}")



