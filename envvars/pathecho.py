import click


@click.command()
@click.option('paths', '--path', envvar='PATH', multiple=True,
              type=click.Path())
def perform(paths):
    for path in paths:
        click.echo(path)

if __name__ == '__main__':
    perform()
