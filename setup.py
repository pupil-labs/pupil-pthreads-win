from setuptools import setup
from pathlib import Path

package_dir = "src"
package = "pupil_pthreads_win"

package_data = [
    str(match.resolve())
    for match in (Path() / package_dir / package / "data").rglob('*')
    if match.is_file()
]

setup(
    name="pupil-pthreads-win",
    version='0.dev0',
    # url="https://github.com/pupil-labs/github-2-clickup",
    license="MIT License",
    author="Pupil Labs GmbH",
    author_email="pypi@pupil-labs.com",

    packages=[package],
    package_dir={"": package_dir},
    package_data={package: package_data},
)
