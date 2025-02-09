import json
import os
from pathlib import Path


def get_file_path(task_id: str, results: dict) -> str:

    first_region = next(iter(results), "Unknown")
    continent = first_region.split("/")[0]

    directory = os.path.join("weather_results", continent)
    Path(directory).mkdir(parents=True, exist_ok=True)
    return os.path.join(directory, f"{task_id}.json")


async def save_to_file(task_id: str, data: dict):
    results = data.get("results", {})
    file_path = get_file_path(task_id, results)

    for region, items in results.items():
        data["results"][region] = [
            item.dict() if hasattr(item, "dict") else item for item in items
        ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
