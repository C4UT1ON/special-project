<<<<<<< HEAD
#!/usr/bin/env python3.6
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'special_project_api.settings')
=======
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reservation_system.settings')
>>>>>>> 9142a665114861ff7c76413fa1846192ce1e6da6
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
<<<<<<< HEAD
=======


if __name__ == '__main__':
    main()
>>>>>>> 9142a665114861ff7c76413fa1846192ce1e6da6