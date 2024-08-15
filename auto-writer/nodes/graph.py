from typing import List, TypedDict

class GraphState(TypedDict):
    """
    表示我们的图的状态。

    属性：
    question: 问题
    generation: LLM生成
    web_search: 是否添加搜索
    documents: 文档列表 
    """
    question : str
    generation : str
    web_search : str
    documents : List[str]