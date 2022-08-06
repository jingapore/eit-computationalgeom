input_filename = "2_inputTriangulation.txt"
output_filename = "2_outputTriangulation.txt"

if __name__ == "__main__":
    with open("./{}".format(input_filename), "r") as f:
        text = f.readlines()
        line_count = 0
        number_of_points = 0
        number_of_triangles = 0
        for line in text:
            if line_count==0:
                number_of_points = int(line.split()[0])
                number_of_triangles = int(line.split()[1])
            elif line_count > 0 and line_count < number_of_points:
                print("hello")
            line_count += 1
            print("+++")