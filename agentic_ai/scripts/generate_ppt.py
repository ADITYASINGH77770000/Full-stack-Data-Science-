from __future__ import annotations
import argparse
from agentic_ai.orchestrator.master import MasterAgent

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--molecule", required=True)
    parser.add_argument("--indication", required=True)
    args = parser.parse_args()

    master = MasterAgent()
    result = master.generate_ppt(args.molecule, args.indication)
    print(result["file_path"])  # print path for convenience

if __name__ == "__main__":
    main()
