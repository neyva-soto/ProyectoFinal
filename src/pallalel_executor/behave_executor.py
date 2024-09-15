from concurrent.futures import ThreadPoolExecutor


class BehaveExecutor:
    def __init__(self, runner):
        self.runner = runner

    def run_scenarios_in_parallel(self, feature_file, scenarios):
        with ThreadPoolExecutor(max_workers=self.runner.executors) as executor:
            for scenario in scenarios:
                command = self.runner.build_command(feature_file, scenario=scenario)
                executor.submit(self.runner.run_command, command)

    def run_tags_in_parallel(self, feature_file, tags):
        with ThreadPoolExecutor(max_workers=self.runner.executors) as executor:
            for tag in tags:
                command = self.runner.build_command(feature_file, tag=tag)
                executor.submit(self.runner.run_command, command)

    def run_feature_file_with_tags_and_scenarios(self, feature_file, scenarios, tags):
        if not scenarios and not tags:
            # Run all scenarios
            scenarios = self.runner.get_scenarios_from_feature(feature_file)

        if scenarios:
            self.run_scenarios_in_parallel(feature_file, scenarios)

        if tags:
            self.run_tags_in_parallel(feature_file, tags)

    def run_feature_files(self, feature_files, scenarios, tags):
        with ThreadPoolExecutor(max_workers=self.runner.executors) as executor:
                executor.map(lambda f: self.run_feature_file_with_tags_and_scenarios(f, scenarios, tags), feature_files)

