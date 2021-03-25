# Removing-noise-from-an-image-using-SVD

# Introduction
SVD method can transform matrix A into product U ΣV T, which allows us to refactor a digital image in three matrices. The values in the SVD form of the image are in the range 0-255 (inclusive) where 0 means pure black and 255 means pure white. Many of the techniques of image processing were developed with application to satellite imagery, medical imaging, object recognition, and photo enhancement. Some other application are Polar Decomposition, Effective rank calculation etc.

# Working of SVD
A matrix can be decomposed in various forms for eg., LU decomposition, QR decomposition, Zariski decomposition etc.
A new form of matrix decomposition called Singular Value Decomposition(U ΣV T ) can be defined from LU
decomposition and QR decomposition. SVD is similar to eigenvalue-eigenvector factorization of

QΛQT of positive definite matrix. The Λ is a diagonal matrix containing the eigenvalues. The matrix Q is orthogonal
(QT Q = I) because eigenvectors of a symmetric matrix can be chosen as orthonormal.
Rectangular matrices have no concept of eigenvalues and eigenvectors, but we can modify the equation in a way to
make Q on the left and QT on the right to be any two orthogonal matrices U and V T , not necessarily transposes
of each other. Then, every matrix(even rectangular) can be defined as <img src="https://latex.codecogs.com/svg.image?A&space;=&space;U\Sigma&space;V^T" title="A = U\Sigma V^T" />

The diagonal matrix Σ has eigen values from AT A. The
diagonal elements of Σ will be σ1 , σ2 , ....., σr . They are the singular values of A. First r places in the main diagonal of Σ are filled by these σi values, when rank of A equals r, and the rest of the entries are zero.

Any m by n matrix A can be decomposed as
A = U ΣV T
(orthogonal) = (diagonal)(orthogonal)

The columns of U (m ∗ m) are eigenvectors of AAT , and the columns of V (n ∗ n) are eigenvectors of AT A. The r singular values on the diagonal of Σ (m ∗ n) are the square roots of the non-zero eigenvalues of both AAT and AT A.




