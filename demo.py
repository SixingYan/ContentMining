import os
from typing import List
import pandas as pd

from pyhanlp import *


"""
参考实例
https://github.com/hankcs/pyhanlp/tree/master/tests/demos
"""

# 这里可以直接抽取命名实体

PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
analyzer = PerceptronLexicalAnalyzer()
print(analyzer.analyze("上海华安工业（集团）公司董事长谭旭光和秘书胡花蕊来到美国纽约现代艺术博物馆参观"))

# 短语抽取


# 依存关系


# 构建事实三元组


查看效果如何


def function():
    pass
    # 基于外部字典

    print(HanLP.segment(text))

    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    CustomDictionary.add("攻城狮")  # 动态增加
    CustomDictionary.insert("白富美", "nz 1024")  # 强行插入
    # CustomDictionary.remove("攻城狮"); # 删除词语（注释掉试试）
    CustomDictionary.add("单身狗", "nz 1024 n 1")
    # print(CustomDictionary.get("单身狗"))

    print(HanLP.segment(text))

    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    text = "教授正在教授自然语言处理课程"
    segment = HanLP.newSegment().enablePartOfSpeechTagging(True)

    print("未标注：", segment.seg(text))
    segment.enablePartOfSpeechTagging(True)
    print("标注后：", segment.seg(text))


以句为单位


先聚类分析，后分类


最后的目的是分类，也可能是聚类


需要基于文档之间的依存关系

因为跨越太大


def progress():
    """ 整体处理流程，这里应该是最后处理"""
    pass


def getRelations():
    """"""

    relations = []
    for s in sents:
        pos = HanLP.parseDependency(s)
        for wpos in pos.getWordArray():
            relations.append((wpos.LEMMA, wpos.DEPREL, wpos.HEAD.LEMMA))
    Counter(relations)


def getData():


def getListData()->List:


def main():
    pass
    df = getListData()


if __name__ == '__main__':
    main()



def 


sample = df.sample(frac=0.5)
sent = sample.values.tolist()
relations = []
for s in sents:
    pos = HanLP.parseDependency(s)
    for wpos in pos.getWordArray():
        relations.append((wpos.LEMMA, wpos.DEPREL, wpos.HEAD.LEMMA))

c = Counter(relations)


c.most_common(10)


sum(c.values())  # 所有计数的总数


c.clear()  # 重置Counter对象，注意不是删除
list(c)  # 将c中的键转为列表
set(c)  # 将c中的键转为set
dict(c)  # 将c中的键值对转为字典
c.items()  # 转为(elem, cnt)格式的列表
Counter(dict(list_of_pairs))  # 从(elem, cnt)格式的列表转换为Counter类对象
c.most_common()[:-n:-1]  # 取出计数最少的n-1个元素
c += Counter()  # 移除0和负值


# 切出4个标签
def getLabel(s: str):

    return l1, l2, l3, l4


import pandas as pd
import os
from pyhanlp import *
from collections import Counter
import re
from typing import List
path = 'D:/yansixing/ContentMining/Datasets/Data/'
source = 'zhengzhi_label.csv'



sample = df.sample(frac=0.2)
paras = sample['para'].values.tolist()
relations = []
# 还是得基于短句来训练
# 这是有长度限制的
#要把标点符号也去掉
# 增加一些过滤规则
for para in paras:
    for sent in parse_sent(para):
        for s in parse_piece(sent):
            pos = HanLP.parseDependency(s)
            for wpos in pos.getWordArray():
                relations.append((wpos.LEMMA, wpos.DEPREL, wpos.HEAD.LEMMA))


def parse_sent(para: str)->List:
    para = re.sub('([。！!\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

def parse_piece(sent:str)->List:
    return list(sent.replace(',','，').split('，'))