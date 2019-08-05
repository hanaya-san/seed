import os
from apiclient.discovery import build
from httplib2 import Http
import numpy as np
import pandas as pd

from oauth2.credentials import get_credentials


SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SPREADSHEET_ID = os.environ['SPSHEET_URL_HOME']
SHEET_NAME = '' # Please setting
RANGE_NAME = '' # Please setting

TARGET_CELL_NAME = u'%s!%s'%(SHEET_NAME, RANGE_NAME)

creds = get_credentials(SCOPES)
service = build('sheets', 'v4', http=creds.authorize(Http()))

result = service.spreadsheets().values() \
    .get(spreadsheetId=SPREADSHEET_ID,
         range=TARGET_CELL_NAME
         ).execute()
values = result.get('values', [])

df = pd.DataFrame(values,
                  index=np.arange(31),
                  columns=['日', '曜日', '区分', '出社', '退社'])

if not values:
    pass
else:
    print(df)
