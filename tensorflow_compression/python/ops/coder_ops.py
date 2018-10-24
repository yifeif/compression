# -*- coding: utf-8 -*-
# Copyright 2018 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Range coder operations."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
from tensorflow.python.framework import load_library
from tensorflow.python.platform import resource_loader


# Use framework version of load_op_library instead of contrib version,
# otherwise if tensorflow contains coder_ops, it will always get loaded
# before tensorflow_compression version can be loaded.
coder_ops = load_library.load_op_library(
    resource_loader.get_path_to_datafile("_coder_ops.so"))

# When tf.contrib gets loaded before tensorflow_compression, the coder_ops
# module returned by load_op_library will contain no ops because they have
# already be registered earlier. In this case, use tf.contrib version instead.
try:
  pmf_to_quantized_cdf = coder_ops.pmf_to_quantized_cdf
except AttributeError:
  from tensorflow.contrib.coder.python.ops import coder_ops
  pmf_to_quantized_cdf = coder_ops.pmf_to_quantized_cdf

range_decode = coder_ops.range_decode
range_encode = coder_ops.range_encode
