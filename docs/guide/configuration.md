# Configuration

The Toolkit can be configured via the CLI and via environment variables.

Besides *global* settings, the Toolkit also allows the configuration of multiple
*profiles* for enabling users to easily work with different Deep Search deployments.

## Profiles

The Toolkit provides the capability of easily interacting with different Deep Search
instances through the use of *profiles*. A user may define multiple profiles, identified
by profile name, and can easily switch between them.

### Profile Setup

To configure your Deep Search profile, check out [Set up your Profile](../index.md#set-up-your-profile).

### Command Overview

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

To use the active profile:
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

To use specific settings:
```python
from deepsearch.core.client.settings import ProfileSettings
from deepsearch.cps.client.api import CpsApi

# create a ProfileSettings object, e.g.:
settings = ProfileSettings(
    # ...
)
# or interactively via the CLI:
# settings = ProfileSettings.from_cli_prompt()

api = CpsApi.from_settings(settings=settings)

print([p.name for p in api.projects.list()])
# -> outputs projects corresponding to provided settings
```

## Environment Variables

Under the hood, the Toolkit leverages [Pydantic Settings with dotenv
support][pydantic_settings], so configuration settings can be easily overriden via
environment variables. This can be useful e.g. in a containerization scenario.

To see which environment variables are supported, check the relevant [Pydantic Settings
classes][settings_file], also taking into account any defined prefixes.

[pydantic_settings]: https://docs.pydantic.dev/dev-v1/usage/settings
[settings_file]: https://github.com/DS4SD/deepsearch-toolkit/blob/main/deepsearch/core/client/settings.py
