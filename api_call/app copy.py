import requests
import pandas as pd

def download_file():

    url = 'https://file-examples-com.github.io/uploads/2017/02/file_example_XLSX_10.xlsx'
    r = requests.get(url, allow_redirects=True)

    excel_sheet = pd.read_excel(r.content)

    for index in excel_sheet.index:
        print(excel_sheet['Id'][index])

    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.json)

if __name__ == "__main__":
    download_file()
