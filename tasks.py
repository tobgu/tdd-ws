from invoke import task, run


@task
def clean():
    run('rm -rf *.pyc')


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
    run('python webapp.py')
