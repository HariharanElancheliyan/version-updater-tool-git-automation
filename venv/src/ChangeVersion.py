import json
import my_logger

get_file_dict = {}


class ChangeVersion:

    # JSON file loaded in constructor
    def __init__(self, json_path):
        my_logger.logger.info("----------------------------------------")
        self.json_path = json_path

        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                my_logger.logger.info("Json File Opened Successfully")
                data = json.load(file)
                self.data = data
                self.files_dict = {}

        except FileNotFoundError:
            my_logger.logger.error("FileNotFoundError Exception occurred", exc_info=True)
            msg = "Sorry, the file " + json_path + " does not exist."
            print(msg)

    # Load JSON file to Dict
    def loadjsontomap(self):
        try:
            for path in self.data:
                key = path
                value = self.data[path]
                self.files_dict[key] = value
                get_file_dict[key] = value
                my_logger.logger.info("{} filepath added to dict Successfully".format(key))
            print(self.files_dict)

        except AttributeError:
            my_logger.logger.error("AttributeError Exception occurred", exc_info=True)
            msg = "Attribute Error occurred !!"
            print(msg)

    # From Dict, we replace the version to file
    def replaceversion(self):
        self.loadjsontomap()
        try:
            for key, value in self.files_dict.items():
                version_number = value
                comma_version_number = version_number.replace('.', ',')

                c_fileversion = "FILEVERSION"
                s_fileversion = "FileVersion"

                c_productversion = "PRODUCTVERSION "
                s_productversion = "ProductVersion"

                linenumber = 0
                c_fv_line_number = 0
                s_fv_line_number = 0

                c_pv_line_number = 0
                s_pv_line_number = 0

                with open(key, 'r', encoding='utf-8') as rc_file:
                    data = rc_file.readlines()
                    my_logger.logger.info("{} file opened".format(key))
                    for line in data:
                        linenumber += 1
                        if c_fileversion in line:
                            c_fv_line_number = linenumber
                        if s_fileversion in line:
                            s_fv_line_number = linenumber
                        if c_productversion in line:
                            c_pv_line_number = linenumber
                        if s_productversion in line:
                            s_pv_line_number = linenumber

                # Changing File Version
                data[c_fv_line_number - 1] = " " + c_fileversion + " " + comma_version_number + '\n'
                data[
                    s_fv_line_number - 1] = '            VALUE \"FileVersion\",' + ' ' + '\"' + version_number + '\"' + '\n'

                # Changing Product Version
                data[c_pv_line_number - 1] = " " + c_productversion + " " + comma_version_number + '\n'
                data[
                    s_pv_line_number - 1] = '            VALUE \"ProductVersion\",' + ' ' + '\"' + version_number + '\"' + '\n'

                # writing to a file
                with open(key, 'w', encoding='utf-8') as file:
                    file.writelines(data)
                my_logger.logger.info("Version edited successfully")
                print("Successfully Edited")
        except:
            print("Exception Occurred")
            my_logger.logger.error("Exception occurred while changing version in .rc file", exc_info=True)
