import click
from functions import Functions

func = Functions()

@click.group()
def cli():
    pass

cli.add_command(func.view_status)
cli.add_command(func.ip_scan)

if __name__ == '__main__':
    cli()
