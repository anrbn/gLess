from google.iam.v1.policy_pb2 import Policy, Binding
from google.cloud.functions_v1 import CloudFunctionsServiceClient
import google.oauth2.credentials

def set_iam_binding(access_token, location, function_name, project_id, principalname):
    
    url = "https://{}-{}.cloudfunctions.net/{}".format(location, project_id, function_name)
    credentials = google.oauth2.credentials.Credentials(access_token)
    client = CloudFunctionsServiceClient(credentials=credentials)

    name="projects/{}/locations/{}/functions/{}".format(project_id, location, function_name)

    if "@" in principalname:
        binding = Binding(
            role="roles/cloudfunctions.invoker",
            members=[f"serviceAccount:{principalname}"],
        )
    else:
        binding = Binding(
            role="roles/cloudfunctions.invoker",
            members=[principalname],
        )

    policy = Policy(bindings=[binding])
    print("\n[+] Set IAM Bind (--setiambinding)")
    try:
        response = client.set_iam_policy(request={"resource": name, "policy": policy})
        print(f"    - IAM Policy Binding has been set on {function_name}")
        print(f"    - Function Invocation URL: {url}")

    except Exception as e:
        if "'cloudfunctions.functions.setIamPolicy' denied" in str(e):
            print("    - You can't set IAM Policy Binding since you don't have the 'cloudfunctions.functions.setIamPolicy' Permission")
        else:
            print(f"    - Error: {str(e)}")
