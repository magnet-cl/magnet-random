from artichoke import Config as ArtichokeConfig
from fabric.api import env, task
from os import path

# local and remote paths
env.local_root_dir = path.join(path.dirname(__file__), "..")
env.server_root_dir = 'example/path'

# server domain used by nginx
env.server_domain = 'example.com'

# git repositories
env.server_git_url = 'example/url.git'


class Config(ArtichokeConfig):
    def __init__(self, env, config_file=None):
        super(Config, self).__init__(config_file)

        self.add_section('DB')
        self.add_section('local_DB')
        self.add_section('staging_DB')


@task
def set(host='cl', user='magnet', branch='master', django_port='8000'):
    """ Host, user, branch and django port setter with shortcuts. """
    # host
    if host == 'cl':
        env.hosts = ['example.com']
    else:
        # TODO Validate input
        env.hosts = [host]

    # user
    env.user = user

    # branch and django_port
    env.branch = branch
    env.django_port = django_port
    # if the branch is not master, append it to env.server_root_dir and set
    # django to run on a different port
    if env.branch != 'master':
        env.server_root_dir += '-%s' % env.branch
        env.django_port = int(env.django_port) + 1

    # artichoke config file saved considering branch
    config_file = '%s/config-%s.ini' % (env.local_root_dir, env.branch)
    env.config = Config(env, config_file)
