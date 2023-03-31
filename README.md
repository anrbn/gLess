# gLess

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
