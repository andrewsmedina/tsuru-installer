class Vagrant(object):
    name = "vagrant"
    steps = [
        "git clone https://github.com/andrewsmedina/tsuru-bootstrap.git",
        "cd tsuru-bootstrap",
        "vagrant up",
    ]
