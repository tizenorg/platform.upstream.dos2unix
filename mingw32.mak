
# Author: Erwin Waterlander
# Copyright (C) 2013 Erwin Waterlander
# This file is distributed under the same license as the dos2unix package.

CC = gcc
CRT_GLOB_OBJ = C:/mingw32/i686-w64-mingw32/lib/CRT_glob.o

prefix=c:/usr/local
ENABLE_NLS=

ifdef ENABLE_NLS
LIBS_EXTRA = -lintl -liconv
# Using MinGW gettext,iconv
#ZIPOBJ_EXTRA = bin/libintl-8.dll bin/libiconv-2.dll
endif
LIBS_EXTRA += $(CRT_GLOB_OBJ)

all:
	$(MAKE) all EXE=.exe ENABLE_NLS=$(ENABLE_NLS) LIBS_EXTRA="$(LIBS_EXTRA)" prefix=$(prefix) LINK="cp -f" CC=$(CC) EO_XNOTATION=1 MAN_NONLATIN=

install:
	$(MAKE) install EXE=.exe ENABLE_NLS=$(ENABLE_NLS) LIBS_EXTRA="$(LIBS_EXTRA)" prefix=$(prefix) LINK="cp -f" CC=$(CC) EO_XNOTATION=1 MAN_NONLATIN=

uninstall:
	$(MAKE) uninstall EXE=.exe prefix=$(prefix) MAN_NONLATIN=

clean:
	$(MAKE) clean EXE=.exe ENABLE_NLS=$(ENABLE_NLS) prefix=$(prefix)

mostlyclean:
	$(MAKE) mostlyclean EXE=.exe ENABLE_NLS=$(ENABLE_NLS) prefix=$(prefix)

dist:
	$(MAKE) dist-zip EXE=.exe prefix=$(prefix) VERSIONSUFFIX="-win32" ZIPOBJ_EXTRA="${ZIPOBJ_EXTRA}" ENABLE_NLS=$(ENABLE_NLS)

strip:
	$(MAKE) strip LINK="cp -f" EXE=.exe

