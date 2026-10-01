#!/usr/bin/env python3
"""generate_statistics.py - General Awareness Question Bank Statistics"""
import os, sys, json
from pathlib import Path
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_DIR = REPO_ROOT / "questions"
METADATA_DIR = REPO_ROOT / "metadata"

def run():
    total_q = 0
    by_topic = defaultdict(int)
    by_diff = defaultdict(int)
    for jf in QUESTIONS_DIR.rglob("*.json"):
        try:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
            items = data if isinstance(data, list) else [data]
            for q in items:
                total_q += 1
                by_topic[q.get("topic", "misc")] += 1
                by_diff[q.get("difficulty", "medium")] += 1
        except Exception:
            pass

    stats = {
        "repository": "ikshvaku-general-awareness",
        "total_questions": total_q,
        "difficulty_distribution": dict(by_diff),
        "topic_distribution": dict(by_topic)
    }
    with open(METADATA_DIR / "question-counts.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)

    print("=" * 80)
    print(" IKSHVAKU GENERAL AWARENESS - STATISTICS DASHBOARD")
    print("=" * 80)
    print(f" Total Questions : {total_q:,}")
    print(f" Topics Covered  : {len(by_topic)}")
    print("=" * 80)

if __name__ == "__main__":
    run()
