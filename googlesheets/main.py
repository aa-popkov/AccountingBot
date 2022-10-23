from pathlib import Path

import googleapiclient.discovery
from google.oauth2 import service_account
import pandas as pd


class GoogleSheet:
    def __init__(self) -> None:
        self._spread_sheet_id = "1WxAj1dH3iXUc2gz310dBVHCheAI1T-k7sf-F8T72gWA"
        self._scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds_path = Path(__file__).resolve().parent / "creds.json"
        self._creds = service_account.Credentials.from_service_account_file(
            creds_path, scopes=self._scopes)
        self._table = googleapiclient.discovery.build(
            "sheets", "v4", credentials=self._creds)
        self.register_range = "Registred!A2:C"
        self.som_currency_formula = "=ЕСЛИОШИБКА(СУММ(FILTER('tg-{0}-Data'!B:B; 'tg-{0}-Data'!C:C='tg-{0}-Pivot'!A1));0)"
        self.usd_currency_formula = "=ЕСЛИОШИБКА(СУММ(FILTER('tg-{0}-Data'!B:B; 'tg-{0}-Data'!C:C='tg-{0}-Pivot'!B1));0)"
        self.rub_currency_formula = "=ЕСЛИОШИБКА(СУММ(FILTER('tg-{0}-Data'!B:B; 'tg-{0}-Data'!C:C='tg-{0}-Pivot'!C1));0)"

    def get_data(self, range: str) -> list:
        resp = self._table.spreadsheets().values().batchGet(
            spreadsheetId=self._spread_sheet_id,
            ranges=range).execute()
        # return resp
        return resp["valueRanges"][0]["values"]

    def append_row(self, user_data: list, range: str) -> None:
        values = user_data
        body = {
            "majorDimension": "ROWS",
            "values": values
        }

        result = self._table.spreadsheets().values().append(
            spreadsheetId=self._spread_sheet_id,
            body=body,
            range=range,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS").execute()

    def update_row(self, user_data: list, range: str) -> None:
        values = user_data
        body = {
            "majorDimension": "ROWS",
            "values": values
        }

        result = self._table.spreadsheets().values().update(
            spreadsheetId=self._spread_sheet_id,
            body=body,
            range=range,
            valueInputOption="USER_ENTERED").execute()

    def get_lists(self) -> any:
        result = self._table.spreadsheets().get(
            spreadsheetId=self._spread_sheet_id).execute()

        return result

    def create_list(self, tg_id):
        body = {
            'requests': [
                {
                    'addSheet': {
                        'properties': {
                            'title': f'tg-{tg_id}-Data'
                        }
                    }
                },
                {
                    'addSheet': {
                        'properties': {
                            'title': f'tg-{tg_id}-Pivot'
                        },
                    }
                }
            ]
        }

        result = self._table.spreadsheets().batchUpdate(
            body=body, spreadsheetId=self._spread_sheet_id).execute()

        return result['replies']

    def merge_cells(self):
        body = {
            'requests': [
                {
                    "mergeCells": {
                        "range": {
                            "sheetId": 2145770502,
                            "startRowIndex": 0,
                            "endRowIndex": 1,
                            "startColumnIndex": 0,
                            "endColumnIndex": 4
                        },
                        "mergeType": "MERGE_ALL"
                    }
                }
            ]
        }

        result = self._table.spreadsheets().batchUpdate(
            body=body, spreadsheetId=self._spread_sheet_id).execute()

        return result


def main():
    pass
    a = GoogleSheet()
    # a.append_row(user_data=[["111", "2222", "333"]], range=a.register_range)
    # print(a.get_data(range=a.register_range))
    # a.update_row(range="Registred!A4:C4", user_data=[["223", ""]])

    # resp = a.get_lists()['sheets']
    # for sheet in resp:
    #     print(sheet['properties']['title'].split('-'))
    # print(a.append_row(range="tg-2455765531-Data!A2:D", user_data=[["Связь", "222", "SOM", "22.07.2022 00:00"]]))

    dat = a.get_data("tg-245576553-Pivot")

    print(dat)


if __name__ == "__main__":
    main()
