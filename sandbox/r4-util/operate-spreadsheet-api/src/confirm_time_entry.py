import sys
import numpy as np
import pandas as pd
from spreadsheets_util import accessor
from spreadsheets_util import conf

RANGE_NAME = 'D2:H33'

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
    _CHECK_RESULT = '比較結果'

    src_df = pd.DataFrame(
        src_range,
        columns=src_range[0]
    ).drop(0).fillna('')

    dst_df = pd.DataFrame(
        dst_range,
        columns=dst_range[0]
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
    view_df[_CHECK_RESULT] = np.where(
        (view_df[_ATT_ST_DIFF] == '-')
        &(view_df[_ATT_FN_DIFF] == '-'),
        '', 'NG'
    )
    return view_df


def main():
    uname = sys.argv[1]

    controller = accessor.SpreadSheetsAccessor(conf.SCOPES)
    home_range_lst = controller.get_sheets(conf.SPREADSHEET_HOME_ID,
                                           get_target_range(uname=uname))
    site_range_lst = controller.get_sheets(conf.SPREADSHEET_SITE_ID,
                                           get_target_range(uname=uname))
    result_df = check_time_coindicence(src_range=home_range_lst,
                                       dst_range=site_range_lst)
    print(result_df)

if __name__ == '__main__':
    main()
