1.) Set up User in  IAM Identity Center with permissions to create users and groups.
2.) Run the following cloud formation template.

1. Create a Group:
Navigate to the IAM Console:

Open the AWS Management Console.
Go to the "IAM" (Identity and Access Management) service.
Create a Group:

In the left navigation pane, click on "Groups."
Click the "Create group" button.
Enter a group name, such as csce_5214_devs.
Click "Next Step."
Attach Policy (Optional):

You can attach existing policies to the group in this step. However, for this example, we will attach the policy later.
Click "Next Step."
Review and Create:

Review the group details.
Click "Create group."
2. Create an S3 Bucket:
Navigate to the S3 Console:

Open the AWS Management Console.
Go to the "S3" service.
Create a Bucket:

Click the "Create bucket" button.
Enter a globally unique bucket name, such as csce5214.
Choose the region for the bucket.
Click "Next."
Configure Options (Optional):

Configure any additional options as needed.
Click "Next."
Set Permissions:

For simplicity, leave the permissions as they are for now.
Click "Next."
Review and Create:

Review the configuration.
Click "Create bucket."
3. Create a Policy:
Navigate to the IAM Console:

Open the AWS Management Console.
Go to the "IAM" (Identity and Access Management) service.
Create a Policy:

In the left navigation pane, click on "Policies."
Click the "Create policy" button.
JSON Tab:

Switch to the "JSON" tab.
Replace the existing policy JSON with the following policy allowing List, Read, and Write actions on the csce5214 bucket. Replace "YOUR-BUCKET-NAME" with your actual bucket name.
json
Copy code
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::csce5214",
        "arn:aws:s3:::csce5214/*"
      ]
    }
  ]
}
Click "Review policy."
Review Policy:

Enter a name for the policy, such as csce_5214_s3_policy.
Click "Create policy."
4. Attach Policy to the Group:
Navigate to the IAM Console:

Open the AWS Management Console.
Go to the "IAM" (Identity and Access Management) service.
Attach Policy:

In the left navigation pane, click on "Groups."
Select the csce_5214_devs group.
In the "Permissions" tab, click "Attach policies."
Search for and select the csce_5214_s3_policy policy.
Click "Attach policy."
Now, the csce_5214_devs group has the csce_5214_s3_policy attached, allowing its members to list, read, and write objects in the csce5214 S3 bucket.