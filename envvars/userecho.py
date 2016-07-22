import click


@click.command()
@click.option('--username', envvar='PWD')
def greet(username):
    click.echo('Hello %s' % username)

if __name__ == '__main__':
    greet()
