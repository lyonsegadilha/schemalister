#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schemalister.settings")
    os.environ.setdefault("SALESFORCE_CONSUMER_KEY", "schemalistter.setings")
    os.environ.setdefault("SALESFORCE_CONSUMER_SECRET", "schemalister.settings")
    os.environ.setdefault("SALESFORCE_API_VERSION", "41")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
