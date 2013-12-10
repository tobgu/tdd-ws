from invoke import task, run


@task
def clean():
    run("find . -name '*.pyc' -delete")


@task
def analysis():
    run('flake8 .')


@task
def tests(continuously=False):
    if continuously:
        run('sniffer')
    else:
        run('nosetests')


@task
def webapp():
    run('python src/webapp.py')
