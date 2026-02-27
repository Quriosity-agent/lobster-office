#!/usr/bin/env python3
"""Update Star Office UI state"""
import json, os, sys
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")
VALID_STATES = ["idle", "writing", "researching", "executing", "coding", "syncing", "articles", "error"]

def save_state(state_name, detail=""):
    state = {
        "state": state_name,
        "detail": detail or f"Status: {state_name}",
        "progress": 0,
        "updated_at": datetime.now().isoformat()
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"State -> {state_name}: {detail}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python set_state.py <state> [detail]")
        print(f"Valid: {', '.join(VALID_STATES)}")
        sys.exit(1)
    s = sys.argv[1]
    d = sys.argv[2] if len(sys.argv) > 2 else ""
    if s not in VALID_STATES:
        print(f"Invalid state: {s}. Valid: {', '.join(VALID_STATES)}")
        sys.exit(1)
    save_state(s, d)
