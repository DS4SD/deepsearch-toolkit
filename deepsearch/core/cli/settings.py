from deepsearch.core.client.settings import DSSettings, SubPrefix


class CLISettings(DSSettings):
    class Config:
        env_prefix = DSSettings.build_prefix(sub_prefix=SubPrefix.CLI)

    show_stacktrace: bool = False
