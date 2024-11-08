from setuptools import setup, find_packages
import os

def find_resource_files(source_dir):
    resource_files = []
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(filepath, source_dir)
            resource_files.append((os.path.join('resources', os.path.dirname(relative_path)), [filepath]))
    return resource_files

resource_files = find_resource_files('resources')

setup(
    name='diagrams',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'my_package': [],  # 패키지 내에 데이터 파일을 포함하지 않음
    },
    data_files= resource_files,  # /site-packages에 복사할 파일    
    install_requires=[],
    author='Jung Jin Young',
    author_email='bungker@gmail.com',
    description='Diagrams extend for  Security365',
    url='https://github.com/jyjung/diagrams',
)