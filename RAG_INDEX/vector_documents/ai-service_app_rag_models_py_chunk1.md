# Knowledge Document: models.py (Chunk 2/2)

## Metadata
```json
{
  "file_path": "ai-service/app/rag/models.py",
  "language": "py",
  "module": "rag",
  "business_domain": "factory",
  "tags": [
    "factory",
    "inventory"
  ],
  "logical_type": "Generic",
  "chunk_index": 1,
  "total_chunks": 2
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in rag.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, inventory

## Source Code Chunk
```py
None


class DocumentProvenance(BaseModel):
    """Document source tracking"""
    document_id: str
    source: str
    source_id: str
    original_created_at: str
    original_updated_at: str
    indexed_at: str
    indexed_by: str
    index_version: int


class ConversationMessage(BaseModel):
    """A message in the conversation history"""
    role: Literal["user", "assistant"]
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class RetrievalConfig(BaseModel):
    """Configuration for retrieval"""
    max_documents: int = 10
    min_relevance_score: float = 0.5
    rerank_top_k: int = 20
    sources: Optional[List[str]] = None
    date_from: Optional[str] = None
    date_to: Optional[str] = None


class QualityMetrics(BaseModel):
    """Quality assessment for a document"""
    completeness: float = Field(ge=0, le=1)
    accuracy: float = Field(ge=0, le=1)
    freshness: float = Field(ge=0, le=1)
    relevance: float = Field(ge=0, le=1)
    overall: float = Field(ge=0, le=1)


class ValidationResult(BaseModel):
    """Result of document validation"""
    valid: bool
    errors: List[str] = Field(default_factory=list)
    warnings: List[str] = Field(default_factory=list)
    quality_score: Optional[QualityMetrics] = None


class IndexingJob(BaseModel):
    """Status of an indexing job"""
    job_id: str
    source: str
    status: Literal["pending", "processing", "completed", "failed"]
    documents_processed: int = 0
    documents_total: int = 0
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

```
