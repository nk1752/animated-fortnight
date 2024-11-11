import os
import yaml
import base64


def build_config():

    # Read the PEM file contents
    # with open("certificate.pem", "r") as pem_file:
    #     pem_content = pem_file.read()

    pem_encoded = "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQ0KICAgICAgICBNSUlFcEFJQkFBS0NBUUVBcnZLZm5MN1o4T0hCUjVROFd1enJ5UjB2L2pVOTZYdXJqRG1JKzh0NWsySHJKMmJoDQogICAgICAgIHBSMEZ0ajdRZlFTaDZqTTdqMUpkMlArY2tad3JPbFgrbitkZlk1THRBc3hsL0I2OFhxTzdmT1FTbWd5TTVaRzYNCiAgICAgICAgb2VaTU42dURmOVcrUTdNUnYzeHo1VjM4ZzRlOEFmRDRncUcwTVpUanpNY000UVgrVmdHeUNHWkdnNmEvdWJ6TQ0KICAgICAgICBPekRReWtaNUdjUWZqTWJsM3MwbjFSamhaMDZFT2NrOEpnN1h0R3lHREZOcjVQMCtGMVl1Z0h2Wm5SSG5IK2JYDQogICAgICAgIEQ1ZnZZYnJDTkFCY0g5dUY5SkQ4Y1Z4ek9wN0FTNVFqRDI1VEYxYmQrMmE1L3IxQUJmZzdMdldtRTdDcSt5ZHoNCiAgICAgICAgLzVjTkpJekdmVzVtVjBaZzRHQ0UvamtQYmYyRWoxK0VsVXdGelFJREFRQUJBb0lCQVFDMVo5ZEZqVGNQc3V3Qg0KICAgICAgICBtVFBwRkVrOFp5WGw2UkwwSEw5ZkdqVTNnUjdFalZvTEtyMmxtY1JKSnpQOHVVVXBUdFhHNFBIa3RNZEJjOHAzDQogICAgICAgIFpYSHhBY2IxdkhoK29yK2h3NXVvenI0WWcxazBMTzd6OWM0VEZMbVFqZDJIbFg4eEk1QzhxakVYUTVPNHlPdEkNCiAgICAgICAgWUdZZTY3QjdZWldXNFFxcGIvUUx4OW9tSWYxa05DMlVWVEcreE80RjZDdk9HSFZXd1ZmSGUxbXNQUXptUS9PSg0KICAgICAgICBUQ1puL1I1KzBMOHE1bVQ2QWZsUWFEQlFVSGtRRlJMRVZvTmRKdk5ZVHhJUmtzWmp3MG9YNmRvSlRPekJnckgyDQogICAgICAgIHpaemN0TG1iOUorVHFGekZPZFowRnowdkNLaFphdi9XMmpEbDVwV2xpVm5sMWV3ek43VnROdStsVnU1S2k2RmINCiAgICAgICAgR3R6KzhGK1pBb0dCQU5YYnZaZjgyVXlLRFo1ZzdUWW1xUGZFY1FqN1pQMk1TNXN6OUxSR1Zha3YzV243UGtpQQ0KICAgICAgICBKcUZKc2prWndsNGViNUxIUnozWlJqazYzTyt5OWx4aERXOCttVjdNamQ4VDdnS3pnVFpLdEk0VjNncndlSW1IDQogICAgICAgIHVaanBQTTZQbU9LVVdFZ3RnK01LRGZWNGt3UEdqOTZnOXh0bHYyMlBPTlAvQmpFeWlmUkVVMG9KQW9HQkFNQ2ENCiAgICAgICAgZGpTcnlhbFZmRHNUTERQcEdzVG8wSThSYUNtOFZ4TmY1SlJUYThGaHpSZDhUazUydjlPcEp0cm1rOEtyelZqRw0KICAgICAgICA5YStuTUZnRGdGeWpWUjk4bDVzV0VvZU12UWYwYWVNazVTSHhPZk9uYVdxS3JOcElaVUV4RjR4R1pMaHNTSDVjDQogICAgICAgIEdnTCtWeEs1Uk1oUzlsMGlJc2NUQ1dVbHEwZTdISk9XMlBzdmsrZzVBb0dBWU1RcTdtTXZQTDRubGhaZzhrNnkNCiAgICAgICAgRytHVkJmdDM4ZzlXbWZ0WENCbTRSQXc0a0I0bmgzUVUybjJ3Vk9ucEZiQ2s4dk01M1VqSmJvQ2Y1L0RRRVltZA0KICAgICAgICAybGIzQUtHQWZkMVdpNlhCKzZGUGRITk85MnRyM2tKZi8yM3lxR0hMNU5rWjhkRFFVaG5TeStmczZQUjlIckx1DQogICAgICAgIGZxQVovQjJNUEZ0Wis1SEFHRFh4UHhzQ2dZRUFrZ1hsQmJLdkYwQlhrOGZwV3grcTZpNU56RHI5N0JwUGU3TUoNCiAgICAgICAgZEhYa1c4TlJFaGZ3V2FSRmVqdkJEWnJzOGorMFZHNFpSYmlIK09QaU5yOHlOSHBoZEVwOGxBZllxZWx4KzhPTQ0KICAgICAgICBvb2Y4dUs0RXlVejhIU2ZHZDlrbXFEVU1seks2YUc3TlFFWkZFeHgxVDAzTUZMcUsxT1BXUUd5b0hMenhxV1dQDQogICAgICAgIDVnaVEzaTBDZ1lFQWx2NU0xQ0s4cjhRazlrTkJnY2JoK2dIOUZ0RkdRR2grZHNNaXF6blJndzRGTlFRNFVhbkINCiAgICAgICAgOE0vSjdNVGV1MWEyK2FzYjBubUFOdWg5U09UNFZDTTd5VjRvck5aN1VMWC9Xc2JOSE9mVXRoSEdUWFdCN0NzbQ0KICAgICAgICBtRUVmdUxuaW92VTVBZUhkakEwek1QbFpGaUw4Q2dyRDRvQTVqaDZUQXE1ejVRaXhPNEFhNmhJPQ0KICAgICAgICAtLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ=="
    pem_decoded = base64.b64decode(pem_encoded).decode("utf-8").replace("\r", "")

    # Define a custom representer that uses `|` for multiline strings
    def str_presenter(dumper, data):
        if "\n" in data:  # Check if the string contains newline characters
            # Use the '|' style for multiline strings
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        # For single-line strings, use the default behavior
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    # Register the custom representer for strings with SafeDumper
    yaml.add_representer(str, str_presenter, Dumper=yaml.SafeDumper)

    fgw_name = "fgw-regionsbank-dev-small-1"

    # Define the data structure as a dictionary and include the PEM content
    data = {
        "apiVersion": "gateway.mulesoft.com/v1alpha1",
        "kind": "Configuration",
        "metadata": {
            "name": fgw_name,
            "namespace": "insert namespace at runtime",
            "labels": {"fgw-name": "runtime insert fg_instance_name"},
        },
        "spec": {
            "logging": {"runtimeLogs": {"logLevel": "info"}},
            "probe": {"enabled": True, "port": 3000},
            "sharedStorage": {
                "redis": {
                    "username": "insert REDIS_USER at runetime",
                    "password": "insert REDIS_PASS at runetime",
                    "address": "insert REDIS_HOST:REDIS_PORT at runtime",
                    "DB": 0,
                    "tls": {
                        "trustedCA": "insert at runtime",
                        "skipValidation": False,
                        "minVersion": "1.1",
                        "maxVersion": "1.3",
                        "alpn": ["h2", "http/1.1"],
                        "ciphers": [
                            "TLS_AES_128_GCM_SHA256",
                            "TLS_AES_256_GCM_SHA384",
                            "TLS_CHACHA20_POLY1305_SHA256",
                            "TLS_RSA_WITH_3DES_EDE_CBC_SHA",
                            "TLS_RSA_WITH_AES_128_CBC_SHA",
                            "TLS_RSA_WITH_AES_256_CBC_SHA",
                            "TLS_RSA_WITH_AES_128_CBC_SHA256",
                            "TLS_RSA_WITH_AES_128_GCM_SHA256",
                            "TLS_RSA_WITH_AES_256_GCM_SHA384",
                            "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA",
                            "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA",
                            "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
                            "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
                            "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                            "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
                            "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
                            "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
                            "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
                            "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
                        ],
                        "certificate": {
                            "key": "insert private key at runtime",
                            "crt": pem_decoded,
                        },
                    },
                }
            },
        },
    }

    # def str_presenter(dumper, data):
    #     if "\n" in data:  # Check for multiline
    #         return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    #     return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    # Add the custom string presenter to use `|` for multiline strings
    # yaml.add_representer(str, str_presenter, Dumper=yaml.SafeDumper)

    # Write the data to a YAML file
    with open("config.yaml", "w") as file:
        yaml.dump(
            data,
            file,
            Dumper=yaml.SafeDumper,
            default_flow_style=False,
            allow_unicode=True,
        )


if __name__ == "__main__":
    build_config()
