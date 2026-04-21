#!/usr/bin/env python3
import json, sys, argparse
def check_semgrep(filepath, threshold):
    with open(filepath) as f:
        data = json.load(f)
    errors = 0
    for r in data.get('results', []):
        sev = r.get('extra', {}).get('severity', 'INFO').upper()
        if threshold.upper() == 'HIGH' and sev in ['HIGH', 'CRITICAL']:
            errors += 1
    return errors
def check_bandit(filepath, threshold):
    with open(filepath) as f:
        data = json.load(f)
    return sum(1 for r in data.get('results', []) if r.get('issue_severity', '').upper() == threshold.upper())
def check_eslint(filepath, threshold):
    with open(filepath) as f:
        data = json.load(f)
    errors = 0
    for file_info in data:
        for msg in file_info.get('messages', []):
            if msg.get('severity') == 2:
                errors += 1
    return errors
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--semgrep', required=True)
    p.add_argument('--bandit', required=True)
    p.add_argument('--eslint', required=True)
    p.add_argument('--threshold', default='HIGH')
    args = p.parse_args()
    total = 0
    total += check_semgrep(args.semgrep, args.threshold)
    total += check_bandit(args.bandit, args.threshold)
    total += check_eslint(args.eslint, args.threshold)
    if total > 0:
        print(f"Security Gate failed: {total} critical issues")
        sys.exit(1)
    else:
        print("Security Gate passed")
        sys.exit(0)

if __name__ == '__main__':
    main()
