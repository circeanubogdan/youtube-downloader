import click


@click.command()
@click.argument("link", type=str)
def _main(link):
    pass


if __name__ == "__main__":
    _main()
