!!!
Please read carefully
!!!

This script only needs to be used once and, only on a clean-just-cloned pair of repos (pocketsphinx and sphinxbase).
If something doesn't work, you need to re-clone the repos (or equivalently copy-paste from wherever you are holding it just cloned)
and use this script to do the changes again.

Once the naming change is done and the libraries are installed correctly, you can forget about this script. In fact,
don't use it any more or you could harm future installations.

You can get tracked of what this script changes by reading the files:
'replace_ps.json'
'replace_bs.json'

The files 'Makefile_am_adtools.txt' and 'Makefile_am_lmtools.txt' don't affect the original installation, they just provide a change of
shadow variables so we can proceed to change the name of key executable files so they don't override the executables of the original installation.
