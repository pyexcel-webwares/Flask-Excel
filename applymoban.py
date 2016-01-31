from os import path, system


def action(command):
    print(command)
    system(command)

config_dir = 'commons/config'
template_dir = 'commons/templates'

if not path.exists("commons"):
    action("git clone https://github.com/pyexcel/pyexcel-commons.git commons")

action("moban -cd {0} -td {1} .moban.d -t README.rst -o README.rst ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} .moban.d -t setup.py -o setup.py ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} .moban.d -t docs/source/conf.py -o doc/source/conf.py ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} .moban.d -t travis.yml -o .travis.yml ".format(config_dir, template_dir))
action("moban -cd {0} -td .moban.d -t requirements.txt -o requirements.txt ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} -t LICENSE.jj2 -o LICENSE ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} .moban.d -t tests/requirements.txt -o tests/requirements.txt ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} .moban.d -t MANIFEST.in.jj2 -o MANIFEST.in ".format(config_dir, template_dir))
action("moban -cd {0} -td {1} .moban.d -t docs/source/index.rst.jj2 -o doc/source/index.rst ".format(config_dir, template_dir))
