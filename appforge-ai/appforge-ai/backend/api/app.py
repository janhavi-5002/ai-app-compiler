from fastapi import FastAPI
from fastapi.responses import FileResponse
import json

from pipeline.intent_extractor import IntentExtractor
from pipeline.architecture_planner import ArchitecturePlanner
from pipeline.schema_generator import SchemaGenerator

from evaluation.evaluator import Evaluator
from evaluation.test_dataset import (
    REAL_PROMPTS,
    EDGE_CASES
)

app = FastAPI(
    title="AI App Compiler",
    version="1.0"
)

# =====================================
# INITIALIZE COMPONENTS
# =====================================

extractor = IntentExtractor()
planner = ArchitecturePlanner()
generator = SchemaGenerator()

evaluator = Evaluator()

# =====================================
# HOME
# =====================================

@app.get("/")
def home():

    return {
        "message": "AI App Compiler Running"
    }


# =====================================
# GENERATE
# =====================================

@app.post("/generate")
def generate(prompt: str):

    intent = extractor.extract(prompt)

    architecture = planner.generate(
        intent
    )

    schemas = generator.generate(
        architecture
    )

    return {
        "intent":
            intent.model_dump(),

        "architecture":
            architecture.model_dump(),

        "ui":
            schemas["ui"].model_dump(),

        "api":
            schemas["api"].model_dump(),

        "db":
            schemas["db"].model_dump(),

        "auth":
            schemas["auth"].model_dump()
    }


# =====================================
# METRICS
# =====================================

@app.get("/metrics")
def metrics():

    try:

        with open(
            "evaluation_results.json",
            "r"
        ) as f:

            return json.load(f)

    except Exception as e:

        return {
            "error": str(e)
        }


# =====================================
# EVALUATE
# =====================================

@app.post("/evaluate")
def evaluate():

    real_results = evaluator.evaluate(
        REAL_PROMPTS
    )

    edge_results = evaluator.evaluate(
        EDGE_CASES
    )

    return {
        "real_prompts":
            real_results,

        "edge_cases":
            edge_results
    }


# =====================================
# DOWNLOAD
# =====================================

@app.get("/download")
def download():

    return FileResponse(
        path="generated_app.zip",
        filename="generated_app.zip",
        media_type="application/zip"
    )