import csv
import io
from functools import wraps
import inspect

from .validation import validate
from .options import apply_options


class QuikCSV:

    @staticmethod
    def one(data, arg=None, opts=None):
        def outer(func):
            @wraps(func)
            def inner(*args, **kwargs):
                validate(data)
                data_ = apply_options(data, opts)
                tmp_csv = io.StringIO()
                try:
                    writer = csv.writer(tmp_csv)
                    writer.writerows(data_)
                    tmp_csv.seek(0)
                    if arg:
                        arg_names = inspect.getfullargspec(func).args
                        index = arg_names.index(arg)
                        args = args[:index] + args[index+1:]
                        args = args[:index] + (tmp_csv,) + args[index:]
                        res = func(*args, **kwargs)
                    else:
                        res = func(tmp_csv, *args, **kwargs)
                finally:
                    tmp_csv.close()
                return res
            return inner
        return outer
