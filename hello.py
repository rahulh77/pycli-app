import click


@click.group()
def cli():
    pass

# Groups can have commands
@cli.command()
# If the attribute has hyphen, it should be passed as underscore (user-name -> user_name) in function
@click.option('--user-name', '-u', default='World', help='This is the thing that is greeted.')
@click.option('--repeat', '-r', default=1, help='How many times you want to be greeted.')
@click.argument('out', type=click.File('w'), default='-', required=False)  # Hyphen wil write to stdout
def clifunction(user_name, repeat, out):
    """ Prints cli function """
    for x in range(repeat):
        # print(f'Hello {name}')
        click.echo(f'Hello {user_name}', file=out)
