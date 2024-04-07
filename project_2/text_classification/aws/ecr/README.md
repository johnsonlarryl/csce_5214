1. Create an ECR Repository (if not already created):
Navigate to the ECR Console:

Open the AWS Management Console.
Go to the "ECR" (Elastic Container Registry) service.
Create a Repository:

Click the "Create repository" button.
Enter a repository name, such as csce5214-repo.
Click "Create repository."
2. Create an IAM Policy:
Navigate to the IAM Console:

Open the AWS Management Console.
Go to the "IAM" (Identity and Access Management) service.
Create a Policy:

In the left navigation pane, click on "Policies."
Click the "Create policy" button.
JSON Tab:

Switch to the "JSON" tab.
Replace the existing policy JSON with the following policy allowing push and pull actions on the csce5214-repo ECR repository. Replace "YOUR-ACCOUNT-ID" with your actual AWS account ID.
json
Copy code
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage",
        "ecr:InitiateLayerUpload",
        "ecr:PutImage",
        "ecr:UploadLayerPart"
      ],
      "Resource": "arn:aws:ecr:your-region:YOUR-ACCOUNT-ID:repository/csce5214-repo"
    }
  ]
}
Click "Review policy."
Review Policy:

Enter a name for the policy, such as csce_5214_ecr_policy.
Click "Create policy."
3. Attach Policy to the Group:
Navigate to the IAM Console:

Open the AWS Management Console.
Go to the "IAM" (Identity and Access Management) service.
Attach Policy:

In the left navigation pane, click on "Groups."
Select the csce_5214_devs group.
In the "Permissions" tab, click "Attach policies."
Search for and select the csce_5214_ecr_policy policy.
Click "Attach policy."
Now, the csce_5214_devs group has the csce_5214_ecr_policy attached, allowing its members to push and pull Docker containers to the csce5214-repo ECR repository. Adjust the policy and repository names as needed for your specific setup.

IAM Permissions:
Make sure that the IAM user has the necessary permissions attached to their IAM policy. You should attach a policy that grants permissions for the ecr:GetAuthorizationToken action. You can create a policy like the following and attach it to the user:

json
Copy code
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ecr:GetAuthorizationToken",
      "Resource": "*"
    }
  ]
}
This policy allows the user to perform the ecr:GetAuthorizationToken action on any ECR resource.

Interactive Login Issue:
The second part of your error message, "Cannot perform an interactive login from a non TTY device," suggests that the user is trying to perform an interactive login, possibly using the AWS CLI, from a non-interactive (non-TTY) environment.

To resolve this, make sure that you are running the AWS CLI command in an environment where it can prompt for input. If you are using a script or a non-interactive environment, you may need to provide the necessary input or credentials in a different way.

Once you've made these adjustments, the user should have the required permissions to perform the ecr:GetAuthorizationToken action, and the error should be resolved. Keep in mind that IAM policies can take some time to propagate, so if the changes don't take effect immediately, you may need to wait a few minutes.
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ecr:GetAuthorizationToken",
            "Resource": "*"
        }
    ]
}

$ aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/csce5214-repo
$  docker build . -t  text_classification--text-classification-web-service:latest --platform linux/amd64 
$ docker tag text_classification--text-classification-web-service:latest 491914570594.dkr.ecr.us-east-1.amazonaws.com/csce5214-repo:latest
$ docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/csce5214-repo