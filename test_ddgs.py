from duckduckgo_search import DDGS
from itertools import islice
from loguru import logger

# with DDGS() as ddgs:
#     results = [r for r in ddgs.text("python programming", max_results=5)]
#     print(results)

def ddg_search_text(query:str, max_results=5):
    search_results = []
    reference_results = []
    with DDGS() as ddgs:
        ddgs_gen = ddgs.text(query, backend="lite")
        for r in islice(ddgs_gen, max_results):
            search_results.append(r)
    for idx, result in enumerate(search_results):
        logger.debug(f"搜索结果{idx + 1}：{result}")
        ##[result["body"], result["href"]]
        reference_results.append({
                "name": result["title"],
                "url": result["href"],
                "snippet": result["body"]
        })
    return reference_results

ddg_search_text("python programming")