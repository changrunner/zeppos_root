# zeppos_root

## Find the root of a project
In python there is no easy way to find the root of a project unlike other languages like .NET
This library makes this easy.

Two things you will need to do:
- Identify a file you want to indicate the root of your project.

``` For example a .root file```

- Call the method

```
from zeppos_root import Root

the_root = Root.find_root_of_project(__file__)
the_root = Root.find_root_of_project(
    current_module_filename=__file__,
    root_marker_filename_list=".root"
)
```