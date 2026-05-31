# VectorFlow AI

## Event-Driven Document Processing & AI Retrieval Platform

VectorFlow AI is a scalable document processing platform designed to ingest, process, and analyze large-scale document workloads asynchronously.

The platform accepts PDFs, CSV files, Excel spreadsheets, and JSON documents, stores metadata in PostgreSQL, and leverages event-driven processing to support scalable document workflows.

This project is being built to explore modern backend engineering concepts including:

- Distributed Systems
- Event-Driven Architecture
- Asynchronous Processing
- AI-Powered Document Analysis
- Semantic Search
- Retrieval-Augmented Generation (RAG)

---

## Architecture

<img width="725" height="937" alt="Screenshot 2026-05-30 at 11 49 17 PM" src="https://github.com/user-attachments/assets/965db730-b13f-4289-b374-c1d51a523fed" />

---

## Current Architecture

```text
Client
   ↓
FastAPI
   ↓
Local File Storage
   ↓
PostgreSQL
```

---

## Target Architecture

```text
Client
   ↓
FastAPI
   ↓
Kafka
   ↓
Worker Services
   ↓
PostgreSQL
   ↓
Vector Database
   ↓
RAG / LLM Layer
```

---

## Current Features

### Document Ingestion

- Upload documents through FastAPI
- Store files locally
- Persist document metadata in PostgreSQL
- Track document processing status

### REST API

Currently implemented:

```text
POST /documents/upload
GET  /documents
GET  /documents/{id}
PUT  /documents/{id}/status
```

### Database

- PostgreSQL
- SQLAlchemy ORM
- Persistent document metadata storage

### Infrastructure

- Dockerized PostgreSQL environment
- Environment variable configuration using `.env`

---

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy

### Database

- PostgreSQL

### Infrastructure

- Docker
- Docker Desktop

### Configuration

- python-dotenv

---

## Engineering Concepts Explored

- REST API Design
- Database Modeling
- SQLAlchemy ORM
- Environment-Based Configuration
- File Storage Strategies
- Asynchronous Processing
- Event-Driven Architecture
- Distributed Systems Design
- Semantic Search
- Retrieval-Augmented Generation (RAG)

---

## Development Roadmap

### Phase 1: Document Ingestion ✅

- [x] FastAPI Backend
- [x] PostgreSQL Integration
- [x] SQLAlchemy ORM
- [x] File Upload API
- [x] Document Metadata Persistence

### Phase 2: Event-Driven Processing 🚧

- [ ] Kafka Event Streaming
- [ ] Background Worker Service
- [ ] Async Document Processing
- [ ] Processing Status Lifecycle

### Phase 3: Document Intelligence

- [ ] PDF Text Extraction
- [ ] CSV Processing
- [ ] Excel Processing
- [ ] JSON Processing
- [ ] Document Chunking

### Phase 4: AI Search & RAG

- [ ] Vector Embeddings
- [ ] Semantic Search
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] AI Summarization

### Phase 5: Frontend Dashboard

- [ ] React Dashboard
- [ ] Upload Interface
- [ ] Processing Metrics
- [ ] Search Experience

### Phase 6: Cloud Infrastructure

- [ ] AWS S3 Storage
- [ ] Dockerized Services
- [ ] Production Deployment

---

## Why This Project?

Many document processing systems work well at small scale but struggle as document volume grows.

VectorFlow AI explores how modern backend systems can leverage asynchronous processing, event streaming, and AI-powered retrieval to efficiently process large document workloads while maintaining responsiveness and scalability.

The long-term goal is to build a cloud-ready platform capable of processing documents asynchronously, enabling semantic search, intelligent document retrieval, and AI-powered summarization across large datasets.
