# Projects

Deep Search projects allow users to collaborate.
All resources such as data, models and knowledge graphs belog to a project.

Collaborators may be added to a project as `owners`, `editors` or `viewers`. Below is a description of the roles.

| Role       | Description                          |
| ---------- | ------------------------------------ |
| `viewer`   | Inspect documents, view all project resources, query project knowledge graphs. |
| `editor`   | All permissions of `viewer` + creating and editing new project resources. |
| `owner`    | All permissions of `editor` + possibility to manage collaborators and delete the project. |



## Listing projects

!!! info
    Please [configure your login](../getting_started/authentication.md) before trying these examples.

=== "CLI"

    Using the [`deepsearch cps`](../cli-reference.md#cps) component:
    <div class="termy">

    ```console
    $ deepsearch cps projects list

    key                                       name
    ----------------------------------------  ---------------------
    c5e1f35a57e1a538c111c59752f06df07aab6c91  dev
    20ae7fb2567d4b777712a6bb50f133c118497d0d  MyProjects
    1146f5cf2c5ebb4774df38888d5fa608673fca33  IT Services
    744978acd58c0cd16893ec4e0ccdd69fd8dd5566  ...
    ```

    </div>

=== "Python"

    After you have generated the api object (from [login configuration](../getting_started/authentication.md)), listing projects is very easy.

    ```python
    projects = api.projects.list()     # returns list of projects

    for proj in projects:
        print(proj.key, proj.name)

    # If your project uses Pandas, you can easily convert the list of projects to a Dataframe
    import pandas as pd
    df = pd.DataFrame(projects)
    print(df)
    ```
