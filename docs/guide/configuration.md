# Configuration

The Toolkit can be configured via the CLI and via environment variables.

Besides global settings, the Toolkit also allows the configuration of multiple
profiles for enabling users to easily work with different Deep Search deployments.

## Profiles

The Toolkit provides the capability of easily interacting with different Deep Search
instances through the use of *profiles*. A user may define multiple profiles, identified
by profile name, and can easily switch between them.

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

To set up a profile use `deepsearch profile config`, providing options as needed (for a
full reference check `deepsearch profile config --help`).

Here is a basic invocation example:

```console
$ deepsearch profile config
Host: https://deepsearch-experience.res.ibm.com
Username: name@example.com
Api key:
```

!!! note
    If you had used the meanwhile deprecated `deepsearch login` command to set up a
    config file in the default location, that will automatically be migrated to a profile.

### Usage

#### Usage in CLI

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

#### Usage in Python

To use the active profile (recommended usage pattern):
```python
from deepsearch.cps.client.api import CpsApi

api = CpsApi.from_env()

print([p.name for p in api.projects.list()])
# -> outputs projects corresponding to active profile
```

To use a specific profile:
```python
from deepsearch.cps.client.api import CpsApi

api = CpsApi.from_env(profile_name="foo")

print([p.name for p in api.projects.list()])
# -> outputs projects corresponding to "foo"
```

## Environment variables

Under the hood, the Toolkit leverages [Pydantic Settings with dotenv
support][pydantic_settings], so configuration settings can be easily overriden via
environment variables. This can be useful e.g. in a containerization scenario.

To see which environment variables are supported, check the following Pydantic Settings
classes, also taking into account the respective prefixes:

| Class | Prefix | Description |
| --- | --- | --- |
| [`ProfileSettings`][settings_file] | `DEEPSEARCH_PROFILE_` | Profile settings (e.g. host, port etc.) |
| [`ModelAppSettings`][model_app_settings] | `DEEPSEARCH_MODELAPP_` | Model app settings |
| [`ArtifactSettings`][artifact_settings] | `DEEPSEARCH_ARTIFACT_` | Artifact management settings |
| [`CLISettings`][cli_settings] | `DEEPSEARCH_CLI_` | Command line utility settings |
| [`PrflManagerSettings`][settings_file] | `DEEPSEARCH_PRM_` |  Profile manager settings (e.g. which profile to use) |

For instance, `DEEPSEARCH_PROFILE_*` environment variables, i.e. `DEEPSEARCH_PROFILE_HOST` etc.
(see [`ProfileSettings`][settings_file]), can be used for injecting profile data even if
no profile has been configured.

!!! note

    When extending the settings (e.g. as for the [model app][model_app_settings]),
    developers must ensure `env_prefix` is [properly set][settings_file] to prevent
    conflicts.

[pydantic_settings]: https://docs.pydantic.dev/dev-v1/usage/settings
[settings_file]: https://github.com/DS4SD/deepsearch-toolkit/blob/main/deepsearch/core/client/settings.py
[model_app_settings]: https://github.com/DS4SD/deepsearch-toolkit/blob/main/deepsearch/model/server/config.py
[artifact_settings]: https://github.com/DS4SD/deepsearch-toolkit/blob/main/deepsearch/artifacts/settings.py
[cli_settings]: https://github.com/DS4SD/deepsearch-toolkit/blob/main/deepsearch/core/cli/settings.py
