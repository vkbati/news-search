from setuptools import setup, find_packages

setup(
    name='news-search',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'transformers',
        'torch',
        'newsapi-python',
        'spacy',
        'spacy-model-en_core_web_sm',
        'spacy-model-de_core_news_sm',
    ],
    entry_points={
        'console_scripts': [
            'news-search = news_search.search:main'
        ]
    },
    author='Veysel Kaan Bati',
    description='A Python library for searching and summarizing news articles headlines',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vkbati/news-search',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.9',
    ],
)
