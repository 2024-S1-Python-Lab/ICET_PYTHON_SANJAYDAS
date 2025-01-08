filename1=input("Enter source file name:")
with open(filename1,'r')as file1:
    lines=file1.readlines()
filename2=input("Enter destination file name:")
with open(filename2,'w')as file2:
    for i in range(len(lines)):
        if i%2==0:
            file2.write(lines[i])
print(f'Odd lines copied to {filename2}.')
with open(filename2,'r')as file2:
    lines2=file1.readlines()
    lines2=[line.strip() for line in lines2]
    print("Lines from the file:",lines2)

    
    
