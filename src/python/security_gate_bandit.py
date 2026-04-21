#!/usr/bin/env python3
import json
import sys
import argparse

def check_bandit(filepath, threshold):
    with open(filepath) as f:
        data = json.load(f)
    high_count = 0
    for result in data.get('results', []):
        severity = result.get('issue_severity', 'UNDEFINED').upper()
        if threshold.upper() == 'HIGH' and severity == 'HIGH':
            high_count += 1
    return high_count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bandit', required=True)
    parser.add_argument('--threshold', default='HIGH')
    args = parser.parse_args()

    errors = check_bandit(args.bandit, args.threshold)
    if errors > 0:
        print(f"Security Gate failed: {errors} HIGH severity issue(s) found.")
        sys.exit(1)
    else:
        print("Security Gate passed: no HIGH severity issues.")
        sys.exit(0)

if __name__ == '__main__':
    main()
