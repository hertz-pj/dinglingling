import datetime
import traceback
import functools
import socket
import os
import requests

DATE_FORMAT = "%Y-%m-%d %H:%M:%d"


def wx_reminder(SCKEY, proxy: str="", remind_started: bool=False):
    """[summary]
    
    Arguments:
        SCKEY {[str]} -- [the sckey you get from http://sc.ftqq.com/3.version]
    
    Keyword Arguments:
        proxy {str} -- [if you use the proxy] (default: {""})
        reminder_start {bool} -- [if you want remind you when the function start] (default: {False})
    
    Raises:
        ex: [description]
    
    Returns:
        [type] -- [description]
    """

    if len(proxy) != 0:
        os.environ["http_proxy"] = proxy
        os.environ["https_proxy"] = proxy

    def decorator_sender(func):
        @functools.wraps(func)
        def wrapper_sender(*args, **kwargs):

            start_time = datetime.datetime.now()
            host_name = socket.gethostname()
            func_name = func.__name__

            title = "Your_training_has_started."
            contents = [
                        'Machine name: %s' % host_name,
                        'Main call: %s' % func_name,
                        'Starting date: %s' % start_time.strftime(DATE_FORMAT)]
            content = '\n\n'.join(contents)
            
            data = {
                "text":title,
                "desp":content
            }

            url = f"https://sc.ftqq.com/{SCKEY}.send"

            if remind_started:
                requests.post(url, data)

            try:
                value = func(*args, **kwargs)
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                title = "Your_training_is_complete."
                contents = [
                            'Machine name: %s' % host_name,
                            'Main call: %s' % func_name,
                            'Starting date: %s' % start_time.strftime(DATE_FORMAT),
                            'End date: %s' % end_time.strftime(DATE_FORMAT),
                            'Training duration: %s' % str(elapsed_time)]
                content = '\n\n'.join(contents)

                data = {
                    "text":title,
                    "desp":content
                }

                requests.post(url, data)

                return value

            except Exception as ex:
                end_time = datetime.datetime.now()
                elapsed_time = end_time - start_time

                title = "Your_training_has_crashed."
                contents = [
                            'Machine name: %s' % host_name,
                            'Main call: %s' % func_name,
                            'Starting date: %s' % start_time.strftime(DATE_FORMAT),
                            'Crash date: %s' % end_time.strftime(DATE_FORMAT),
                            'Crashed training duration: %s\n\n' % str(elapsed_time),
                            "Here's the error:",
                            '%s\n\n' % ex,
                            "Traceback:",
                            '%s' % traceback.format_exc()]
                content = '\n\n'.join(contents)

                data = {
                    "text":title,
                    "desp":content
                }

                requests.post(url, data)
                
                raise ex

        return wrapper_sender

    return decorator_sender