"""
rag.py (Legacy Compatibility Module)
-------------------------------------------------------
The heavy pgvector / PyTorch / HuggingFace RAG pipeline has been replaced
with the lightweight LangChain service in `app.ai_service`.

This module re-exports the functions for backward compatibility with existing
imports and management commands.
-------------------------------------------------------
"""

from .ai_service import (
    get_llm,
    get_upcycle_ideas,
    get_instructions,
)

# Backward-compatible aliases for views
get_upcycle_ideas_with_rag = get_upcycle_ideas
get_instructions_with_rag = get_instructions


def get_vector_store():
    """Stub kept for legacy management commands."""
    class DummyStore:
        def delete_collection(self):
            pass
        def add_documents(self, docs):
            pass
    return DummyStore()


def load_knowledge_to_vectorstore(knowledge_items):
    """Stub kept for legacy management commands."""
    return len(knowledge_items)
