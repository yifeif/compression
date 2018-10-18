CXX := g++
CFLAGS := -O2 -std=c++11

HEADERS = $(wildcard tensorflow_compression/cc/kernels/*.h)
SRCS = $(filter-out tensorflow_compression/cc/kernels/range_coder_ops_test.cc, $(wildcard tensorflow_compression/cc/kernels/*.cc) \
        $(wildcard tensorflow_compression/cc/ops/*.cc))

TF_CFLAGS := $(shell python -c 'import tensorflow as tf; print(" ".join(tf.sysconfig.get_compile_flags()))')
TF_LFLAGS := $(shell python -c 'import tensorflow as tf; print(" ".join(tf.sysconfig.get_link_flags()))')

CFLAGS = ${TF_CFLAGS} -fPIC -O2 -std=c++11 -D_GLIBCXX_USE_CXX11_ABI=0 
LDFLAGS = -shared ${TF_LFLAGS}

TARGET_LIB = tensorflow_compression/python/ops/_coder_ops.so


.PHONY: all
all: ${TARGET_LIB}

$(TARGET_LIB):  ${HEADERS} $(SRCS)
	$(CXX) $(CFLAGS) -o $@ $^ ${LDFLAGS}

.PHONY: clean
clean:
	rm -f $(TARGET_LIB)