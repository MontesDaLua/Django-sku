from distutils.core import setup 
import os
import setuplib 
#packages, package_data = setuplib.find_packages('sku')

setup(name="sku", 
version="0.2", 
description="packaged Python sku", 
author="Miguel Rodrigues", 
author_email="miguel___rodrigues@hotmail.com", 
url="Your website URL here", 
license='BSD License',
platforms=['OS Independent'],
py_modules=["sku"], 
download_url="URL to download this package here",
classifiers=[ "'Development Status :: 0 - Pre-alpha', 'Environment :: Web Environment', 'Framework :: Django', 'Intended Audience :: Developers', 'License :: OSI Approved :: BSD License ', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Topic :: Internet :: WWW/HTTP :: Dynamic Content', 'Topic :: Software Development', 'Topic :: Software Development :: Libraries :: Application Frameworks',"],
)
