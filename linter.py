#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jon Surrell
# Copyright (c) 2014 Jon Surrell
#
# Wonyoung Ju make it compatible with SublimeLinter4 at 2018.03
#
# License: MIT
#

"""This module exports the GotypeLinter plugin class."""

import os
from os.path import dirname
import logging

from SublimeLinter.lint import Linter, util  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


logger = logging.getLogger(__name__)


class GotypeLinter(Linter):
    """Provides an interface to gotype."""

    syntax = ('go', 'gosublime-go')
    executable = "gotype"
    regex = r'(?P<filename>^.+):(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'

    def cmd(self):
        """Return the command line to run."""
        return [self.executable_path, "-e", dirname(self.filename)]

    def communicate(self, cmd, code=None):
        """Customize Linter.communicate for pulling unnecessary file name off."""
        settings = self.get_view_settings()
        cwd = self.get_working_dir(settings)
        env = self.get_environment(settings)

        if logger.isEnabledFor(logging.INFO):
            logger.info('{}: {} {}'.format(
                self.name,
                os.path.basename(self.filename or '<unsaved>'),
                cmd)
            )
            if cwd:
                logger.info('{}: cwd: {}'.format(self.name, cwd))

        return util.communicate(
            cmd,
            code,
            output_stream=self.error_stream,
            env=env,
            cwd=cwd)

    def split_match(self, match):
        """Process each match modifying or discarding it."""
        match, line, col, error, warning, message, near = super().split_match(match)
        if match.group("filename") != self.filename:
            return None, None, None, None, None, '', None
        return match, line, col, error, warning, message, near
