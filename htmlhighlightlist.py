ayray = ["e2523", "e9283"]
with open("C:/Python27/Book1_files/sheet001.htm","r") as f, open("c:/Python27/Book1_files/sheetdump.htm","w+") as u:
    for line in f:
        if any(s in line for s in ayray):
            for x in ayray:
                if x in line:
                    print("Before: " + line)
                    print(x)
                    line = line.replace(x + "</td>", "<mark>" + x + "</mark>" + "</td>")
                    print("After: " + line)
                    u.write(line)
        elif 'Book1.htm' in line:
            line = line.replace('Book1.htm','Book2.htm')
        else:
            u.write(line)

with open("C:/Python27/Book1.htm","r") as f, open("c:/Python27/Book2.htm","w+") as u:
    for line in f:
        if 'Book1.htm' in line:
            line = line.replace('Book1.htm','Book2.htm')
            u.write(line)
        elif 'sheet001' in line:
            line = line.replace('sheet001','sheetdump')
            u.write(line)
        else:
            u.write(line)
        
        
    
