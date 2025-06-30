from psycopg_pool import ConnectionPool

pool = ConnectionPool(
    conninfo="dbname=avo_users user=adminavo password=$#fKcdXPg4@ue8AW host=avo-adb-001.postgres.database.azure.com",
    max_size=10,
)
