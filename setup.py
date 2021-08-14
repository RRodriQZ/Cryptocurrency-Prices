from setuptools import setup


dependencies = [
    "requests==2.25.1",
    "marshmallow==3.13.0",
]

package_data = {}

packages = [
    "controller",
    "crypto",
    "functions",
    "log",
    "model",
    "schemas",
    "view",
]

platform = ["any"]

long_description = (
    "Program that allows you to obtain exchange rates at the moment of different markets: "
    "1) ArgenBTC 2) Bitex 3) Bitso 4) Buda 5) Buenbit 6) Copter 7) CriptoFacil 8) Ripio"
)

manifest = dict(
    name="cryptocurrency-prices",
    version="1.0.0",
    author="DobleRR - Rodrigo Quispe",
    author_email="rrquispezabala@gmail.com",
    description="Program that allows you to obtain exchange rates at the moment of different markets",
    url="https://github.com/RRodriQZ",
    license="MIT",
    python_requires=">=3.6, <4",
    keywords="exchange markets cryptocurrency prices",
    install_requires=dependencies,
    package_data=package_data,
    packages=packages,
    platforms=platform,
    long_description=long_description,
    long_description_content_type="text/markdown",
)


if __name__ == "__main__":
    setup(**manifest)
