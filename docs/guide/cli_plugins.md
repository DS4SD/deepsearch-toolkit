# CLI plugins

We use [Pluggy](https://pluggy.readthedocs.io/en/stable/index.html) to extend the DeepSearch CLI. We recommend having a look at it's documentation for further details.

## Writing a CLI plugin

We use [Typer](https://typer.tiangolo.com) on the DeepSearch CLI. We recommend having a look at it's tutorial, which goes into further detail on how to use this library. In the example file below, we use the `hookimpl` to add our own CLI command group.

The main requirements are:

- Your hook implementation must return a `typer.Typer` instance
- The instance must have a `name` set

Consider the following toy example:

```python
# my_deepsearch_plugin/main.py

import typer

# Get the hookimpl that you will use to hook into the DeepSearch CLI
from deepsearch.core.cli.plugins import deepsearch_cli_hookimpl

# Implement the function to return a group.
# We're defining an 'example' group,
# using the Typer library.
# It will be available as 'deepsearch example'.
# Note: the name of the function is important!
@deepsearch_cli_hookimpl
def deepsearch_cli_add_group() -> typer.Typer:
    app = typer.Typer(name="example")

    # Define one or more commands.
    @app.command("test")
    def test(name: str):
        typer.echo(f"Hello, {name}!")

    return app
```

You can use any of the `deepsearch` package's contents to write your CLI plugins. See [deepsearch/examples](../deepsearch/plugins/) for more examples.

## Adding the plugin to your package

Pluggy makes use of setuptools entry points to load plugins. Here's how you can add yours:

### Via `setup.py`

Add a `entry_points` argument to your `setup.py`, replacing `my_deepsearch_plugin.main` to point to the file where you defined your plugin.

```python
setup(
    entry_points={
        "deepsearch": ["cli = my_deepsearch_plugin.main"],
    }
)
```

### Via Poetry with `pyproject.toml`

Add the following to your `pyproject.toml`, replacing `my_deepsearch_plugin.main` to point to the file where you defined your plugin.

```toml
[tool.poetry.plugins.deepsearch]
cli = "my_deepsearch_plugin.main"
```

## Using the plugin

After installing your plugin package, you should see the `example` section when you run `deepsearch`:

```
> deepsearch

Usage: deepsearch [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  config   Manage CLI config files
  cps      Interact with DeepSearch CPS component
  example
  login    Login to DeepSearch platform
  query    Interact with DeepSearch Query component
  version  Print the client and server version information
```

And running our newly added command gives us...

```
> deepsearch example test DeepSearch

Hello, DeepSearch!
```
