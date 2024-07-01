from fastapi import APIRouter

from api.routes import schemas

router = APIRouter()

@router.get("/health", response_model=schemas.HealthResponse)
async def health():
    '''
    Health API interface
    :return:
    '''
    return schemas.HealthResponse(status=True)


@router.get("/api/search")
def search_query():
    '''
    search API interface
    :return:
    '''
    return "搜索请求"


@router.get("/api/search/outline")
def search_result_outline():
    '''
    对搜索结果进行总结成大纲
    :return:
    '''
    return "搜索请求"


@router.get("/api/search/mindmap")
def search_result_mindmap():
    '''
    对搜索结果生成思维导图的格式
    :return:
    '''
    return "搜索请求"


@router.get("/api/search")
def search_query():
    return "搜索请求"


@router.get("/api/chat")
def chat():
    '''
    chat对话框
    :return:
    '''
    return "搜索请求"


@router.get("/api/model-select")
def model_select():
    '''
    界面模型选择
    :return:
    '''
    return "搜索请求"


@router.get("/api/history")
def search_histroy():
    '''
    搜索和对话的历史记录存储，这里需要做一个KV缓存机制
    :return:
    '''
    return "搜索请求"


@router.get("/api/content-cite")
def search_engine_api():
    '''
    获取搜索引擎的搜索内容以及引用ID
    :return:
    '''
    return "搜索请求"
