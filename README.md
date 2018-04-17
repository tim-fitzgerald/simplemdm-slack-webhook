### SimpleMDM Webhook to Slack  

This is a python script written for intended use with AWS Lambda that will take a payload from the SimpleMDM webhook and convert the payload into one compatible with Slack's incoming webhooks. 


#### AWS Requirements

The runtime for this script should be Python 3.6.

If you intend to use this script with AWS you will also need to create an API Gateway endpoint. In that API Gateway you will need to creat a POST Method Execution. [Here][1] is a pretty useful reference that will give you an idea on how to do that. Once you've deploed the API you'll need to get the URL to execute the POST method and use that as your webhook URL in your SimpleMDM account. 

The script also assumes you're setting the Slack incoming webhook URL via an environment variable in Lambda called `SLACK_URL`. 

#### TO-DO:
* general refactoring and make the code a bit more Python-esque. 
* explore posting additional useful information from the SimpleMDM Payload. 

[1]: https://api.slack.com/tutorials/aws-lambda