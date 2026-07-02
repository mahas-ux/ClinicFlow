# === Stage 16: Add argparse support for the most common commands ===
# Project: ClinicFlow
import argparse

def main():
    parser = argparse.ArgumentParser(description="ClinicFlow Queue Coordinator")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # New visit command
    new_parser = subparsers.add_parser('new-visit', help='Register a new patient visit')
    new_parser.add_argument('--name', required=True, help="Patient name")
    new_parser.add_argument('--priority', choices=['low', 'medium', 'high'], default='medium', help="Visit priority")
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Generate daily queue summary')
    summary_parser.add_argument('--format', choices=['text', 'json'], default='text', help="Output format")
    
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    
    # Placeholder for actual command logic implementation
    print(f"Executing command: {args.command}")
