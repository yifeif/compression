#!/bin/bash
./configure.sh
bazel build :new_pip_pkg
bazel-bin/new_pip_pkg /tmp/pip_pkg
pip install /tmp/pip_pkg/*.whl
cp /tmp/pip_pkg/*.whl /working_dir/artifacts/.
