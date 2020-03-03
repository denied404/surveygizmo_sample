# A test case for using SurveyGizmo PyPI package in order to fetch a SurveyGizmo survey data

OK, since the code is straightforward, let's just glance over it and quickly describe each step.

```
import os
from surveygizmo import SurveyGizmo
```
Basically, all we need is to import `SurveyGizmo` object from `surveygizmo` package. `os` is imported here for the purpose of fetching SG API token and API secret token which are used to connect to SG from OS env variables.
Then we initialize our instance of `SurveyGizmo` object:
```
# SurveyGizmo object initialization
client = SurveyGizmo(
            api_version='v5',
            api_token=os.getenv('SG_API_TOKEN'),
            api_token_secret=os.getenv('SG_API_TOKEN_SECRET')
        )
```
That's it. Simple and straightforward. Now we can make our API calls through the SG object. Let's fetch a list of all our surveys:
```
# A list of surveys
surveys = client.api.survey.list()
if not surveys['result_ok']:
    print('Something went wrong and request for survey list has ended with error')
    exit(1)
```
NB: keep in mind that `client.api.survey.list()` supports `.filter()` chain calls in order to filter our surveys by some criteria, like survey create date etc.
Now we just pick a first survey from the surveys list as an example:
```
# Pick first survey as a test sample survey
test_survey = surveys['data'][0]
```
Now, since the primary focus of the test case is to show how we could fetch and process additional URL attributes which are being passed with each survey, let's fetch survey responses:
```
# Fetch the test survey responses
responses = client.api.surveyresponse.list(test_survey['id'])
if not responses['result_ok']:
    print('Something went wrong and request for survey responses list has ended with error')
    exit(1)
```
And now, having a list of survey responses, we can easily fetch both URL attributes and survey Q&As from there. Along with any other survey's response attribute:
```
# Let's try to access each response answers and URL attributes
for response in responses['data']:
    print("Response ID {0}".format(response['id']))

    # Print out each response's URL variables
    # Since url_variables is a dict, we traverse
    # through its items()
    print('URL Variables:')
    for key, var in response['url_variables'].items():
        print("{0}: {1}".format(key, var['value']))

    # Print out each question and answer
    # And again, we traverse through a dict.items()
    print('Questions And Answers:')
    for key, var in response['survey_data'].items():
        print("Question ID: {0}".format(var['id']))
        print("Question: {0}".format(var['question']))
        print("Answer: {0}".format(var['answer']))
```
