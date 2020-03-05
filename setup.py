from setuptools import setup, find_packages
from io import open

setup(
	name='dinglingling',
	version='0.1.0',
	description='remind you the status of the program',
	long_description=open('readme.md', 'r', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	url='https://github.com/PeijiYang/dinglingling',
	author='Peiji',
	author_email='peiji.yang@foxmail.com',
	license='MIT',
	packages=find_packages(),
	zip_safe=False,
	python_requires='>=3.6',
	install_requires=[],
	classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)