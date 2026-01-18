import argparse
import json
import sys
from analyzer import analyze_calls
from report import create_report

def main():
    """
    Main function for the TokenLens CLI.
    """
    parser = argparse.ArgumentParser(
        description="TokenLens: A token waste profiler for LLMs."
    )
    parser.add_argument(
        "--run",
        dest="filepath",
        required=True,
        help="Path to the JSON file containing sample LLM calls."
    )
    
    args = parser.parse_args()
    
    try:
        with open(args.filepath, 'r') as f:
            try:
                call_data_list = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON in file: {args.filepath}", file=sys.stderr)
                sys.exit(1)
                
    except FileNotFoundError:
        print(f"Error: File not found at: {args.filepath}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(call_data_list, list):
        print(f"Error: JSON file must contain a list of call objects.", file=sys.stderr)
        sys.exit(1)

    # Perform analysis
    analysis_result = analyze_calls(call_data_list)
    
    # Create and print the report
    final_report = create_report(analysis_result)
    print(final_report)

if __name__ == "__main__":
    main()
