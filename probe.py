"""Deterministic local canary; no network, secrets or host changes."""
import json


def main():
    print(json.dumps({"kind": "qualification_canary", "status": "ok"}, sort_keys=True))


if __name__ == "__main__":
    main()
