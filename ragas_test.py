from datasets import load_dataset
#  https://geek-docs.com/python/python-ask-answer/144_python_learning_asyncio_coroutine_was_never_awaited_warning_error.html
fiqa_eval = load_dataset("explodinggradients/fiqa", "ragas_eval")['baseline']

from ragas.metrics import faithfulness, answer_relevancy, context_precision
from ragas.metrics.critique import harmfulness
 
# metrics you chose
metrics = [faithfulness, answer_relevancy, context_precision, harmfulness]  
from ragas.run_config import RunConfig
from ragas.metrics.base import MetricWithLLM, MetricWithEmbeddings

import asyncio
 
 
# util function to init Ragas Metrics
def init_ragas_metrics(metrics, llm, embedding):
    for metric in metrics:
        if isinstance(metric, MetricWithLLM):
            metric.llm = llm
        if isinstance(metric, MetricWithEmbeddings):
            metric.embeddings = embedding
        run_config = RunConfig()
        metric.init(run_config)
        
        
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
 
# wrappers
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
 
llm = ChatOpenAI()
emb = OpenAIEmbeddings()
 
init_ragas_metrics(
    metrics,
    llm=LangchainLLMWrapper(llm),
    embedding=LangchainEmbeddingsWrapper(emb),
)

row = fiqa_eval[0]
row['question'], row['answer']

from langfuse import Langfuse
 
langfuse = Langfuse()
langfuse.auth_check()

async def score_with_ragas(query, chunks, answer):
    scores = {}
    for m in metrics:
        print(f"calculating {m.name}")
        scores[m.name] = await m.ascore(
            row={"question": query, "contexts": chunks, "answer": answer}
        )
    return scores


question = row['question']
trace = langfuse.trace(name = "rag")
print(question)
 
# retrieve the relevant chunks
# chunks = get_similar_chunks(question)
contexts = row['contexts']
# pass it as span
trace.span(
    name = "retrieval", input={'question': question}, output={'contexts': contexts}
)
print(contexts)
 
# use llm to generate a answer with the chunks
# answer = get_response_from_llm(question, chunks)
answer = row['answer']
trace.span(
    name = "generation", input={'question': question, 'contexts': contexts}, output={'answer': answer}
)
print(answer)

 
# compute scores for the question, context, answer tuple
async def test_langfuse_rags():
    ragas_scores = await score_with_ragas(question, contexts, answer)
    print(ragas_scores)
    for m in metrics:
        trace.score(name=m.name, value=ragas_scores[m.name])
        

asyncio.run(test_langfuse_rags())     
