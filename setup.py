from setuptools import setup, find_packages

setup(
    name='a2c-ppo-acktr',
    packages=find_packages(),
    version='0.0.1',
    scripts=['run_a2c_ppo_acktr.py'],
    install_requires=['gym', 'matplotlib', 'pybullet'])
