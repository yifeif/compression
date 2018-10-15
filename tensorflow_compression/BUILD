package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

cc_binary(
    name = 'python/ops/_coder_ops.so',
    srcs = [
        "cc/kernels/range_coder_ops_util.cc",
        "cc/kernels/range_coder_ops_util.h",    
        "cc/kernels/range_coder_ops.cc",
        "cc/kernels/range_coder.cc",
        "cc/kernels/range_coder.h", 
        "cc/kernels/pmf_to_cdf_op.cc",        
        "cc/ops/coder_ops.cc",
    ],
    linkshared = 1,
    deps = [
        "@local_config_tf//:libtensorflow_framework",
        "@local_config_tf//:tf_header_lib",
    ],
    copts = ["-pthread", "-std=c++11", "-D_GLIBCXX_USE_CXX11_ABI=0"]
)

py_library(
    name = "coder_ops_py",
    srcs = [
        "python/ops/coder_ops.py",
    ],
    data = [
        "//tensorflow_compression:python/ops/_coder_ops.so",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "coder_ops_py_test",
    srcs = [
        "python/ops/coder_ops_test.py",
    ],
    deps = [
        ":coder_ops_py",
    ],
    main = "python/ops/coder_ops_test.py",
)

py_library(
    name = "math_ops_py",
    srcs = [
        "python/ops/math_ops.py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "math_ops_py_test",
    srcs = [
        "python/ops/math_ops_test.py",
    ],
    deps = [
        ":math_ops_py",
    ],
    main = "python/ops/math_ops_test.py",
)

py_library(
    name = "padding_ops_py",
    srcs = [
        "python/ops/padding_ops.py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "padding_ops_py_test",
    srcs = [
        "python/ops/padding_ops_test.py",
    ],
    deps = [
        ":padding_ops_py",
    ],
    main = "python/ops/padding_ops_test.py",
)

py_library(
    name = "spectral_ops_py",
    srcs = [
        "python/ops/spectral_ops.py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "spectral_ops_py_test",
    srcs = [
        "python/ops/spectral_ops_test.py",
    ],
    deps = [
        ":spectral_ops_py",
    ],
    main = "python/ops/spectral_ops_test.py",
)

py_library(
    name = "compression_ops_py",
    srcs = [
        "python/ops/__init__.py",
    ],
    deps = [
        ":coder_ops_py",
        ":math_ops_py",
        ":padding_ops_py",
        ":spectral_ops_py",
    ],
    data = [
        "//tensorflow_compression:python/ops/_coder_ops.so",
    ],    
)

py_library(
    name = "entropy_models_py",
    srcs = [
        "python/layers/entropy_models.py",
    ],
    deps = [
        "compression_ops_py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "entropy_models_py_test",
    srcs = [
        "python/layers/entropy_models_test.py",
    ],
    deps = [
        ":entropy_models_py",
    ],
    main = "python/layers/entropy_models_test.py",
)

py_library(
    name = "gdn_py",
    srcs = [
        "python/layers/gdn.py",
    ],
    deps = [
        "compression_ops_py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "gdn_py_test",
    srcs = [
        "python/layers/gdn_test.py",
    ],
    deps = [
        ":gdn_py",
        ":parameterizers_py"
    ],
    main = "python/layers/gdn_test.py",
)

py_library(
    name = "parameterizers_py",
    srcs = [
        "python/layers/parameterizers.py",
    ],
    deps = [
        "compression_ops_py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "parameterizers_py_test",
    srcs = [
        "python/layers/parameterizers_test.py",
    ],
    deps = [
        ":parameterizers_py",
    ],
    main = "python/layers/parameterizers_test.py",
)

py_library(
    name = "signal_conv_py",
    srcs = [
        "python/layers/signal_conv.py",
    ],
    deps = [
        "compression_ops_py",
        ":parameterizers_py",
    ],
    srcs_version = "PY2AND3",
)

py_library(
    name = "initializers_py",
    srcs = [
        "python/layers/initializers.py",
    ],
    srcs_version = "PY2AND3",
)

py_test(
    name = "signal_conv_py_test",
    srcs = [
        "python/layers/signal_conv_test.py",
    ],
    deps = [
        ":signal_conv_py", 
        ":initializers_py",      
    ],
    main = "python/layers/signal_conv_test.py",
)


py_library(
    name = "compression_layers_py",
    srcs = [
        "python/layers/__init__.py",
    ],
    deps = [
        ":entropy_models_py",
        ":gdn_py",
        ":initializers_py",
        ":parameterizers_py",
        ":signal_conv_py",
    ], 
)

py_library(
    name = "tensorflow_compression_py",
    srcs = [
        "__init__.py",
        "python/__init__.py",
    ],
    deps = [
        ":compression_ops_py",
        ":compression_layers_py",
    ],
)