import yaml

yaml_file = open("filename.yaml", "r")
contents = yaml.safe_load(yaml_file)
yaml_file.close()
print(contents)


from pathlib import Path
import yaml

file_path = "/home/user/scripts/file.yaml"
file_contents = Path(file_path).read_text()
yaml_content = yaml.load(file_contents)
