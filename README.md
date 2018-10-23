
To build tensorflow_compression pip package, first clone this branch

```bash
git clone -b test https://github.com/yifeif/compression.git
cd compression
```

Then run the following in Docker container

```bash
docker pull yifeif/tensorflow:custom_op
mkdir artifacts
docker run --rm --pid=host -v ${PWD}:/working_dir -w /working_dir  yifeif/tensorflow:custom_op ./build_and_test_wheel.sh
```
Install pip package with:
```bash
pip install artifacts/*.whl
```
