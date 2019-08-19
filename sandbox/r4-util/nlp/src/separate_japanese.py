import pandas as pd

DUO_FILE = '../data/duo_3-0'


def main():
    raw_df = pd.read_csv('{}.csv'.format(DUO_FILE), dtype='object')
    jp_df = raw_df.loc[:, ['id', 'ja']]

    jp_df.to_csv('{}_ja.csv'.format(DUO_FILE), index=False)
    print('[INF] Output {}_ja.csv'.format(DUO_FILE))


if __name__ == '__main__':
    main()


