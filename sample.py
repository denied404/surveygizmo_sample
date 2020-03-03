import os
from surveygizmo import SurveyGizmo

# SurveyGizmo object initialization
client = SurveyGizmo(
            api_version='v5',
            api_token=os.getenv('SG_API_TOKEN'),
            api_token_secret=os.getenv('SG_API_TOKEN_SECRET')
        )

# A list of surveys
surveys = client.api.survey.list()
if not surveys['result_ok']:
    print('Something went wrong and request for survey list has ended with error')
    exit(1)

# Pick first survey as a test sample survey
test_survey = surveys['data'][0]

# Fetch the test survey responses
responses = client.api.surveyresponse.list(test_survey['id'])
if not responses['result_ok']:
    print('Something went wrong and request for survey responses list has ended with error')
    exit(1)

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




