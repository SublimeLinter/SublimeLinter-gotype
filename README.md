SublimeLinter-gotype
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-gotype.png?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-gotype)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [gotype](http://godoc.org/code.google.com/p/go.tools/cmd/gotype).
It will be used with files that have the "Go" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please install via [Package Control](https://packagecontrol.io).

Before using this plugin, ensure that `gotype` is installed on your system.
To install `gotype`, do the following:

1. From the command line type the following:

   ```
   go get -u golang.org/x/tools/cmd/gotype
   ```


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Additional SublimeLinter-gotype provides settings:

|Setting|Description         |
|:------|:-------------------|
|gopath |Set a custom GOPATH |

### Settings example
```json
{
    "SublimeLinter": {
        "linters": {
            "gotype": {
                "gopath": "/custom/go/path:/another/go/path"
            }
        }
    }
}
```
