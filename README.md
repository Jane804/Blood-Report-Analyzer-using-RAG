# Blood Report Analyzer using RAG

## Overview

A Retrieval-Augmented Generation (RAG) application that allows users to:

- Upload blood test report PDFs
- Generate AI-powered summaries
- Ask questions about reports
- Retrieve relevant report sections using semantic search

## Tech Stack

### Frontend
- React.js
- Axios

### Backend
- FastAPI

### AI
- Google Gemini
- Sentence Transformers

### Vector Database
- ChromaDB

### PDF Processing
- PyPDF

## Architecture

PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Retrieval
↓
Gemini
↓
Answer

## Run Backend

```bash
uvicorn app.main:app --reload
```

## Run Frontend

```bash
npm run dev
```

## Docker

```bash
docker-compose up --build
```

## Features

- PDF Upload
- Blood Report Summarization
- Semantic Search
- Question Answering
- RAG Pipeline