from pydantic import BaseModel
from src.rag import graph_rag
from src.entity.rag.graphiti.document_retriever_request import DocumentRetrieverRequest as GraphitiDocumentRetrieverRequest


class DocumentRetrieverRequest(BaseModel):
    index_name: str
    search_query: str = ''
    metadata_filter: dict = {}

    threshold: float = 0.7
    enable_term_search: bool = True

    text_search_weight: float = 0.9
    text_search_mode: str = 'match'

    enable_vector_search: bool = True
    vector_search_weight: float = 0.1

    rag_k: int = 10
    rag_num_candidates: int = 1000
    enable_rerank: bool = False

    embed_model_base_url: str = ''
    embed_model_api_key: str = ''
    embed_model_name: str = ''

    rerank_model_base_url: str = ''
    rerank_model_api_key: str = ''
    rerank_model_name: str = ''
    rerank_top_k: int = 5

    rag_recall_mode: str = "chunk"

    size: int = 100
    enable_naive_rag: bool = True

    enable_qa_rag: bool = False
    qa_size: int = 10
    enable_graph_rag: bool = False

    graph_rag_request: GraphitiDocumentRetrieverRequest = None
