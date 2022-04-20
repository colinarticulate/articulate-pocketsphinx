# Articulate-pocketsphinx
Repo to create variations of CMU's pocketsphinx.  
This is the xyz version; our first prototype.  
  

This branch sets FSG_PNODE_CTXT_BVSZ to 2 (default is 4) in fsg_lextree.h line 64 (src/libpocketsphinx).  
The aim is to limit our number of phones to 64 or less to make search blazing fast.  
Also, here logging is not disabled.  


## Requirements  
compiler: gcc  
libraries: -lm -lpthread  
build: autotools  

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



