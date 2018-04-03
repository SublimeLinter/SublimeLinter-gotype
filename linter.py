from SublimeLinter.lint import Linter, util


class Gotype(Linter):
    cmd = 'gotype'
    regex = r'(?P<filename>^.+):(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    error_stream = util.STREAM_STDERR
    defaults = {
        'selector': 'source.go',
        # we want auto-substitution of the dirname of the file, but `cmd` does not support that yet
        '-e:': '${file_path}'
    }

    def split_match(self, match):
        """Process each match modifying or discarding it."""
        match, line, col, error, warning, message, near = super().split_match(match)
        if match.group("filename") != self.filename:
            return None, None, None, None, None, '', None
        return match, line, col, error, warning, message, near
