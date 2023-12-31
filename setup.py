from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in weapon_management/__init__.py
from weapon_management import __version__ as version

setup(
	name="weapon_management",
	version=version,
	description="Project ",
	author="Expedien",
	author_email="agaur@expediens.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
