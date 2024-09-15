import argparse

from src.pallalel_executor.behave_executor import BehaveExecutor
from src.pallalel_executor.behave_runner import BehaveRunner


def parse_arguments():
    parser = argparse.ArgumentParser(description="Execute Behave tests in parallel with Allure report")
    parser.add_argument('--executors', type=int, default=2, help='Number of executors (threads) to use')
    parser.add_argument('--generate_reports', action='store_true', help='Generate Allure test reports')
    parser.add_argument('--features', type=str,
                        help='Comma-separated list of feature files to run. Extensions will be added if omitted')
    parser.add_argument('--scenarios', type=str, help='Comma-separated list of scenarios to run')
    parser.add_argument('--tags', type=str, help='Comma-separated list of tags to filter scenarios')
    parser.add_argument('--base_dir', type=str, default='features',
                        help='Base directory feature files. Default is "features"')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    runner = BehaveRunner(base_dir=args.base_dir, executors=args.executors, generate_reports=args.generate_reports)
    executor = BehaveExecutor(runner)

    feature_files = [file.strip() for file in args.features.split(',')] if args.features else []
    feature_files = [f'{file}' if file.endswith('.feature') else f'{file}.feature' for file in feature_files]

    if not feature_files:
        feature_files = runner.find_feature_files()
    else:
        feature_files = runner.find_feature_files(feature_files=feature_files)

    scenarios = args.scenarios.split(',') if args.scenarios else []
    tags = args.tags.split(',') if args.tags else []

    if not feature_files:
        print("No feature files found.")
    else:
        print(f"Found {len(feature_files)} feature files.")
        executor.run_feature_files(feature_files, scenarios, tags)

