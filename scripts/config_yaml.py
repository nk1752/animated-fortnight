import os
import yaml
import base64


def build_config():
    print("build config function")

    # read pem file


    with open("certificate.pem", "r") as f:
        pem_encoded = f.read()
    pem_decoded = base64.b64decode(pem_encoded).decode("utf-8").replace("\r", "")

    config = {
        "bg_name": "test",
        "crt": pem_decoded,
    }
    print(config)

    with open("config.yaml", "w") as f:
        yaml.dump(config, f, default_flow_style=False)


if __name__ == "__main__":
    build_config()
