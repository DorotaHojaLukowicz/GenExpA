import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='GenExpA',
    version='0.0.5',
    author='Dawid Maciazek',
    description="Comprehensive tool based on the new workflow for qPCR data analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'PySide2>=5.15.2',
        'numpy>=1.19.5',
        'cycler>=0.10.0',
        'et-xmlfile>=1.1.0',
        'kiwisolver>=1.3.1',
        'matplotlib>=3.3.4',
        'openpyxl>=3.0.7',
        'pandas>=1.1.5',
        'patsy>=0.5.1',
        'Pillow>=8.2.0',
        'pyparsing>=2.4.7',
        'python-dateutil>=2.8.1',
        'pytz>=2021.1',
        'scipy>=1.5.4',
        'scikit-posthocs>=0.6.7',
        'seaborn>=0.11.1',
        'shiboken2>=5.15.2',
        'six>=1.16.0',
        'statsmodels>=0.12.2',
        'xlrd>=1.2.0'],
    entry_points = {
        "console_scripts": [
            "genexp = genexpa.main:main"
        ]
    },
    python_requires=">=3.6",

)
