from setuptools import find_packages, setup


install_requires = open("requirements.txt").read().strip().split("\n")
dev_requires = open("dev-requirements.txt").read().strip().split("\n")
test_requires = open("test-requirements.txt").read().strip().split("\n")


extras = {
    "dev": dev_requires + test_requires,
    "test": test_requires
}
extras["all_extras"] = sum(extras.values(), [])


setup(
    name="paper-translator",
    version='0.0.1',
    description="paper translator",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="David(Lee Gyu Hyuk)",
    author_email="matda8080@gmail.com",
    url="https://github.com/david-laugh/IA-Paper-Translator.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras,
    setup_requires=['pytest-runner'],
)
