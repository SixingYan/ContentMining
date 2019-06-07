import os

import pandas as pd

import const


def extract_zhengzhi(source, target):
    """ 只保留target是1的"""
    pass
    df = pd.read_csv(os.path.join(const.DATAPATH, source), encoding='gb2312')
    df['sent'] = df['sentence'].apply(lambda x: str(x))
    df['sent'] = df['sent'].apply(lambda x: x.encode('utf-8').decode('utf-8'))
    df = df[df['target'] != '0']
    df = df[['file_id', 'target', 'sent']]
    df['sent'] = df['sent'].apply(lambda x: x.split('，'))

    df.to_csv(os.path.join(const.DATAPATH, target), index=None)


def main():
    pass
    extract_zhengzhi(const.DATAPATH, 'raw_', 'zhengzhi.csv')


if __name__ == '__main__':
    main()
