#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoBlog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "you didnt install django right"
            "follow the instractions right thentry again "
            "come on you can do it"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
