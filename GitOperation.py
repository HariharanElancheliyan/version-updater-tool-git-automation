import git
from git import Repo
import json
import my_logger
import subprocess
import ChangeVersion


class GitOperation:
    def __init__(self, gjson_path):
        my_logger.logger.info("----------------------------------------")
        self.git_json_path = gjson_path
        self.git_json_dict = {}
        self.git_access_token = ""
        self.git_branch_name = ""
        self.git_clone_path = ""
        self.files_list = []
        try:
            with open(self.git_json_path, 'r', encoding='utf-8') as git_json_file:
                git_data = json.load(git_json_file)
                self.git_file_data = git_data
                my_logger.logger.info("Git data json file opened successfully")
        except FileNotFoundError:
            my_logger.logger.error("Error in opening git json file")
            my_logger.logger.error("Exception occurred in Git operation constructor", exc_info=True)

    def git_load_json_to_map(self):
        try:
            for item in self.git_file_data:
                key = item
                value = self.git_file_data[item]
                self.git_json_dict[key] = value
                my_logger.logger.info("{} added to dict Successfully".format(key))
            print(self.git_json_dict)
        except AttributeError:
            my_logger.logger.error("AttributeError Exception occurred", exc_info=True)
            msg = "Attribute Error occurred while loading data from json to dict !!"
            print(msg)

    def parse_data_from_dict(self):
        try:
            self.git_load_json_to_map()
            self.git_access_token = self.git_json_dict['access_token']
            self.git_clone_path = self.git_json_dict['clone_path']
            self.git_branch_name = self.git_json_dict['branch_name']
            my_logger.logger.info("Successfully parsed data from dict")

            print(self.git_access_token)
            print(self.git_branch_name)
            print(self.git_clone_path)
        except KeyError:
            my_logger.logger.error("KeyError Exception occurred in parse_data_from_dict() - JSON Format is wrong",
                                   exc_info=True)
            msg = "Exception occurred in parse_data_from_dict()"
            print(msg)

    def add_files_for_commit(self):
        source_dict = ChangeVersion.get_file_dict.copy()
        for key in source_dict:
            temp_lst = key.split('/')
            self.files_list.append(temp_lst[-1])
            temp_lst.clear()

    def git_push(self):
        self.add_files_for_commit()
        try:
            path_url = self.git_branch_name.replace('.git','')
            msg = 'Commit from py'
            for file in self.files_list:
                subprocess.run(["git", "add", file], cwd=self.git_clone_path)
            subprocess.run(["git", "commit", "-m", msg], cwd=self.git_clone_path)
            if subprocess.run(["git", "push", "-u", path_url, "master"], cwd=self.git_clone_path):
                my_logger.logger.info("Updated and Pushed successfully")
            else:
                my_logger.logger.error("Error in git_push()")
        except:
            my_logger.logger.error("Error in git_push()")
            print("Error in git_push()")

    def git_pull(self):
        self.parse_data_from_dict()
        try:
            Repo.clone_from(self.git_branch_name, self.git_clone_path)
            # git.Git(self.git_clone_path).clone(self.git_branch_name) it creates another directory
            my_logger.logger.info("Github repository cloned successfully")
            print("Github repository cloned successfully")
        except:
            my_logger.logger.error("Error in git_pull()")
            print("Error in git_pull()")
