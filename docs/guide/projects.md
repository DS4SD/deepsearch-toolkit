!!! tip
        The features described on this page are not available in the public service. [Contact us](https://ds4sd.github.io/) to know more.

# Projects

Deep Search projects allow users to collaborate.
All resources such as data, models and knowledge graphs belong to a project.

A collaborator may be added to a project as `owner`, `editor`, or `viewer`. Below is a description of these roles.

| Role       | Description                          |
| ---------- | ------------------------------------ |
| `viewer`   | Inspect documents, view all project resources, query project knowledge graphs. |
| `editor`   | All permissions of `viewer` + creating and editing new project resources. |
| `owner`    | All permissions of `editor` + possibility to manage collaborators and delete the project. |

## Project management

!!! info
    Make sure to [configure your login](../getting_started/index.md#authentication) before
    using the project management features listed below.

### Creating a project

=== "CLI"

    Using the [`deepsearch cps`](../cli-reference.md#cps) component:
    <div class="termy">

    ```console
    $ deepsearch cps projects create my-project

    key                                       name
    ----------------------------------------  ----------
    d1d526e14cdac562b5174c2df9dd1b04c29a8c33  my-project
    ```

    </div>

=== "Python"

    After you have generated the `api` object (from [login configuration](../getting_started/#authentication)), creating a project is very easy.

    ```python
    proj = api.projects.create(name="my-project")

    print(proj)
    # > Project(key='7be8d8e763b55996710007cf97f31244e8ea237c', name='my-project')
    ```

### Listing projects

=== "CLI"

    Using the [`deepsearch cps`](../cli-reference.md#cps) component:
    <div class="termy">

    ```console
    $ deepsearch cps projects list

    key                                       name
    ----------------------------------------  ---------------------
    d1d526e14cdac562b5174c2df9dd1b04c29a8c33  my-project
    20ae7fb2567d4b777712a6bb50f133c118497d0d  test-project
    1146f5cf2c5ebb4774df38888d5fa608673fca33  it-services
    744978acd58c0cd16893ec4e0ccdd69fd8dd5566  ...
    ```

    </div>

=== "Python"

    After you have generated the `api` object (from [login configuration](../getting_started/#authentication)), listing projects is very easy.

    ```python
    projects = api.projects.list()     # returns list of projects

    for proj in projects:
        print(proj.key, proj.name)

    # If your project uses Pandas, you can easily convert the list of projects to a Dataframe
    import pandas as pd
    df = pd.DataFrame(projects)
    print(df)
    ```

### Removing a project

=== "CLI"

    Using the [`deepsearch cps`](../cli-reference.md#cps) component:
    <div class="termy">

    ```console
    $ deepsearch cps projects remove d1d526e14cdac562b5174c2df9dd1b04c29a8c33
    ```

    </div>

=== "Python"

    After you have generated the `api` object (from [login configuration](../getting_started/#authentication)),
    you can remove a project given its key:

    ```python
    # example project key to delete:
    # proj_key = "7be8d8e763b55996710007cf97f31244e8ea237c"

    api.projects.remove(proj_key=proj_key)
    ```
