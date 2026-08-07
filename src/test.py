from file_loader import ResumeLoader
from chunker import DocumentChunker
from metadata_extractor import MetadataExtractor

# ==========================================
# Load Resume Documents
# ==========================================

loader = ResumeLoader()

documents = loader.load_documents()

print(f"Loaded {len(documents)} pages.")

# ==========================================
# Chunk Documents
# ==========================================

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print(f"Created {len(chunks)} chunks.")

# ==========================================
# Metadata Extraction
# ==========================================

extractor = MetadataExtractor()

metadata = extractor.extract_metadata(
    chunks[0].page_content
)

print(metadata)