import ChangeVersion
import GitOperation


go = GitOperation.GitOperation('git_json_file.json')
go.git_pull()
cv = ChangeVersion.ChangeVersion('json_file.json')
cv.replaceversion()
go.git_push()