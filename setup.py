import subprocess

from setuptools import Command, setup


class LintCommand(Command):
    """A custom command to run linters."""

    description = "run linters"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.call(["black", "."])
        subprocess.call(["isort", "."])
        subprocess.call(["pydocstyle", "."])
        subprocess.call(["pylint", "--ignore=migrations ", "."])


setup(
    name="shop",
    version="0.1",
    packages=["shop"],
    cmdclass={
        "lint": LintCommand,
    },
)
