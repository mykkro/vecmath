from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    long_description=readme(),
    name="vecmath",
	version="0.1",
	description="Simple vecmath library",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"License :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Topic :: Miscellaneous :: Utility"
	],
	keywords="python tools",
	url="http://dev/null",
	author="mykkro",
	author_email="myrousz@gmail.com",
	license="MIT",
	packages=[
		"vecmath"
	],
	install_requires=[
	],
	entry_points={
	},
    include_package_data=True,
	zip_safe=False
)
