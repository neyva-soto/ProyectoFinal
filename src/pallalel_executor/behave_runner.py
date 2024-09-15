import subprocess
import sys
import os
import glob
import re


class BehaveRunner:
    def __init__(self, base_dir='features', executors=2, generate_reports=False):
        self.base_dir = base_dir
        self.executors = executors
        self.generate_reports = generate_reports

    def run_command(self, command):
        print(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, check=True)
        if result.returncode != 0:
            print(f"Error running command: {' '.join(command)}")

    def build_command(self, feature_file, scenario=None, tag=None):
        command = [sys.executable, '-m', 'behave']

        if tag:
            command.extend(['--tags', tag])
        if scenario:
            command.extend(['--name', scenario])
        if self.generate_reports:
            command.extend(['--format', 'allure_behave.formatter:AllureFormatter', '--outfile', 'allure-results'])

        command.append(feature_file)
        return command

    def find_feature_files(self, feature_files=[]):
        if feature_files:
            files = []
            for file in feature_files:
                file_path = os.path.join(self.base_dir, file)
                if not file_path.endswith('.feature'):
                    file_path += '.feature'
                if os.path.isfile(file_path):
                    files.append(file_path)
                else:
                    files.extend(glob.glob(os.path.join(self.base_dir, '**', file_path), recursive=True))
            return files
        else:
            return glob.glob(os.path.join(self.base_dir, '**', '*.feature'), recursive=True)

    @staticmethod
    def get_scenarios_from_feature(feature_file):
        with open(feature_file, 'r', encoding='utf-8') as file:
            content = file.read()
        return re.findall(r'Scenario: (.+)', content)

