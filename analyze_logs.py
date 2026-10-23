
import csv
from collections import Counter
from datetime import datetime

filename = "web-access-logs.csv"

page_counts = Counter()
hour_counts = Counter()
unique_ips = set()

total_requests = 0
errors_4xx = 0
errors_5xx = 0

try:
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required = {
            "timestamp", "ip", "method",
            "path", "status", "bytes", "user_agent"
        }

        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError("CSV file is missing required columns.")

        for row in reader:
            if not row.get("timestamp") or not row.get("ip"):
                continue

            try:
                status = int(row["status"])
                timestamp = datetime.strptime(
                    row["timestamp"], "%Y-%m-%d %H:%M:%S"
                )
            except (ValueError, TypeError):
                continue

            total_requests += 1
            page_counts[row["path"]] += 1
            hour_counts[timestamp.strftime("%H:00")] += 1
            unique_ips.add(row["ip"])

            if 400 <= status < 500:
                errors_4xx += 1
            elif 500 <= status < 600:
                errors_5xx += 1

    print("AWS PROJECT - WEB LOG ANALYSIS")
    print("=" * 35)
    print("Total valid requests:", total_requests)

    print("\nTop requested pages:")
    for page, count in page_counts.most_common(5):
        print(f"{page}: {count} requests")

    print("\n4xx errors:", errors_4xx)
    print("5xx errors:", errors_5xx)

    if hour_counts:
        peak_hour, count = hour_counts.most_common(1)[0]
        print(f"\nPeak traffic hour: {peak_hour} ({count} requests)")
    else:
        print("\nPeak traffic hour: No valid records")

    print("Unique visitor IPs:", len(unique_ips))

except FileNotFoundError:
    print(f"Error: {filename} was not found.")
    print("Keep the CSV file in the same directory as this script.")
except (OSError, ValueError) as error:
    print("Unable to analyze logs:", error)
