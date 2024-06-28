import psycopg2

try:
    # Establish the connection
    connection = psycopg2.connect(
        user="postgres",
        password="kasuku",
        host="127.0.0.1",
        port="5432",
        database="mwangihub_use_docker_1"
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Print PostgreSQL details
    print("PostgreSQL connection is open")

    # Execute a simple SQL query
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Closing database connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
