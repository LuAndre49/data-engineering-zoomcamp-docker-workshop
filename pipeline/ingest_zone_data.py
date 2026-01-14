import pandas as pd
from sqlalchemy import create_engine
import click


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
def main(pg_user, pg_pass, pg_host, pg_port, pg_db):
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
    df = pd.read_csv(url)
    df.to_sql(name="zones", con=engine, if_exists='replace')
    print('done')


if __name__ == '__main__':
    main()