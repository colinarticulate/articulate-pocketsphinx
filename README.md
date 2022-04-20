# Articulate-pocketsphinx
Repo to create variations of CMU's pocketsphinx.  
This is the xyz version; our first prototype.  

<<<<<<< HEAD
This current branch has logging disable to make pocketsphinx thread-safe.  
This is library is meant to be installed system-wide as it is required by xyz_plus (Go version of pocketsphinx_continuous and pocketsphinx_batch)

## Requirements  
compiler: gcc  
libraries: -lm -lpthread  
build: autotools  
=======
This branch disables logging which otherwise causes multithreading issues.  

>>>>>>> 777ee73828491a1e90a78440e3e501d6a00a4ac1

## System installation  
Should work the same way as with the original pocketsphinx installation.  
[PocketSphinx 5prealpha] (https://github.com/cmusphinx/pocketsphinx)  
  

```
$ cd articulate-pocketsphinx
$ cd xyzsphinxbase
$ ./autogen.sh
$ make  
$ sudo make install
$ cd ..
$ cd xyzpocketsphinx
$ ./autogen.sh
$ make  
$ sudo make install  
$ cd /usr/local/lib 
$ sudo ldconfig  

```



