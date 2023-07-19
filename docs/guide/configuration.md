# Configuration

The Toolkit can be configured both via the CLI and via
environment variables.

Besides *global* settings, the Toolkit also allows the configuration of multiple
*profiles* for enabling users to easily work with different Deep Search deployments.

## Profiles

### Overview

For an overview of the profile management commands check `deepsearch profile --help`:
```console
$ deepsearch profile --help

 Usage: deepsearch profile [OPTIONS] COMMAND [ARGS]...

 Manage profile configuration

╭─ Options ──────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                    │
╰────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────╮
│ config         Add or update a profile.                        │
│ list           List all profiles.                              │
│ remove         Remove a profile.                               │
│ show           Display a profile.                              │
│ use            Activate a profile.                             │
╰────────────────────────────────────────────────────────────────╯
```

### Profile setup

To setup a profile use [`deepsearch profile config`](../cli-reference.md#profile),
providing options as needed (for a full reference run with `--help`).

Here is a basic invocation example:

```console
$ deepsearch profile config
Host: https://deepsearch-experience.res.ibm.com
Username: name@example.com
Api key:
```

> NOTE: If you had used the meanwhile deprecated `deepsearch login` command to set up a
config file in the default location, that will automatically be migrated to a profile.

### Usage

Here some usage examples:

=== "CLI"

    ```console
    $ # configure a profile
    $ deepsearch profile config --profile-name foo --host ds-1.example.com ...
    $ # -> "foo" now available and selected as the active profile
    $
    $ deepsearch cps projects list
    $ # -> outputs projects corresponding to "foo"
    $
    $ # configure another profile
    $ deepsearch profile config --profile-name bar --host ds-2.example.com ...
    $ # -> "bar" now available and selected as the active profile
    $
    $ deepsearch profile list
    $ # -> displays all profiles, with "bar" marked as the active one
    $
    $ deepsearch cps projects list
    $ # -> outputs projects corresponding to "bar"
    $
    $ # switch to previous profile
    $ deepsearch profile use foo
    $ # -> "foo" now selected as the active profile
    $
    $ deepsearch cps projects list
    $ # -> outputs projects corresponding to "foo"
    ```

=== "Python"

    ```python
    from deepsearch.cps.client.api import CpsApi

    # using the active profile; let's assume that is "foo"
    api = CpsApi.from_env()
    print([p.name for p in api.projects.list()])
    # -> outputs projects corresponding to "foo"

    # using a profile by name
    api = CpsApi.from_env(profile_name="bar")
    print([p.name for p in api.projects.list()])
    # -> outputs projects corresponding to "bar"
    ```

---


## Environment variables

Under the hood, configuration management in the Toolkit is implemented based on [Pydantic
Settings with dotenv support](https://docs.pydantic.dev/1.10/usage/settings).

Configuration is persisted in Toolkit-managed dotenv files, but can be overriden via
environment variables.

To see which environment variables are supported, check the relevant [Pydantic Settings
classes][settings_file], also taking into account any defined prefixes.

For example you can set the profile for the scope of a single operation (e.g. a project
listing) as follows:

```console
DEEPSEARCH_PROFILE=bar deepsearch cps projects list
```

[settings_file]: https://github.com/DS4SD/deepsearch-toolkit/blob/main/deepsearch/core/client/settings.py
