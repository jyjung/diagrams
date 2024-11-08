from setuptools import setup, find_packages

setup(
    name='diagrams-security365',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,  # 추가
    package_data={
        '': ['resources/*'],  # 프로젝트의 리소스를 포함
    },    
    install_requires=[],
    author='Jung Jin Young',
    author_email='bungker@gmail.com',
    description='Diagrams extend for  Security365',
    url='https://github.com/jyjung/diagrams',
)