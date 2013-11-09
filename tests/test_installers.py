from unittest import TestCase

from installer.installers import Vagrant


class VagratTest(TestCase):
    def test_steps(self):
        expected = [
            "git clone https://github.com/andrewsmedina/tsuru-bootstrap.git",
            "cd tsuru-bootstrap",
            "vagrant up",
        ]
        self.assertEqual(Vagrant.steps, expected)
