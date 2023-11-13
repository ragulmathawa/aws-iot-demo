# Update the Policy

Note: update the <thing_name> & <client_id> with your own thing name
```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish"
      ],
      "Resource": [
        "arn:aws:iot:ap-south-1:450963760464:topic/$aws/things/<thing_name>/shadow/*",
        "arn:aws:iot:ap-south-1:450963760464:topic/<client_id>/test"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Receive"
      ],
      "Resource": [
        "arn:aws:iot:ap-south-1:450963760464:topic/$aws/things/<thing_name>/shadow/*",
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Subscribe"
      ],
      "Resource": [
        "arn:aws:iot:ap-south-1:450963760464:topicfilter/$aws/things/<thing_name>/shadow/*",
        "arn:aws:iot:ap-south-1:450963760464:topicfilter/<client_id>/test"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iot:Connect",
      "Resource": [
        "arn:aws:iot:ap-south-1:450963760464:client/<client_id>"
      ]
    }
  ]
}

```