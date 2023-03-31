# gLess
gLess aims to eliminate bloated and unnecessary permissions that are often encountered when performing tasks with gCloud. gLess leverage gRPC to directly interact with the Cloud Function API and execute tasks with only the required set of permissions.

## Tools Purpose

gLess aims to remove any unnecessary permissions which are typically needed by gCloud for performing certain tasks. For instance, deploying a Cloud Function using Cloud Storage via gCloud requires the following permissions:

- iam.serviceAccounts.actAs
- cloudfunctions.functions.create
- cloudfunctions.functions.get

However, one might wonder why cloudfunctions.functions.get is needed for deploying a function, as it primarily serves to view details of already deployed functions. gLess addresses this issue by doing the task with only the requiring set of permissions. Compared to gCloud, gLess would require the following permissions:

- iam.serviceAccounts.actAs
- cloudfunctions.functions.create

By eliminating bloated permissions, gLess does more/same with less :)

## Requirements and Compatibility:
gLess is developed using Python 3 and requires Python 3 to run. It is compatible with both Windows and Unix-based systems.

## Usage

```
Arguments:
      --project-id                 Project ID : Specify the Project ID
      
      --location                   Region : Function Location/Region
      
      --function-name              Function's Name : Name of the Function to Deploy, Update, Delete etc.
      
      --gsutil-uri                 Cloud Storage URI : Cloud Storage URI pointing to the ZIP File uploaded 
      
      --function-entry-point       Function's Entry Point : Function's Entry point
      
      --service-account            Service Account : Service Account the Cloud Function should use
      
      --checkperm                  Check's Permissions : Check if user has required Permissions to 
                                   play around with Cloud Functions
                                   Requires the following arguments:
                                   --project-id
      
      --list                       List's Cloud Functions : List the Cloud Functions running in the Project 
                                   Requires the following arguments:
                                   --project-id
      
      --deploy                     Deploy's Function : Deploys a Function
                                   Requires the following arguments:
                                   --project-id, --location, --function-name, --gsutil-uri, 
                                   --function-entry-point, --service-account
      
      --update                     Update Function : Updates an Existing Function 
                                   Requires the following arguments:
                                   --project-id, --location, --function-name, --gsutil-uri, 
                                   --function-entry-point, --service-account
      
      --delete                     Delete Function : Deletes an Existing Function
                                   Requires the following arguments:  
                                   --project-id, --location, --function-name    
      
      --createsakey                Create Service Account Key : Creates and Downloads a Service Account Key
                                   Requires the following arguments:
                                   --project-id
                                   
      --setiambinding              Set IAM Binding : Binds an IAM Policy to a Function requires specifying 
                                   the principal name (e.g., 'allUsers', 'allAuthenticatedUsers')")
                                   Requires the following arguments:
                                   --project-id, --location, --function-name, --setiambinding                              
    
    
Examples:
      # Deploy a Cloud Function
      python main.py --project-id abc-123456 --location us-east1 --function-name function1 --gsutil-uri gs://bucket/function.zip --function-entry-point function --service-account 1234567890-compute@developer.gserviceaccount.com --deploy
      # Update a Cloud Function
      python main.py --project-id abc-123456 --location us-east1 --function-name function1 --gsutil-uri gs://bucket/function.zip --function-entry-point function --service-account 1234567890-compute@developer.gserviceaccount.com --update
      # Delete a Cloud Function
      python main.py --project-id abc-123456 --location us-east1 --function-name function1 --delete
      # List Cloud Function(s)
      python main.py --project-id abc-123456 --list
      # Check if you hold the required permissions to tinker around with Cloud Functions
      python main.py --project-id abc-123456 --checkperm
      # Create and Download a Service Account Key
      python main.py --project-id abc-123456 --createsakey
      # Bind an IAM Policy to the Cloud Function
      python main.py --project-id abc-123456 --location us-east1 --function-name function1 --setiambinding allUsers
```

## Screenshots
<p><img src="https://github.com/anrbn/GCP-Attack-Defense/blob/main/images/36.png"></p>
<p><img src="https://github.com/anrbn/GCP-Attack-Defense/blob/main/images/37.png"></p>
<p><img src="https://github.com/anrbn/GCP-Attack-Defense/blob/main/images/22.png"></p>
<p><img src="https://github.com/anrbn/GCP-Attack-Defense/blob/main/images/38.png"></p>
