import sys
import datetime as dt
import numpy as np
import pandas as pd
from spreadsheets_util import accessor
from spreadsheets_util import conf

RANGE_NAME = 'D2:H33'
CHECK_RESULT = '比較結果'
REASON = '事由'

def get_target_range(uname=''):
    target_cell_name = u'{}!{}'.format(
        uname,
        RANGE_NAME
    )

    return target_cell_name


def check_time_coindicence(src_range=[],
                           dst_range=[]):
    _ATT_ST_DIFF = '出社_差分'
    _ATT_FN_DIFF = '退社_差分'

    src_df = pd.DataFrame(src_range,columns=src_range[0]
                          ).drop(0).fillna('')

    dst_df = pd.DataFrame(dst_range,columns=dst_range[0]
                          ).drop(0).fillna('')

    view_df = src_df.iloc[:, [0,1,3,4]]
    view_df[_ATT_ST_DIFF] = np.where(
        src_df.iloc[:, 3] == dst_df.iloc[:, 3],
        '-', dst_df.iloc[:, 3]
    )
    view_df[_ATT_FN_DIFF] = np.where(
        src_df.iloc[:, 3] == dst_df.iloc[:, 3],
        '-', dst_df.iloc[:, 3]
    )
    view_df[CHECK_RESULT] = check_matching(
        view_df[_ATT_ST_DIFF],
        view_df[_ATT_FN_DIFF]
    )
    view_df[REASON] = np.where(view_df[CHECK_RESULT] == 'WARN',
                               '本社、現場の時刻差分', '')
    view_df[CHECK_RESULT] = check_blank(
        view_df,
    )
    view_df[REASON] = np.where(view_df[CHECK_RESULT] == 'WARN',
                               '未記入', view_df[REASON])

    return view_df


def check_matching(src_srs, dst_srs):
    _srs = np.where(
        (src_srs == '-') & (dst_srs == '-'),
        '', 'WARN'
    )
    return _srs


def check_blank(src_df):
    _DAYS = '日'
    _DAYOFWEEK = '曜日'
    _ATT_ST = '出社'
    _ATT_FN = '退社'

    now = dt.datetime.now()
    _rtn_srs = np.where(
        (src_df[_DAYS].astype(int) <= now.day)
        & (src_df[_DAYOFWEEK] != '土')
        & (src_df[_DAYOFWEEK] != '日')
        & ((src_df[_ATT_ST] == '') | (src_df[_ATT_FN] == '')),
        'WARN', src_df[CHECK_RESULT]
    )

    return _rtn_srs


def main():
    uname = sys.argv[1]
    print('[INF] Target User: {}'.format(uname))

    controller = accessor.SpreadSheetsAccessor(conf.SCOPES)
    home_range_lst = controller.get_sheets(conf.SPREADSHEET_HOME_ID,
                                           get_target_range(uname=uname))
    site_range_lst = controller.get_sheets(conf.SPREADSHEET_SITE_ID,
                                           get_target_range(uname=uname))
    result_df = check_time_coindicence(src_range=home_range_lst,
                                       dst_range=site_range_lst)
    print('[INF] Result:')
    print(result_df)


if __name__ == '__main__':
    main()

