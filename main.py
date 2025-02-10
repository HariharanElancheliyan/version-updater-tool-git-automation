import ChangeVersion
import GitOperation
import my_logger

print("VERSION UPDATER")
print("================================================\n")
x = (input("You must have to configure JSON file (git_config , file_config) in this directory \n"
           "Make sure to check both file in current directory\n"
           "If you already configured and available \n"
           "PRESS 'Y' and ENTER to continue the update process :"))
print('\n\n')
try:
    if x == 'y' or x == 'Y':
        my_logger.logger.debug("**************** STARTS HERE **********************")
        go = GitOperation.GitOperation('git_config.json')
        go.git_pull()

        cv = ChangeVersion.ChangeVersion('file_config.json')
        cv.replace_version()

        go.git_push()

        my_logger.logger.debug("**************** PROGRAM ENDED **********************")
        my_logger.logger.info("****************************************************")
    print('\n\n\n')

except:
    my_logger.logger.error("Exception Occured", exc_info=True)
    print("Exception Occured !!")

close = input("Press Enter to close")
exit()
