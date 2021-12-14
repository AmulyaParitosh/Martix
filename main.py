from Matrix import Matrix

if __name__ == "__main__":
    mat1 = Matrix.fromfile("input_file.txt", which=0)
    mat2 = Matrix.fromfile("input_file.txt", which=1)

    # print(mat1)
    # mat2.add_column([1, 1, 1], 0)
    # print(mat2)
    # mat1.add_column(mat2.matrix, 0)
    # print(mat1)
    Matrix.soe(mat1, mat2)
    # mat3 = Matrix.oforder(3, 3, 1)
    # print(mat1.rank())
