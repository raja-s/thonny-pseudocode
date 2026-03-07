
# thonny-pseudocode

A [Thonny](https://thonny.org/) plugin that generates inline pseudocode on-demand, explaining the Python source code line-by-line, powered by the [PyToPseu project](https://github.com/jppellet/PyToPseu).

Table of contents:<br/>
[Installation](#installation)<br/>
[User Guide](#user-guide)<br/>
[Limitations](#limitations)

## Installation

Inside Thonny, click on `Tools` > `Manage plug-ins...` to open the plug-ins dialog.
Search for the "thonny-pseudocode" package and install it.
**Make sure your installed version is at least 0.1.3.**

Once installed, restart Thonny to load the plug-in.

## User Guide

You can generate pseudocode with the plug-in's "Explain with pseudocode" command. There are 3 ways to trigger the command:

1) From the menu:

![Generating the pseudocode from the menu](/demos/trigger_menu-item.gif)

2) From the toolbar:

![Generating the pseudocode from the toolbar](/demos/trigger_toolbar-item.gif)

3) Using the Ctrl+E/Cmd+E hotkey:

![Generating the pseudocode using the hotkey](/demos/trigger_hotkey.gif)

Once generated, the command may be used again to erase the generated pseudocode:

> Note: When the plugin erases generated pseudocode, it will systematically remove all trailing whitespaces on all lines.

![Erasing the pseudocode](/demos/generate-erase.gif)

Since the generated pseudocode is actually appended to the source code in the form of comments (preserving the developer's own comments), the developer may continue to edit the code afterwards.
Using the command again on edited code will immediately regenerate pseudocode for the new code.
As soon as the command is used a second time on a particular piece of code, the plug-in will erase the generated pseudocode.

![Erasing the pseudocode](/demos/generate-regenerate-erase.gif)

## Limitations

The plugin currently has the following limitations:
- It cannot generate pseudocode for code with the slightest syntax error
- Generated pseudocode goes into the editing history and "pollutes" it, which means that erasing pseudocode then undoing the last change will bring back the pseudocode
