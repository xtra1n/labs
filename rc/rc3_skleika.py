def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        num1 = f1.readline().strip()
        num2 = f2.readline().strip()

        while num1 or num2:
            if num1 and (not num2 or int(num1) >= int(num2)):
                out.write(num1 + '\n')
                num1 = f1.readline().strip()
            elif num2:
                out.write(num2 + '\n')
                num2 = f2.readline().strip()

# Call the function with file names
merge_files('in1.txt', 'in2.txt', 'out.txt')