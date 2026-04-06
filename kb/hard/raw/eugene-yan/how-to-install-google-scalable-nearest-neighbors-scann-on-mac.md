# How to Install Google Scalable Nearest Neighbors (ScaNN) on Mac

**Source:** https://eugeneyan.com//writing/how-to-install-scann-on-mac/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** recsys, ml-systems

---

A few months back, Google shared about Scalable Nearest Neighbors, [ScaNN](https://ai.googleblog.com/2020/07/announcing-scann-efficient-vector.html) ([Paper](https://arxiv.org/abs/1908.10396), [Code](https://github.com/google-research/google-research/tree/master/scann)) for efficient vector similarity search. It seemed to beat the SOTA benchmarks on angular distance (i.e., >2x throughput for a given recall level).

Approximate Nearest Neighbors Benchmarks on the GloVe embeddings (dim=100) ([source](https://ai.googleblog.com/2020/07/announcing-scann-efficient-vector.html))

Recently, I found some time to try it out but was frustrated by how tricky it was to install on a Mac. Here are the steps I took to install it successfully.

## Step-by-step walkthrough

First, we install the necessary compilers.

```
brew install bazel
brew install llvm
brew install gcc
```

Then, we set up our Python version via `pyenv`

```
brew update && brew upgrade pyenv
pyenv --version
> pyenv 1.2.21

pyenv install 3.8.6. # Doesn't work with 3.9 yet
pyenv local 3.8.6
python --version
> Python 3.8.6
```

Now, we create our virtual environment.

```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

`ScaNN` is part of the [google-research repo](https://github.com/google-research/google-research) which is huge. There are more than 200 directories in there and we don’t need all of them. Thus, we’ll do the following to only checkout the ScaNN directory.

```
git clone --depth 1 --filter=blob:none --no-checkout https://github.com/google-research/google-research.git
git checkout master -- scann
cd scann
```

Next, we’ll need to install the Python dependencies.

```
pip install wheel
python configure.py
# There might be complaints about "tensorflow 2.3.1 requires numpy<1.19.0,>=1.16.0, but you'll have numpy 1.19.2 which is incompatible." but it's fine
```

Several issues prevent a direct installation and we’ll be manually fixing them here.

First, we’ll update `.bazelrc` and `.bazel-query.sh`. (It’s not absolutely necessary to update `.bazel-query.sh` but I thought we do it anyway for completeness). We should replace:

```
TF_SHARED_LIBRARY_NAME="ensorflow_framework.2"
```

With:

```
TF_SHARED_LIBRARY_NAME="libtensorflow_framework.2.dylib"
```

Then, we’ll need to update the C++ imports by replacing (there are four of these):

```
#include <hash_set>
```

With:

```
#include <ext/hash_set>
```

Now, we can build it via `bazel`. Instead of using `clang-8` as specified, I just used the latest version of `clang` and it worked fine.

```
CC=/usr/local/opt/llvm/bin/clang CXX=/usr/local/opt/gcc/bin/gcc bazel build -c opt --copt=-mavx2 --copt=-mfma --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0" --cxxopt="-std=c++17" --copt=-fsized-deallocation --copt=-w :build_pip_pkg
```

If it builds successfully, we should see output similar to this.

```
INFO: Elapsed time: 316.366s, Critical Path: 206.32s
INFO: 1066 processes: 319 internal, 747 local.
INFO: Build completed successfully, 1066 total actions
```

Then, we build the Python wheel:

```
./bazel-bin/build_pip_pkg
```

And now we can install it:

```
pip install scann-1.1.1-<replace with your package suffix>
```

You can test if the installation was successful in Python:

```
import scann
scann.scann_ops_pybind.builder()

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: builder() missing 3 required positional arguments: 'db', 'num_neighbors', and 'distance_measure'
```

You should get the error if installation was successful. Here’s a [sample demo on using it](https://github.com/google-research/google-research/blob/master/scann/docs/example.ipynb).

  

If you found this useful, please cite this write-up as:

> Yan, Ziyou. (Oct 2020). How to Install Google Scalable Nearest Neighbors (ScaNN) on Mac. eugeneyan.com.
> https://eugeneyan.com/writing/how-to-install-scann-on-mac/.

or

```
@article{yan2020scann,
  title   = {How to Install Google Scalable Nearest Neighbors (ScaNN) on Mac},
  author  = {Yan, Ziyou},
  journal = {eugeneyan.com},
  year    = {2020},
  month   = {Oct},
  url     = {https://eugeneyan.com/writing/how-to-install-scann-on-mac/}
}
```

  
Share on:
