import os
import subprocess



def CompileProject(project_path):
    
    if IsFolderEmpty(project_path):
        print("ERROR: Folder doesnt contain a src, include, or lib folder")
        return
    
    
    #Wether the include folder is empty
    include_path = project_path + "/include"
    lib_path = project_path + "/lib"
    src_path = project_path + "/src"

    

    command = "gcc"
    print("Building compiling command....")
    if FolderContainsFileType(src_path, ".c"):
        command += " src/*.c"
        if FolderContainsFileType(lib_path, ".dll"):
            command += " lib/*.dll"
        
        if FolderContainsFileType(include_path, ".h"):
            command += " -Include/*.h"
        
    else:
        return

    
   
    subprocess.Popen(command, cwd=project_path)
    
    print("Build and compiled!")


def IsFolderEmpty(folder_path):
    return len(os.listdir(folder_path)) == 0

def FolderContainsFile(folder, file_name):
    for file in os.listdir(folder):
        if file == file_name:
            return True 
    return False

def FolderContainsFileType(folder, file_tag) -> bool:
    for file in os.listdir(folder):
        if file.endswith(file_tag):
            return True 

    return False
    
path = input("Enter CProjectPath: " )
os.chdir(path)

 

while True:
    
    i = input()
    
    if i == "build":
        complete = input("Do you want to build and compile? (y/n): ")
        if complete == "y" or complete == "Y":
            CompileProject(path)