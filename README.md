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

## Usage:
Deploy a Cloud Function
```powershell
main.py --project-id abc-123456 --location us-east1 --function-name function1 --gsutil-uri gs://bucket/function.zip --function-entry-point function --service-account 1234567890-compute@developer.gserviceaccount.com --deploy
```
Update a Cloud Function
```powershell
main.py --project-id abc-123456 --location us-east1 --function-name function1 --gsutil-uri gs://bucket/function.zip --function-entry-point function --service-account 1234567890-compute@developer.gserviceaccount.com --update
```
Delete a Cloud Function
```powershell
main.py --project-id abc-123456 --location us-east1 --function-name function1 --delete
```
List Cloud Function(s)
```powershell
main.py --project-id abc-123456 --list
```
Check if you hold the required permissions to tinker around with Cloud Functions
```powershell
main.py --project-id abc-123456 --checkperm
```
Create and Download a Service Account Key
```powershell
main.py --project-id abc-123456 --createsakey
```
Bind an IAM Policy to the Cloud Function
```powershell
main.py --project-id abc-123456 --location us-east1 --function-name function1 --setiambinding allUsers
``` 
