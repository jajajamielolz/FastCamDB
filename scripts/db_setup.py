"""DB setup script."""
import os
import sys

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

sys.path.append(os.getcwd())


from app.core.config import config  # noqa


def main():
    """Set up postgres db."""
    conn = connect(
        dbname=config.DB_DATABASE,
        user=config.DB_SUPERUSER,
        host=config.DB_HOSTNAME,
        password=config.DB_SUPERPASSWORD,
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    print("Creating User {} ...".format(config.DB_USERUSER))
    try:
        cursor.execute(
            "CREATE USER {} WITH PASSWORD %s".format(config.DB_USERUSER),
            (config.DB_USERPASSWORD,),
        )
    except Exception as e:
        print(e)

    print("Giving {} Permissions to public...".format(config.DB_USERUSER))
    try:
        cursor.execute(
            "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO {}".format(
                config.DB_USERUSER
            )
        )
    except Exception as e:
        print(e)

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
