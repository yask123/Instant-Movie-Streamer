
from setuptools import setup

setup(name="ims",
	  version="2.4",
	  description="Instantly stream movies/ tv episodes",
	  url="http://iyask.me",
	  author="Yask Srivastava",
	  author_email="yask123@gmail.com",
	  license='MIT',
	  packages=["ims"],
	  scripts=["bin/ims"],
	  nstall_requires=[
		  'BeautifulSoup4',
		  'requests'],
	  zip_safe=False)
