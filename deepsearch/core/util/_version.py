from dataclasses import dataclass


@dataclass
class VersionSpecs:
    client: str
    server: str


# placeholder values
def get_server_version():
    # TODO
    return "TBA"


def get_client_version():
    import importlib.metadata

    return importlib.metadata.version("deepsearch")


def version() -> VersionSpecs:
    versions = VersionSpecs(
        client=get_client_version(),
        server=get_server_version(),
    )
    return versions
