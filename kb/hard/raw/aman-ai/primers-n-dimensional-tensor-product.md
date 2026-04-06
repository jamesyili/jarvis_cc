# Primers • N-Dimensional Tensor Product

**Source:** https://aman.ai/primers/ai/matmul/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Overview](#overview)
* [General Procedure](#general-procedure)
* [Implementation](#implementation)
* [References](#references)
* [Citation](#citation)

## Overview

* In this article, let’s go over the rules and procedure for an \(n\)-dimensional tensor product, i.e., say \(A[a,b,c] \times B[i,j,k]\).

## General Procedure

* The general procedure is called [tensor contraction](http://en.wikipedia.org/wiki/Tensor_contraction). Concretely it’s given by summing over various indices. For example, just as ordinary matrix multiplication \(C=A \times B\) is given by,

\[c\_{i j}=\sum\_{k} a\_{i k} b\_{k j}\]

* We can contract by summing across any index. For example,

  \[c\_{i j l m}=\sum\_{k} a\_{i j k} b\_{k l m}\]
  + which gives a 4-tensor (“4-dimensional matrix”) rather than a 3-tensor.
* We can also contract twice, for example

  \[c\_{i l}=\sum\_{j, k} a\_{i j k} b\_{k j l}\]
  + which gives a 2-tensor.

## Implementation

* First, let’s look how matrix multiplication works. Say you have \(A[m,n]\) and \(B[n,p]\). **A requirement for the multiplication to be valid is that the number of columns of \(A\) must match the number of rows of \(B\).** Then, all you do is iterate over rows of \(A\) `(i)` and columns of \(B\) `(j)` and the common dimension of both `(k)` (matlab/octave example):

```
m = 2
n = 3
p = 4
A = randn(m,n)
B = randn(n,p)
C = zeros(m,p)

for i = 1:m
    for j = 1:p
        for k = 1:n
             C(i,j) = C(i,j) + A(i,k)*B(k,j)
        end
    end
end

C-A*B %to check the code, should output zeros
```

* Note that the common dimension \(n\) got **“contracted”** in the process.
* Now, assuming you want something similar to happen in 3D case, i.e., one common dimension to contract, what would you do? Assume you have \(A[l,m,n]\) and \(B[n,p,q]\). **The requirement of the common dimension is still there - the last one of A must equal the first one of B**. Then, \(n\) just cancels in \(L \times M \times N \times N \times P \times Q\) and what you get is \(L \times M \times P \times Q\), which is 4-dimensional. To compute it, just append two more for loops to iterate over new dimensions:

```
l = 5
m = 2
n = 3
p = 4
q = 6
A = randn(l,m,n)
B = randn(n,p,q)
C = zeros(l,m,p,q)

for h = 1:l
    for i = 1:m
        for j = 1:p
            for g = 1:q
                for k = 1:n
                    C(h,i,j,g) = C(h,i,j,g) + A(h,i,k)*B(k,j,g)
                end
            end
        end
    end
end
```

* At the heart of it, it is still row-by-column kind of operation (hence only one dimension “contracts”), just over more data.
* Now, let’s tackle the multiplication of \(A[m,n]\) and \(B[n,p,q]\), where the tensors have different ranks (i.e., number of dimensions), i.e, \(2D \times 3D\), but it seems doable nonetheless (after all, matrix times vector is \(2D \times 1D\)). The result is \(C[m,p,q]\), as follows:

```
m = 2
n = 3
p = 4
q = 5
A = randn(m,n)
B = randn(n,p,q)
C = zeros(m,p,q)

Ct=C
for i = 1:m
    for j = 1:p
        for g = 1:q
            for k = 1:n
                C(i,j,g) = C(i,j,g) + A(i,k)*B(k,j,g)
            end
        end
    end
end
```

* which checks out against using the full for-loops:

```
for j = 1:p
    for g = 1:q
        Ct(:,j,g) = A*B(:,j,g); %"true", but still uses for-loops
    end
end
C-Ct
```

## References

* [Is there a 3-dimensional “matrix” by “matrix” product?](https://math.stackexchange.com/questions/63074/is-there-a-3-dimensional-matrix-by-matrix-product)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020DistilledN-DimTensorProduct,
  title   = {N-Dimensional Tensor Product},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
