my_plugins = 
my_headers =
my_files =
if BUILD_GST
my_plugins += libgstxyzpocketsphinx.la
endif

plugin_LTLIBRARIES = $(my_plugins)

libgstxyzpocketsphinx_la_SOURCES = gstpocketsphinx.c

libgstxyzpocketsphinx_la_LIBADD = \
	$(GST_LIBS) \
	-lgstaudio-$(GST_MAJORMINOR) \
	$(top_builddir)/src/libpocketsphinx/libxyzpocketsphinx.la \
	-lxyzsphinxbase

libgstxyzpocketsphinx_la_LDFLAGS = $(GST_PLUGIN_LDFLAGS)

noinst_HEADERS = gstpocketsphinx.h

AM_CFLAGS = \
	-I$(top_srcdir)/include \
	-I$(top_builddir)/include \
	$(GST_CFLAGS) \
	-DMODELDIR=\"$(pkgdatadir)/model\"

EXTRA_DIST = livedemo.py livedemo.c

