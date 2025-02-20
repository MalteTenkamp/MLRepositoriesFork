from setuptools import setup

console_scripts = """
[console_scripts]
sacremoses=sacremoses.cli:cli
"""

setup(
  name = 'sacremoses',
  packages = ['sacremoses'],
  version = '0.0.53',
  description = 'SacreMoses',
  long_description = 'MosesTokenizer in Python',
  author = '',
  package_data={'sacremoses': ['data/perluniprops/*.txt', 'data/nonbreaking_prefixes/nonbreaking_prefix.*']},
  url = 'https://github.com/alvations/sacremoses',
  keywords = [],
  classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  install_requires = ['regex', 'click', 'joblib', 'tqdm'],
  entry_points=console_scripts,
)
