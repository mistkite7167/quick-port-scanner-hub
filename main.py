"""
Port Scanner - Main module with CLI support.
"""
import argparse
import sys

VERSION = "0.3.0"

def process(data):
    """Process input data."""
    results = []
    for item in data:
        result = item.strip()
        if result:
            results.append(result)
    return results

def run(args):
    """Main entry point."""
    if args.version:
        print(f"Port Scanner v{VERSION}")
        return

    if not args.input:
        print("No input provided. Use --help for usage.")
        return

    results = process(args.input)
    if args.output:
        with open(args.output, "w") as f:
            for r in results:
                f.write(r + "\n")
        print(f"Output written to {args.output}")
    else:
        for r in results:
            print(r)

def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("input", nargs="*", help="Input data")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
