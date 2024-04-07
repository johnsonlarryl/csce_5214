Log in to the AWS Management Console:
Log in to the AWS Management Console using an account that has the necessary permissions to modify IAM policies.

Navigate to IAM Console:
Go to the IAM console by selecting "Services" in the top left corner, then choosing "IAM" under the "Security, Identity, & Compliance" section.

Locate the IAM User:
In the IAM dashboard, navigate to "Users" in the left sidebar. Find and select the IAM user "csce_5212_ljohnson" in the user list.

Update IAM User Policy:

In the "Permissions" tab, you'll see the policies attached to the user.
Identify the policy that is attached to the user and lacks the necessary CloudFormation permissions.
Edit the policy to include the required permissions. You can attach an existing policy or create a new one.
Add CloudFormation Permissions:

Here is an example policy snippet that grants the necessary permission for cloudformation:CreateStack. Make sure to adjust the policy based on your specific needs.

json
Copy code
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "cloudformation:CreateStack",
      "Resource": "arn:aws:cloudformation:us-east-1:1234566:stack/TextClassificationECSCluster/*"
    }
  ]
}
Ensure that the Resource ARN corresponds to the CloudFormation stack you are trying to create.

Review and Save Changes:

Review the changes and save the updated policy.
Attempt to create the CloudFormation stack again with the IAM user.