def read_sample_txt_with():
    """
    Reads data from sample1.txt. This method utilizes the with block to
    do so. A with block allows us to safely conduct file operations. If
    there is any exception, the file is closed automatically. It also
    demonstrates how to reset the file pointer if we want to read
    multiple times.
    """
    print("\nReading the sample.txt file using a with block")
    print("----------------------------------------------")
    with open("sample.txt", mode='r') as my_text_file:
        data = my_text_file.read()
        print(f"File Data:\n{data}")
        data = my_text_file.read()
        print(f"Printing Data again: {data}")
        my_text_file.seek(0)
        data = my_text_file.read()
        print(f"Printing data after seeking to the beginning:\n {data}")


def main():
    pass


if __name__ == '__main__':
    main()
