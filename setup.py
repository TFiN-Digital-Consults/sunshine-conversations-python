# coding: utf-8

"""
    Sunshine Conversations API

    The version of the OpenAPI document: 9.15.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "sunshine-conversations-client"
VERSION = "9.15.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
setup(
    name=NAME,
    version=VERSION,
    description="Sunshine Conversations API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["Sunshine Conversations API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
        The Python package for the Sunshine Conversations API\n
        This SDK is automatically generated by the [OpenAPI Generator Codegen](https://github.com/OpenAPITools/openapi-generator) project using the [Sunshine Conversations API spec](https://github.com/zendesk/sunshine-conversations-api-spec).
    """
)
