"""
Django command to wait for teh database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for the database...')
        db_down = True
        while db_down:
            try:
                self.check(databases=['default'])
                db_down = False
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting for 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
