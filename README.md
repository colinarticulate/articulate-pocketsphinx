# Articulate-pocketsphinx
Repo to create variations of CMU's pocketsphinx.  


## Naming change  

There are scripts provided to change the naming convention of the installed files. This is usefule if we want to have multiple variants of pocketsphinx installed in one system without corrupting each other.  
To change the naming of the final installed files (affecting subfolders and library names in /usr/loca/), follow these instructions:
1. Make sure pocketsphinx and sphinxbase have been just cloned and there have been NOT installed yet.
2. Go to the folder 'naming_scripts'
3. Check the files 'replace_ps.json' and 'replace_bs.json' are set correctly or that you are happy with the default naming convention.
4. Launch a terminal from 'naming_scripts' folder and type:  
```
python change_naming.py
```
5. Now you are ready to install the pocketsphinx library without overriding the original default installation in your system.   
6. Don't ever execute the script again or it will mess your future installations. So, you can delete 'naming_scripts' folder or keep it somewhere else. It will only work in just-cloned original versions of pocketsphinx and sphinxbase.  


## System installation  
Should work the same way as with the original pocketsphinx installation.  
[PocketSphinx 5prealpha] (https://github.com/cmusphinx/pocketsphinx)  
  
```
$ cd sphinxbase
$ ./autogen.sh
$ make  
$ sudo make install
$ cd ..
$ cd pocketsphinx
$ ./autogen.sh
$ make  
$ sudo make install

```

## Local installation  
This is useful for debugging the libraries before release if the original source code is to be modified. Make sure your desired directory contains  

```
usr/local/  
```   


### sphinxbase  

Within the sphinxbase/ directory:
```
$ ./autogen.sh --prefix=</absolute-or-relative-path-to-your-local-directory/usr/local/>
$ make  
$ make install
```


### pocketsphinx  

Within the pocketsphinx/ directory:  

```
$ ./autogen.sh --prefix=</absolute-or-relative-path-to-your-local-directory/usr/local/>
$ make  
$ make install
```  

For more options check
```
$./configure -help  
```
  
You can play with them to pass compiler options or preprocessor options.  
Each package (pocketsphinx or sphinxbase) offers tailor-made options.  

