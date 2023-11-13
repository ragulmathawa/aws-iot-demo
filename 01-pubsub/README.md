# Policy to Update


```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:Publish",
        "iot:Receive",
      ],
      "Resource": [
        "arn:aws:iot:ap-south-1:450963760464:topic/<client_id>/test"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "iot:Subscribe",
      "Resource": [
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

#  Update the following places in pubsub.py
```
# Specify the path to your private key, certificate, and Amazon Root CA 1
privateKeyPath = "./certs/device.private.key"
certificatePath = "./certs/device.cert.pem"
caPath = "./certs/root-CA.crt"

# Specify your AWS IoT endpoint
endpoint = "a17xbon89p9o7a-ats.iot.ap-south-1.amazonaws.com"

# Specify your client ID (typically the name of the IoT Thing)
clientId = "Ragul_device"
```