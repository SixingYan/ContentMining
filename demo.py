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
    for s in sents:
        pos = HanLP.parseDependency(s)
        for wpos in pos.getWordArray():
            wpos.LEMMA, wpos.DEPREL, wpos.HEAD.LEMMA


def getData():


def getListData()->List:


def main():
    pass
    df = getListData()


if __name__ == '__main__':
    main()
