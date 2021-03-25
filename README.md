# Removing-noise-from-an-image-using-SVD

# Introduction
SVD method can transform matrix A into product <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;U\Sigma&space;V^T" title="U\Sigma V^T" />, which allows us to refactor a digital image in three matrices. The values in the SVD form of the image are in the range 0-255 (inclusive) where 0 means pure black and 255 means pure white. Many of the techniques of image processing were developed with application to satellite imagery, medical imaging, object recognition, and photo enhancement. Some other application are Polar Decomposition, Effective rank calculation etc.

# Working of SVD
A matrix can be decomposed in various forms for eg., <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;LU" title="LU" /> decomposition, QR decomposition, Zariski decomposition etc.
A new form of matrix decomposition called Singular Value Decomposition(<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;U\Sigma&space;V^T" title="U\Sigma V^T" />) can be defined from <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;LU" title="LU" />
decomposition and QR decomposition. SVD is similar to eigenvalue-eigenvector factorization of

<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;Q^TQ" title="Q^TQ" /> of positive definite matrix. The Λ is a diagonal matrix containing the eigenvalues. The matrix Q is orthogonal
(<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;Q^TQ&space;=&space;I" title="Q^TQ = I" />) because eigenvectors of a symmetric matrix can be chosen as orthonormal.
Rectangular matrices have no concept of eigenvalues and eigenvectors, but we can modify the equation in a way to
make Q on the left and <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;Q^T" title="Q^T" /> on the right to be any two orthogonal matrices U and <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;V^T" title="V^T" /> , not necessarily transposes
of each other. Then, every matrix(even rectangular) can be defined as <img src="https://latex.codecogs.com/svg.image?A&space;=&space;U\Sigma&space;V^T" title="A = U\Sigma V^T" />

The diagonal matrix Σ has eigen values from <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;A^TA" title="A^TA" />. The
diagonal elements of Σ will be σ1 , σ2 , ....., σr . They are the singular values of A. First r places in the main diagonal of Σ are filled by these σi values, when rank of A equals r, and the rest of the entries are zero.

Any m by n matrix A can be decomposed as
<img src="https://latex.codecogs.com/png.image?\dpi{110}&space;A&space;=&space;U\Sigma&space;V^T" title="A = U\Sigma V^T" />
(orthogonal) = (diagonal)(orthogonal)

The columns of <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;U&space;(m&space;\times&space;n)" title="U (m \times n)" /> are eigenvectors of <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;AA^T" title="AA^T" /> , and the columns of <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;V(n&space;\times&space;n)" title="V(n \times n)" /> are eigenvectors of <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;A^TA" title="A^TA" />. The r singular values on the diagonal of <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;\Sigma&space;(m&space;\times&space;n)" title="\Sigma (m \times n)" /> are the square roots of the non-zero eigenvalues of both <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;AA^T" title="AA^T" /> and <img src="https://latex.codecogs.com/png.image?\dpi{110}&space;A^TA" title="A^TA" />.




