import pandas as pd
from spreadsheets_util import accessor
from spreadsheets_util import conf


def get_target_range(uid=0):
    target_cell_name = u'{}!{}'.format(
        conf.SHEET_NAME[uid],
        conf.RANGE_NAME
    )

    return target_cell_name


def main():

    controller = accessor.SpreadSheetsAccessor(conf.SCOPES)
    home_range_lst = controller.get_sheets(conf.SPREADSHEET_HOME_ID,
                                           get_target_range(0))
    df = pd.DataFrame(home_range_lst[1:],
                      columns=home_range_lst[0])
    print(df)


if __name__ == '__main__':
    main()
