from setuptools import setup, find_packages
from io import open

setup(
	name='dingdong',
	version='0.2',
	description='remind you the status of the program',
	long_description=open('README.md', 'r', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	url='http://github.com/light8lee/dingdong',
	author='Light Lee',
	author_email='light8lee@gmail.com',
	license='MIT',
	packages=find_packages(),
	zip_safe=False,
	python_requires='>=3.5',
	install_requires=[
		'pillow',
		'itchat',
		'paho-mqtt'
	],
	classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ]
)