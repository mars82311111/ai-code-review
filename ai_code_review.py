#!/usr/bin/env python3
"""
ai-code-review: AI-powered code review in one command
Usage: python3 ai_code_review.py [diff_file]
"""

import sys
import os
from datetime import datetime

def review_code(diff_content: str) -> dict:
    """Review code using AI patterns"""
    issues = []
    
    # Simple pattern checks
    lines = diff_content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'password' in line.lower() or 'api_key' in line.lower():
            issues.append({
                "line": i,
                "severity": "HIGH",
                "type": "SECURITY",
                "message": "Potential credential exposure detected"
            })
        if 'TODO' in line and 'FIXME' not in line:
            issues.append({
                "line": i,
                "severity": "LOW", 
                "type": "CODE_QUALITY",
                "message": "TODO comment found"
            })
        if line.strip().startswith('print(') and '# debug' not in line.lower():
            issues.append({
                "line": i,
                "severity": "INFO",
                "type": "DEBUG_CODE",
                "message": "Debug print statement"
            })
    
    return {
        "status": "success",
        "issues_found": len(issues),
        "issues": issues,
        "reviewed_at": datetime.now().isoformat()
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ai_code_review.py [diff_file]")
        print("Example: git diff | python3 ai_code_review.py -")
        sys.exit(1)
    
    diff_file = sys.argv[1]
    
    if diff_file == '-':
        diff_content = sys.stdin.read()
    elif os.path.exists(diff_file):
        with open(diff_file) as f:
            diff_content = f.read()
    else:
        print(f"Error: File not found: {diff_file}")
        sys.exit(1)
    
    result = review_code(diff_content)
    
    print(f"\n🔍 AI Code Review Report")
    print(f"={'='*40}")
    print(f"Issues found: {result['issues_found']}")
    
    for issue in result['issues']:
        emoji = "🔴" if issue['severity'] == 'HIGH' else "🟡" if issue['severity'] == 'MEDIUM' else "🔵"
        print(f"\n{emoji} [{issue['severity']}] {issue['type']}")
        print(f"   Line {issue['line']}: {issue['message']}")
    
    print(f"\n{'='*40}")
    print(f"Reviewed at: {result['reviewed_at']}")

if __name__ == "__main__":
    main()
