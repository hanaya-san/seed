from apiclient.discovery import build
from httplib2 import Http
from oauth2.credentials import get_credentials

class SpreadSheetsAccessor:

    def __init__(self, scopes):
        self.scopes = scopes
        self.creds = get_credentials(scopes)


    def get_sheets(self, sheet_id, range_name):
        sheets = build(
            'sheets',
            'v4',
            http=self.creds.authorize(Http())
        ).spreadsheets()
        values = sheets.values()
        result = values.get(
            spreadsheetId=sheet_id,
            range=range_name
        ).execute()

        return result.get('values', list())


    def scopes_setting(self, scopes):
        self.scopes = scopes
