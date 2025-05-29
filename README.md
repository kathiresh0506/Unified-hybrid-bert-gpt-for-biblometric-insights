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


## Project Structure

ML_RESEARCH/
│
├── app1.py # Main entry point using environment variables
├── app2.py # Main entry point using direct API access
├── your_pipeline2.py # Full pipeline script (with .env)
├── your_pipeline3.py # Full pipeline script (no .env)
│
├── fetch_arxiv.py # Fetch papers from arXiv
├── fetch_core.py # Fetch papers from CORE
│
├── graph_builder.py # Builds Neo4j graph from data
├── graph_info.py # Helper for graph metadata
├── graph.html # HTML visualization of the knowledge graph
│
├── clustered_papers.csv # Clustering results
├── core_papers_fulltext.csv # Fulltext from CORE
├── papers_enriched.csv # Final enriched metadata for graphing
├── papers3.csv # Raw paper metadata
│
├── requirements.txt # Required Python packages
├── .env # (Optional) API keys and config
├── .gitignore # Standard ignore rules
├── README.md # Project documentation
├── Unified_Hybrid_NLP_Workflow.pdf # Workflow overview (PDF)

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
git clone https://github.com/yourusername/ML_RESEARCH.git
cd ML_RESEARCH
