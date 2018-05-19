from SublimeLinter.lint import Linter, util
from SublimeLinter.lint.linter import substitute_variables


class Gotype(Linter):
    cmd = ('gotype', '-t', '-e', '${file_path}')
    regex = r'(?P<filename>^.+):(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    error_stream = util.STREAM_STDERR
    tempfile_suffix = '-'
    defaults = {
        'selector': 'source.go'
    }

    def split_match(self, match):
        """Process each match modifying or discarding it."""
        match, line, col, error, warning, message, near = super().split_match(match)
        if match.group("filename") != self.filename:
            return None, None, None, None, None, '', None
        return match, line, col, error, warning, message, near

    def finalize_cmd(self, cmd, context, **kwargs):
        return substitute_variables(context, cmd)
