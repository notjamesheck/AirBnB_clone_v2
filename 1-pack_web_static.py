#!/usr/bin/python3
"""
Fabric script that generates .tgz archive from the contents of web_static
"""

from fabric.api import *
from datetime import datetime


def do_pack():
    current = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            current))
        return ("versions/web_static_{}.tgz".format(current))
    except:
        return None
