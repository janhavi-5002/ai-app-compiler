# AI App Compiler

## Overview

AI App Compiler is a reliability-focused application generation system that converts natural language requirements into structured software architectures, validates them, repairs inconsistencies, evaluates reliability, and generates executable application artifacts.

Unlike simple prompt-to-code systems, this project introduces validation, repair, execution verification, mutation handling, and evaluation layers to improve reliability.

---

## Pipeline

User Prompt

↓

Requirement Analyzer

↓

Clarification Engine

↓

Intent Extractor

↓

Architecture Planner

↓

Schema Generator

↓

Validation Engine

↓

Repair Engine

↓

Consistency Validator

↓

Reliability Score

↓

Mutation Engine

↓

Runtime Generator

↓

Execution Validator

↓

Metrics Tracker

↓

ZIP Export

---

## Features

* Intent Extraction
* Architecture Planning
* Schema Generation
* Validation Engine
* Repair Engine
* Consistency Checking
* Reliability Scoring
* Requirement Mutation
* Runtime Generation
* Execution Validation
* Metrics Tracking
* Architecture Graph Generation
* Evaluation Framework
* ZIP Export
* FastAPI APIs

---

## API Endpoints

GET /

POST /generate

GET /metrics

POST /evaluate

GET /download

---

## Evaluation

The system is evaluated on:

* Real-world prompts
* Edge-case prompts
* Reliability metrics
* Execution validation

---

## Generated Outputs

* Application Architecture
* UI Schema
* API Schema
* Database Schema
* Auth Schema
* Architecture Graph
* Executable Project Files
* ZIP Package

---

## Tech Stack

* Python
* FastAPI
* Pydantic
* NetworkX
* Matplotlib

---

## Future Work

* LLM-based Intent Extraction
* Multi-language Code Generation
* Cloud Deployment
* Frontend Generation
* Docker Export

## Architecture

![Architecture](backend/generated_app/architecture_graph.png)
