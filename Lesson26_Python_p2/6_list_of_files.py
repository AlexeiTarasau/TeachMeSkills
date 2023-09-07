import os

def find_files_with_substring(file_list, substring):
    matching_files = []
    
    for file_name in file_list:
        if substring in file_name:
            matching_files.append(file_name)
    
    return matching_files

file_list = ["file1.txt", "file2.jpg", "document.docx", "example.txt", "data.csv"]
    
search_substring = "txt"
    
result = find_files_with_substring(file_list, search_substring)
    
if result:
    print("Files whose names contain a substring: ", result)
else:
    print("There are no files whose names contain the specified substring.")
