# Articulate-pocketsphinx
Repo to create variations of CMU's pocketsphinx.  
## This is the first prototype. Variant code named 'xyz'.      

This version uses posix-compliant file mappping in memory so, it will not work on Windows.  



## System installation  
Should work the same way as with the original pocketsphinx installation.  
[PocketSphinx 5prealpha] (https://github.com/cmusphinx/pocketsphinx)  
  
```
$cd articulate-pocketsphinx
$ cd xyzsphinxbase
$ ./autogen.sh
$ make  
$ sudo make install
$ cd ..
$ cd xyzpocketsphinx
$ ./autogen.sh
$ make  
$ sudo make install

```

