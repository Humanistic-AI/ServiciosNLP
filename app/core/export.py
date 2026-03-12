# app/core/export.py
import csv
from typing import Dict


def export_counts_to_csv(counts: Dict[str, int], filename: str) -> str:
    """
    Writes word counts to a CSV file sorted by frequency (desc).
    Returns the filename.
    """
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    with open(filename, "w", newline="") as fout:
        writer = csv.writer(fout)
        writer.writerow(["word", "count"])
        for word, count in sorted_items:
            writer.writerow([word, count])

    return filename