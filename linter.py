#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell
# Copyright (c) 2014 Jon Surrell
#
# License: MIT
#

"""This module exports the Gotype plugin class."""

from os import listdir
from os.path import dirname
from SublimeLinter.lint import Linter, util


class Gotype(Linter):

    """Provides an interface to gotype."""

    syntax = ('go', 'gosublime-go')
    cmd = ('gotype', '-e', '-a', '.')
    regex = r'^.+:(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    error_stream = util.STREAM_STDERR

    def __init__(self, view, syntax):
        """Initialize and load GOPATH from settings if present."""
        super(Gotype, self).__init__(view, syntax)

        gopath = self.get_view_settings().get('gopath')
        if gopath:
            if self.env:
                self.env['GOPATH'] = gopath
            else:
                self.env = {'GOPATH': gopath}

    def run(self, cmd, code):
        """Copy package files to temp dir."""
        files = [f for f in listdir(dirname(self.filename)) if f[-3:] == '.go']
        return self.tmpdir(cmd, files, code)
