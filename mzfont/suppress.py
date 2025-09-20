from os import O_RDWR, close, devnull, dup, dup2, open as os_open


class suppress_output:
    '''Context manager to suppress output.'''
    def __enter__(self):
        self.stdout_fd = dup(1)
        self.stderr_fd = dup(2)

        self.devnull = os_open(devnull, O_RDWR)
        dup2(self.devnull, 1)
        dup2(self.devnull, 2)

    def __exit__(self, exc_type, exc_value, traceback):
        dup2(self.stdout_fd, 1)
        dup2(self.stderr_fd, 2)
        close(self.devnull)
        close(self.stdout_fd)
        close(self.stderr_fd)
