with open ('data/inputData.txt') as input_data:

    counter = 1
    print("1. Now printing line by line:")
    for line in input_data:
        print("line:", counter, line)
        counter += 1


    # print("2. Reading the whole content and assigning to a variable")
    # contents = input_data.read()
    # print(contents)

filename = 'data/inputData.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love programming.")
