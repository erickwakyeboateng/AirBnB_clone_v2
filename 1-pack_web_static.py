#!/usr/bin/python3
# Fabfile helps generate a .tgz archive file from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    date_time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_time.year,
                                                         date_time.month,
                                                         date_time.day,
                                                         date_time.hour,
                                                         date_time.minute,
                                                         date_time.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
