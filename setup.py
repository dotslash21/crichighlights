from setuptools import setup

setup(
    name='crichighlights',
    packages=['crichighlights'],
    version='0.1',
    description='A library for fetching live cricket match highlights from cricbuzz',
    author='Arunangshu Biswas',
    author_email='arunangshubsws@gmail.com',
    license='MIT',
    url='https://github.com/dotslash21/crichighlights',
    download_url='https://github.com/codophobia/pycricbuzz/archive/master.zip',
    keywords=['crichighlights', 'cricket', 'highlights', 'cricbuzz'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
