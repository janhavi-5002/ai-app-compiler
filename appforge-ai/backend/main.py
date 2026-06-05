import time

from validators.requirement_analyzer import RequirementAnalyzer
from validators.clarification_engine import ClarificationEngine

from pipeline.intent_extractor import IntentExtractor
from pipeline.architecture_planner import ArchitecturePlanner
from pipeline.schema_generator import SchemaGenerator
from pipeline.mutation_engine import MutationEngine

from validators.schema_validator import SchemaValidator
from validators.consistency_validator import ConsistencyValidator

from repair.repair_engine import RepairEngine

from evaluation.reliability_score import ReliabilityScore
from evaluation.metrics_tracker import MetricsTracker

from runtime.runtime_generator import RuntimeGenerator
from runtime.execution_validator import ExecutionValidator

from runtime.architecture_graph import ArchitectureGraph
from runtime.project_exporter import ProjectExporter



from evaluation.evaluator import Evaluator
from evaluation.test_dataset import (
    REAL_PROMPTS,
    EDGE_CASES
)
evaluator = Evaluator()

# =====================================
# INITIALIZE COMPONENTS
# =====================================

requirement_analyzer = RequirementAnalyzer()
clarification_engine = ClarificationEngine()

extractor = IntentExtractor()
planner = ArchitecturePlanner()
generator = SchemaGenerator()

validator = SchemaValidator()
consistency_validator = ConsistencyValidator()

repair_engine = RepairEngine()

reliability_engine = ReliabilityScore()

mutation_engine = MutationEngine()

runtime_generator = RuntimeGenerator()
project_exporter = ProjectExporter()

execution_validator = ExecutionValidator()
graph_generator = ArchitectureGraph()

metrics_tracker = MetricsTracker()




# =====================================
# USER PROMPT
# =====================================

start_time = time.time()

prompt = "Build CRM with login contacts dashboard analytics"

print("\n" + "=" * 60)
print("USER PROMPT")
print("=" * 60)
print(prompt)


# =====================================
# REQUIREMENT ANALYSIS
# =====================================

requirement_issues = requirement_analyzer.analyze(
    prompt
)

print("\n" + "=" * 60)
print("REQUIREMENT ANALYSIS")
print("=" * 60)
print(requirement_issues)


# =====================================
# CLARIFICATION QUESTIONS
# =====================================

clarification_questions = (
    clarification_engine.generate_questions(
        requirement_issues
    )
)

print("\n" + "=" * 60)
print("CLARIFICATION QUESTIONS")
print("=" * 60)
print(clarification_questions)


# =====================================
# INTENT EXTRACTION
# =====================================

intent = extractor.extract(prompt)

print("\n" + "=" * 60)
print("INTENT")
print("=" * 60)
print(intent.model_dump())


# =====================================
# ARCHITECTURE PLANNING
# =====================================

architecture = planner.generate(intent)

print("\n" + "=" * 60)
print("ARCHITECTURE")
print("=" * 60)
print(architecture.model_dump())


# =====================================
# SCHEMA GENERATION
# =====================================

schemas = generator.generate(
    architecture
)

print("\n" + "=" * 60)
print("UI SCHEMA")
print("=" * 60)
print(schemas["ui"].model_dump())

print("\n" + "=" * 60)
print("API SCHEMA")
print("=" * 60)
print(schemas["api"].model_dump())

print("\n" + "=" * 60)
print("DB SCHEMA")
print("=" * 60)
print(schemas["db"].model_dump())

print("\n" + "=" * 60)
print("AUTH SCHEMA")
print("=" * 60)
print(schemas["auth"].model_dump())


# =====================================
# VALIDATION
# =====================================

validation_errors = validator.validate(
    schemas
)

print("\n" + "=" * 60)
print("VALIDATION ERRORS")
print("=" * 60)
print(validation_errors)


# =====================================
# REPAIR ENGINE
# =====================================

schemas, repair_log = repair_engine.repair(
    schemas,
    validation_errors
)

print("\n" + "=" * 60)
print("REPAIR LOG")
print("=" * 60)
print(repair_log)


# =====================================
# CONSISTENCY VALIDATION
# =====================================

consistency_issues = (
    consistency_validator.validate(
        architecture,
        schemas
    )
)

print("\n" + "=" * 60)
print("CONSISTENCY ISSUES")
print("=" * 60)
print(consistency_issues)


# =====================================
# RELIABILITY SCORE
# =====================================

score = reliability_engine.calculate(
    validation_errors,
    consistency_issues
)

print("\n" + "=" * 60)
print("RELIABILITY SCORE")
print("=" * 60)
print(score)


# =====================================
# REQUIREMENT MUTATION
# =====================================

change_request = "Add payment support"

print("\n" + "=" * 60)
print("CHANGE REQUEST")
print("=" * 60)
print(change_request)

architecture, mutation_log = (
    mutation_engine.apply_change(
        architecture,
        change_request
    )
)

print("\n" + "=" * 60)
print("MUTATION LOG")
print("=" * 60)
print(mutation_log)

print("\n" + "=" * 60)
print("UPDATED ARCHITECTURE")
print("=" * 60)
print(
    architecture.model_dump()
)


# =====================================
# RUNTIME GENERATION
# =====================================

generated_project = (
    runtime_generator.generate(
        architecture
    )
)
zip_file = project_exporter.export_zip(
    generated_project
)

print("\n" + "=" * 60)
print("ZIP EXPORT")
print("=" * 60)
print(zip_file)

graph_file = (
    graph_generator.generate(
        architecture
    )
)

print("\n" + "=" * 60)
print("ARCHITECTURE GRAPH")
print("=" * 60)
print(graph_file)

print("\n" + "=" * 60)
print("GENERATED PROJECT")
print("=" * 60)
print(generated_project)

execution_results = (
    execution_validator.validate(
        generated_project
    )
)

print("\n" + "=" * 60)
print("EXECUTION VALIDATION")
print("=" * 60)
print(execution_results)


# =====================================
# METRICS
# =====================================

end_time = time.time()

generation_time = round(
    end_time - start_time,
    6
)

metrics = metrics_tracker.save_metrics(
    generation_time=generation_time,
    validation_errors=len(validation_errors),
    repair_count=len(repair_log),
    consistency_issues=len(consistency_issues),
    reliability_score=score
)

print("\n" + "=" * 60)
print("METRICS")
print("=" * 60)
print(metrics)

# =====================================
# EVALUATION FRAMEWORK
# =====================================

real_results = evaluator.evaluate(
    REAL_PROMPTS
)

edge_results = evaluator.evaluate(
    EDGE_CASES
)

print("\n" + "=" * 60)
print("REAL PROMPT EVALUATION")
print("=" * 60)

print(
    f"Success Rate: "
    f"{real_results['success_rate']}%"
)

print(
    f"Passed: "
    f"{real_results['passed']}/"
    f"{real_results['total_tests']}"
)

print("\n" + "=" * 60)
print("EDGE CASE EVALUATION")
print("=" * 60)

print(
    f"Success Rate: "
    f"{edge_results['success_rate']}%"
)

print(
    f"Passed: "
    f"{edge_results['passed']}/"
    f"{edge_results['total_tests']}"
)


# =====================================
# FINAL SUMMARY
# =====================================

print("\n" + "=" * 60)
print("PIPELINE SUMMARY")
print("=" * 60)

print(
    f"Requirement Issues : {len(requirement_issues)}"
)

print(
    f"Validation Errors  : {len(validation_errors)}"
)

print(
    f"Consistency Issues : {len(consistency_issues)}"
)

print(
    f"Reliability Score  : {score}/100"
)

print(
    f"Generation Time    : {generation_time}s"
)

print(
    f"Generated Project  : {generated_project}"
)


print("\n" + "=" * 60)
print("PIPELINE EXECUTED SUCCESSFULLY")
print("=" * 60)