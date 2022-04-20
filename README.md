# Articulate-pocketsphinx
Repo to create variations of CMU's pocketsphinx.  
This is the xyz version; our first prototype.  

This current branch has logging disable to make pocketsphinx thread-safe.  
This is library is meant to be installed system-wide as it is required by xyz_plus (Go version of pocketsphinx_continuous and pocketsphinx_batch)

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



