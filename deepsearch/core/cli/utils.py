from functools import wraps

import typer

from deepsearch.core.client.settings import CLISettings


def cli_handler():
    """Decorator for wrapping CLI commands and handling exceptions as controlled via settings"""

    def decorate(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                settings = CLISettings()
                if settings.show_cli_stack_traces:
                    raise e
                else:
                    typer.secho(str(e), fg=typer.colors.RED)
                    raise typer.Exit(code=1)

        return wrap

    return decorate
