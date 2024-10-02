[app]

# (str) Title of your application
title = JustTranslate

# (str) Package name
package.name = justTranslate

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = src

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,onnx,exe

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3, sentencepiece, namex, mpmath, libclang, flatbuffers, wrapt, wheel, urllib3, typing-extensions, tqdm, termcolor, tensorboard-data-server, sympy, six, setuptools, safetensors, regex, pyyaml, pygments, protobuf, packaging, opt-einsum, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, networkx, mdurl, MarkupSafe, markdown, idna, grpcio, gast, fsspec, filelock, charset-normalizer, certifi, absl-py, werkzeug, triton, requests, optree, nvidia-cusparse-cu12, nvidia-cudnn-cu12, ml-dtypes, markdown-it-py, jinja2, h5py, google-pasta, astunparse, tensorboard, rich, nvidia-cusolver-cu12, huggingface-hub, torch, tokenizers, keras, transformers, tensorflow,  simpleaudio, kivy

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 31

# (int) Minimum API that you want to support
android.minapi = 30

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable Android auto backup feature (Android API >=23)
android.allow_backup = True

# (list) Add additional JARs for Android (for missing Java dependencies)
android.add_jars = /usr/share/java/jaxb-api.jar, /usr/share/java/jaxb-impl.jar

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
