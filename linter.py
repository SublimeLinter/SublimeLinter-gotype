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
    cmd = None
    executable = 'gotype'
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

    def cmd(self):
        """Generate the linter command string"""
        return [self.executable_path, '-e', '-a', '-r='+self.filename, '.')

