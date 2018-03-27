import os
from os.path import dirname
import logging

from SublimeLinter.lint import Linter, util


logger = logging.getLogger(__name__)


class GotypeLinter(Linter):
    executable = "gotype"
    regex = r'(?P<filename>^.+):(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    defaults = {
        'selector': 'source.go'
    }

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
