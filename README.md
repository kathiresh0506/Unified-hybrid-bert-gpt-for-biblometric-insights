# ML_RESEARCH: Unified Hybrid NLP Research Assistant

This repository provides a full NLP pipeline to automate bibliometric research on scientific papers. It includes tools to fetch full-text research papers (from arXiv and CORE), extract metadata, perform keyword extraction, generate embeddings, cluster papers, and visualize relationships in a knowledge graph (Neo4j).

## Features

- Fetch full-text papers from **arXiv** and **CORE**
- Extract metadata and keywords
- Generate embeddings using BERT
- Cluster papers based on keyword/semantic similarity
- Build and visualize a **Neo4j knowledge graph**
- Two modes of access:
  - **With `.env` file** for secure credential-based access (e.g., API keys)
  - **Without `.env`**, using direct API access for development or testing


## Workflow Overview

The complete NLP bibliometric pipeline runs as follows:

### 1. Paper Retrieval
- Use `fetch_arxiv.py` and `fetch_core.py` to fetch papers from arXiv and CORE APIs.
- You can choose to use:
  - `app1.py` or `your_pipeline2.py`: **With `.env` file**
  - `app2.py` or `your_pipeline3.py`: **Direct API access**

### 2. Preprocessing
- Extract abstracts, metadata, and full-text where available.
- Store them in CSV files (e.g., `core_papers_fulltext.csv`, `papers3.csv`).

### 3. Keyword Extraction & Clustering
- Extract keywords from the text.
- Generate embeddings (e.g., using BERT).
- Cluster papers based on semantic similarity.
- Save clustered results in `clustered_papers.csv`.

### 4. Graph Building
- Use `graph_builder.py` and `graph_info.py` to create a Neo4j-compatible graph from enriched paper data (`papers_enriched.csv`).
- Relationships are created based on topic, keyword similarity, authorship, etc.
- Graph can be visualized with Neo4j Desktop or as HTML (`graph.html`).

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kathiresh0506/ML_RESEARCH.git
cd ML_RESEARCH
