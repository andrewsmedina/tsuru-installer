from unittest import TestCase

from installer import Component


class ComponentTest(TestCase):
    def test_should_have_name(self):
        self.assertTrue(hasattr(Component, "name"))

    def test_should_have_steps(self):
        self.assertTrue(hasattr(Component, "steps"))
