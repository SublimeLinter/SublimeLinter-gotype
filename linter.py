from SublimeLinter.lint import Linter, util


class Gotype(Linter):
    cmd = ('gotype', '-t', '-e', '${file_path}')
    regex = r'(?P<filename>^.+):(?P<line>\d+):(?P<col>\d+):\s+(?P<message>.+)'
    error_stream = util.STREAM_STDERR
    tempfile_suffix = '-'
    defaults = {
        'selector': 'source.go'
    }

    def split_match(self, match):
        if match.group('filename') == self.filename:
            return super().split_match(match)
