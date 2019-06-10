import os
import pandas as pd

from pandas.core.frame import DataFrame

import const


def extract_zhengzhi(source, target):
    """ 只保留target是1的"""
    pass
    df = pd.read_csv(os.path.join(const.DATAPATH, source), encoding='gb2312')
    df['paragraph'] = df['sentence'].apply(lambda x: str(x))
    df['paragraph'] = df['paragraph'].apply(lambda x: x.encode('utf-8').decode('utf-8'))
    df['target'] = df['target'].apply(lambda x: str(x))
    df['target'] = df['target'].apply(lambda x: x.encode('utf-8').decode('utf-8'))
    df['target'] = df['target'].apply(lambda x: '0' if '0' in x else x)
    df = df[df['target'] != '0']
    df = df[['file_id', 'target', 'paragraph']]

    df.to_csv(os.path.join(const.DATAPATH, target), index=None)


def extract_labels(source, target):
    """  """
    fileid, para, label1, label2, label3, label4 = [], [], [], [], [], []

    df = pd.read_csv(os.path.join(const.DATAPATH, source))
    df = df[df['target'] != '0']
    df['target'] = df['target'].apply(lambda x: str(x))
    for fid, t, p in zip(df['file_id'].values.tolist(), df['target'].values.tolist(), df['paragraph'].values.tolist()):
        t = t.replace(',', '，')
        if '，' in t:
            for s in t.split('，'):
                # print(s)
                l1, l2, l3, l4 = tuple(s.split('-'))

                fileid.append(fid)
                para.append(p)
                label1.append(l1)
                label2.append(l2)
                label3.append(l3)
                label4.append(l4)
        else:
            try:
                l1, l2, l3, l4 = tuple(t.split('-'))
            except Exception as e:
                print(t)
                print(t.split('-'))
                raise e
            fileid.append(fid)
            para.append(p)
            label1.append(l1)
            label2.append(l2)
            label3.append(l3)
            label4.append(l4)

    data = DataFrame({'file_id': fileid, 'para': para, 'label1': label1, 'label2': label2, 'label3': label3, 'label4': label4})

    data.to_csv(os.path.join(const.DATAPATH, target), index=None)


def main():
    pass
    #extract_zhengzhi('zhengzhi_file.csv', 'zhengzhi.csv')
    #extract_labels('zhengzhi.csv', 'zhengzhi_label.csv')

if __name__ == '__main__':
    main()
