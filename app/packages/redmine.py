import click
import os
from redminelib import Redmine

# リクエスト設定
redmine = Redmine('http://' + os.environ.get('REDMINE_API'),
                  key=os.environ.get('API_ACCESS_KEY'))

# プロジェクトの作成コマンド
@click.command(help="create project")
@click.option('--indentifier', '-i', help=u'project identifier', required=True)
@click.option('--production',  '-p', is_flag=True, help=u'add production project')
@click.option('--prototype',  '-pt', is_flag=True, help=u'add prototype project')
@click.option('--sandbox',  '-sb', is_flag=True, help=u'add sandbox project')
def create(indentifier, production, prototype, sandbox):
    if production:
        redmine.project.create(name=indentifier, identifier=indentifier)
        print('production project created')

    if prototype:
        redmine.project.create(
            name=indentifier + '-prototype', identifier=indentifier + '-prototype')
        print('prototype project created')

    if sandbox:
        redmine.project.create(
            name=indentifier + '-sandbox', identifier=indentifier + '-sandbox')
        print('sandbox project created')

# プロジェクトのリスト表示コマンド
@click.command(help="list projects")
def list():
    projects = redmine.project.all()
    for project in projects:
        print(project.identifier)

# プロジェクトの削除コマンド
@click.command(help="delete project")
@click.option('--indentifier', '-i', help=u'project identifier', required=True)
@click.option('--production',  '-p', is_flag=True, help=u'delete production project')
@click.option('--prototype',  '-pt', is_flag=True, help=u'delete prototype project')
@click.option('--sandbox',  '-sb', is_flag=True, help=u'delete sandbox project')
def delete(indentifier, production, prototype, sandbox):
    if production:
        redmine.project.get(indentifier).delete()
        print('production project deleted')

    if prototype:
        redmine.project.get(indentifier + '-prototype').delete()
        print('prototype project deleted')

    if sandbox:
        redmine.project.get(indentifier + '-sandbox').delete()
        print('sandbox project deleted')


# コマンド構成
@click.group(help="command for project")
def project():
    pass


project.add_command(create)
project.add_command(list)
project.add_command(delete)


@click.group(help="command for redmine")
def cli():
    pass


cli.add_command(project)

if __name__ == "__main__":
    cli()
