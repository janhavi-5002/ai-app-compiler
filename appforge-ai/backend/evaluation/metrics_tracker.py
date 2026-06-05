import json
from datetime import datetime


class MetricsTracker:

    def save_metrics(
        self,
        generation_time,
        validation_errors,
        repair_count,
        consistency_issues,
        reliability_score
    ):

        metrics = {
            "timestamp": str(datetime.now()),
            "generation_time": generation_time,
            "validation_errors": validation_errors,
            "repair_count": repair_count,
            "consistency_issues": consistency_issues,
            "reliability_score": reliability_score
        }

        with open(
            "evaluation_results.json",
            "w"
        ) as f:

            json.dump(
                metrics,
                f,
                indent=4
            )

        return metrics