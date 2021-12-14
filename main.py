from Matrix import Matrix

if __name__ == "__main__":
    mat1 = Matrix.fromfile("input_file.txt", which=1)
    mat2 = Matrix.oforder(2, 2, 2)
    mat3 = Matrix([[1., 2.], [2., 1.]])
    print(mat1**2)
    print(~mat3)
    print(mat2)
    print(mat1)
