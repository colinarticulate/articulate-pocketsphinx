import os

cwd=os.getcwd()

def get_include_files(filename):
    files=[]
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            files.append(line.strip('\n'))    

    return files

def replace_in_file(filename, previous_name, new_name):
    with open(filename,'r') as f:
        contents = f.read()
        #print(contents)
        parts = contents.split(previous_name)
        #print(parts)
        new_contents = f"{new_name}".join(parts)
        #print(new_contents)
    with open(filename, 'w') as f:
        f.write(new_contents)

ps_files = get_include_files("include_pocketsphinx.txt")
sb_files = get_include_files("include_sphinxbase.txt")

#print(ps_files)
#print(sb_files)

for file in ps_files[:1]:
    file_path = os.path.join(cwd, "..", "xyzpocketsphinx", file) #,"..","xyzpocketsphinx",file)
    print(file_path)
    replace_in_file(file_path, "#include <sphinxbase/", "#include <xyzsphinxbase/")