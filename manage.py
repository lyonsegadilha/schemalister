#!/usr/bin/env python
import os
import sys
import django.core.management

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schemalister.settings")
    os.environ.setdefault("SALESFORCE_CONSUMER_KEY", "23423")
    os.environ.setdefault("SALESFORCE_CONSUMER_SECRET", "234234")
    os.environ.setdefault("SALESFORCE_API_VERSION", "41")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
