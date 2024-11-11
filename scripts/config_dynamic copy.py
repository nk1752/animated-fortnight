import os
import yaml
import base64


def build_config():

    # Read the PEM file contents
    with open('certificate.pem', 'r') as pem_file:
        pem_content = pem_file.read()

    #pem_content = pem_content.replace('\r', '')


    # Define the data structure as a dictionary
    import yaml

    class MyDumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super(MyDumper, self).increase_indent(flow, False)

    # Define the data structure as a dictionary and include the PEM content
    data = {
        'version': '1.0',
        'components': {
            'database': {
                'type': 'PostgreSQL',
                'version': '13',
                'settings': {
                    'host': 'localhost',
                    'port': 5432
                }
            },
            'webserver': {
                'type': 'nginx',
                'port': 80,
                'ssl': True,
                'certificate': pem_content  # Adding PEM file content here
            }
        },
        'environment': ['production', 'staging']
    }

    # def str_presenter(dumper, data):
    #     if "\n" in data:  # Check for multiline
    #         return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    #     return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    # Add the custom string presenter to use `|` for multiline strings
    #yaml.add_representer(str, str_presenter, Dumper=yaml.SafeDumper)

    # Write the data to a YAML file
    with open("config.yaml", "w") as file:
        yaml.dump(data, file, Dumper=MyDumper, default_flow_style=False, allow_unicode=True)



if __name__ == "__main__":
    build_config()
