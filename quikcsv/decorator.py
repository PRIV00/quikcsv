import csv
import io
from functools import wraps
import inspect

from .validation import validate
from .options import apply_options


def QuikCSV(datasets):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            csvs = []
            validate(datasets)
            try:
                for dataset in datasets:
                    data_ = apply_options(
                        dataset['data'],
                        dataset.get('opts')
                    )
                    stream = io.StringIO()
                    writer = csv.writer(stream)
                    writer.writerows(data_)
                    stream.seek(0)
                    if dataset.get('arg'):
                        arg_names = inspect.getfullargspec(func).args
                        index = arg_names.index(dataset['arg'])
                        args = args[:index] + args[index+1:]
                        args = args[:index] + (stream,) + args[index:]
                    else:
                        csvs.append(stream)
                if len(csvs) > 0:
                    return func(csvs, *args, **kwargs)
                else:
                    return func(*args, **kwargs)
            finally:
                for stream in csvs:
                    stream.close()
        return inner
    return outer
