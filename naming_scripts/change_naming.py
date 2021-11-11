'''
    Script to automatically change key parts of the installation scripts to be able to change the name of the project and the corresponding libraries.
    This way we can install and evaluate new version of pocketsphinx in the system without overriding the original installation.
    Directory names and file names are not modified.

    Requires two json files with the required modifications:
        'replace_ps.json' and 'replace_bs.json'. There are the files 'replace_ps_master.json' and 'replace_bs_master.json' where no changes are made to
                                                 the key strings to change the name of the project. They can be used to change to a different name.
                                                 We are currently using the changes: pocketsphinx -> xyzpocketsphinx and sphinxbase -> xyzsphinxbase


    and the scripts:
        'Makefile_adtools.am' and 'Makefile_lmtools.am'


    Ex: 
        pocketsphinx -> xyzpocketsphnx (in the system installation)
        -lsphinxbase -> -lxyzsphinxbase 
        libpocketsphinx.so -> libxyzpocketsphinx.so
'''


import os
import shutil
import json



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


def replace_name_in_project(project, jsondata):
    
    files = list(jsondata.keys())
    cwd=os.getcwd()
    for file in files:
        filename = os.path.join(cwd, project, file)
        print("\n", filename )
        previous_names = jsondata[file]['previous']
        for previous_name in previous_names:
            
            if "pocketsphinx" in previous_name:
                parts = previous_name.split("pocketsphinx")
                #print(parts)
                new_name = "xyzpocketsphinx".join(parts)
            elif "sphinx" in previous_name:
                parts = previous_name.split("sphinx")
                new_name = "xyzsphinx".join(parts)
                
            elif "PocketSphinx" in previous_name:
                parts = previous_name.split("PocketSphinx")
                #print(parts)
                new_name = "xyzPocketSphinx".join(parts)
            elif "SphinxBase" in previous_name:
                parts = previous_name.split("SphinxBase")
                new_name = "xyzSphinxBase".join(parts)
            else:
                print(f"Error in: {filename} replacing {previous_name}.")
                
            print(f"   {previous_name} ----> {new_name}")
            replace_in_file(filename, previous_name, new_name)


def replace_make_am_files():
    '''
        No option but to replace the Makefile.am scripts for 'adtools' and 'lmtools'.
        Programs with the same make configuration don't require individual shadow variables they can use a general one. Any name change in an executable can be done
        without altering the name of source files but for that to happen each executalbe has to have a different shadow variable with its
        name changed accordingly. Therefore, the whole Makefile.am script has to be re-coded as each script makes two different programs with the same rules.

        An example can be found in 'pocketsphinx/src/programs/Makefile.am' where 'pocketsphinx_continuous' is made using the source file 'continuous.c' (and similarly
        for the other two programs in there)

    '''


    cwd=os.getcwd()
    adtools_filename = os.path.join(cwd, "../sphinxbase/src/sphinx_adtools/Makefile.am")
    lmtools_filename = os.path.join(cwd, "../sphinxbase/src/sphinx_lmtools/Makefile.am")

    #adtools:
    with open("Makefile_adtools.am",'r') as f:
        contents=f.read()
    with open(adtools_filename, 'w') as f:
        f.write(contents)

    #lmtools:
    with open("Makefile_lmtools.am",'r') as f:
        contents=f.read()
    with open(lmtools_filename, 'w') as f:
        f.write(contents)


def rename_key_files_and_folders():
    #pocketsphinx
    os.rename(os.path.join("../","pocketsphinx","pocketsphinx.pc.in"), os.path.join("../", "pocketsphinx", "xyzpocketsphinx.pc.in"))
    os.rename(os.path.join("../","pocketsphinx"), os.path.join("../", "xyzpocketsphinx"))
    #sphinxbase
    os.rename(os.path.join("../","sphinxbase","sphinxbase.pc.in"), os.path.join("../", "sphinxbase", "xyzsphinxbase.pc.in"))
    os.rename(os.path.join("../","sphinxbase"), os.path.join("../", "xyzsphinxbase"))


def add_src_code_modifications(path):
    
    list_of_files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            list_of_files[filename] = os.sep.join([dirpath, filename])
            
    print("Adding changes in source code ...")
    for file in list(list_of_files.keys()):
        src = list_of_files[file]
        dst = os.path.join("../",*list_of_files[file].split("/")[1:])

        shutil.copy(src, dst)
        print(f"replacing: {src} ---> {dst}")
        
    print("Source code changes finished.")


def change_pattern(pattern, previous_name, new_name):
    return new_name.join(pattern.split(previous_name))


def replace_sphinxbase_system_header(path, pattern, new_pattern):
    print(f"Replacing {pattern} for {new_pattern}")
    files = {}
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            #print(filename)
            #print(dirpath[len(path):])
            #files[filename] = os.sep.join([dirpath[len(path):], filename])
            #files[filename] = os.sep.join([dirpath, filename])
            path_file = os.sep.join([dirpath, filename])
            filename_bare, ext = os.path.splitext(path_file)
            if ext==".c" or ext==".h":
                #print(filename)
                with open(path_file, 'r') as f:
                    contents = f.read()
                    #print(contents)
                    parts = contents.split(pattern)
                    if len(parts) > 1:
                        files[filename] = os.sep.join([dirpath[len(path):], filename])
                        print(f"       {files[filename]}")
                        new_contents = new_pattern.join(parts)
                        with open(path_file, 'w') as f:
                            f.write(new_contents)
                        
                
    return files


def change_sphinxbase_system_headers():
    pattern = "#include <sphinxbase/"
    previous_name = "sphinxbase"
    new_name = "xyzsphinxbase"
    new_pattern = change_pattern(pattern, previous_name, new_name)
    path_original_ps = "../pocketsphinx"
    path_original_sb = "../sphinxbase"
    ps_modified_files = replace_sphinxbase_system_header(path_original_ps, pattern, new_pattern)
    sb_modified_files = replace_sphinxbase_system_header(path_original_sb, pattern, new_pattern)



def main():

    file_ps="replace_ps.json"
    file_sb="replace_sb.json"
    with open(file_ps, 'r') as f:
        contents = f.read()
        jps=json.loads(contents)
    with open(file_sb, 'r') as f:
        contents = f.read()
        jsb=json.loads(contents)


    #Order matters in here:
    #Change source code:
    add_src_code_modifications( "new_version" )

    #Change sphinxbase system headers in source code:
    change_sphinxbase_system_headers()


    #For pocketsphinx:
    replace_name_in_project("../pocketsphinx",jps[1])

    #For sphinxbase:
    replace_make_am_files()
    replace_name_in_project("../sphinxbase",jsb[1])


    #Rename folders and files:
    rename_key_files_and_folders()



if __name__ == "__main__":

    main()



