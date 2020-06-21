# slstest
Serverless hello world

# install

`$ npm install -g serverless`

# create

`$ sls create -t aws-python -p slstest`

# deploy

`$ sls deploy`

`$ sls deploy -v`

`$ sls deploy --aws-profile hoge`

# test

`$ sls invoke -f hello`

`$ sls invoke local -f hello`

## S3

`$ aws s3 cp assets/family_picnic_resized.jpg s3://c5apple-slstest/upload/family_picnic_resized.jpg --acl public-read`

`$ aws s3 cp assets/yoga_swimwear_resized.jpg s3://c5apple-slstest/upload/yoga_swimwear_resized.jpg --acl public-read`

# remove

`$ sls remove`

# aws

ポリシー名：AWSCloudFormationDeployer

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "iam:DeleteRolePolicy",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "cloudformation:*",
            "Resource": "*"
        }
    ]
}
```
