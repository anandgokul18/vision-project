from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['vision_package'],
    package_dir={'': 'src'},
    install_requires=[
        'email-keyword-matcher',
    ]
)

setup(**setup_args)
