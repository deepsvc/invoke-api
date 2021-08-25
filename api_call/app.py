import requests
import pandas as pd

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    url = 'https://file-examples-com.github.io/uploads/2017/02/file_example_XLSX_10.xlsx'
    r = requests.get(url, allow_redirects=True)

    excel_sheet = pd.read_excel(r.content)

    for index in excel_sheet.index:
        print(excel_sheet['Id'][index])

