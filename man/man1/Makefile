# pod2man.mk -- Makefile portion to convert *.pod files to manual pages
#
#   Copyright information
#
#	Copyright (C) 2010 Jari Aalto
#
#   License
#
#	Redistribution and use in source and binary forms, with or
#	without modification, are permitted provided that the
#	following conditions are met:
#
#	1. Redistributions of source code must retain the above
#	   copyright notice, this list of conditions and the following
#	   disclaimer.
#
#	2. Redistributions in binary form must reproduce the above
#	   copyright notice, this list of conditions and the following
#	   disclaimer in the documentation and/or other materials
#	   provided with the distribution.
#
#	THIS SOFTWARE IS PROVIDED "AS IS" AND ANY EXPRESS OR
#	IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#	PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR(S) OF THIS
#	FILE OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#	INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
#	GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#	INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#	WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#	NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
#	THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
#	DAMAGE.
#
#	The license text is copy of the FreeBSD License available at
#	<http://www.gnu.org/copyleft/gpl.html> with following
#	modifications: wording "THIS SOFTWARE IS PROVIDED BY THE
#	FREEBSD PROJECT" was changed to "THIS SOFTWARE IS PROVIDED 'AS
#	IS'" and wording "IN NO EVENT SHALL THE FREEBSD PROJECT" was
#	changed to "IN NO EVENT SHALL THE AUTHOR(S)"
#
#   Description
#
# 	Convert *.pod files to manual pages.

ifneq (,)
    This makefile requires GNU Make.
endif

# This variable *must* be set when calling
PACKAGE		?= dos2unix

# Optional variables to set
MANSECT		?= 1
PODCENTER	?= $$(date "+%Y-%m-%d")

# Directories
MANSRC		=
MANDEST		= $(MANSRC)

MANPOD		= $(MANSRC)$(PACKAGE).pod
MANPAGE		= $(MANDEST)$(PACKAGE).$(MANSECT)

POD2MAN		= pod2man
POD2MAN_FLAGS	=
MAN_NONLATIN    ?= 1

PODFILES = $(wildcard ../*/man1/dos2unix.pod)
MAN_OBJECTS = dos2unix.1 $(patsubst %.pod,%.1,$(PODFILES))
ifeq ($(MAN_NONLATIN),1)
PODFILES_NONLATIN = $(wildcard ../nonlatin/*/man1/dos2unix.pod)
MAN_OBJECTS_NONLATIN = dos2unix.1 $(patsubst %.pod,%.1,$(PODFILES_NONLATIN))
endif

all: $(MAN_OBJECTS) $(MAN_OBJECTS_NONLATIN)

MAN_OBJECTS_NONLATIN = $(patsubst %.pod,%.1,$(PODFILES_NONLATIN))

# The .pod files for Latin scripts are encoded in Latin-1 (ISO-8859-1/CP1252).
# UTF-8 man pages are not properly displayed in a Windows Command Prompt,
# therefore we keep them in Latin-1 format.

# Cygwin 1.7 expects man pages to be in Latin-1 format.

# The perl version of MinGW and DJGPP is 5.8.8. The pod2man command of perl
# 5.8.8 does not yet have the options -u, --utf8, and does support the =encoding
# command.

# There are different *roff implementations. For now I assume we are using
# groff (GNU-roff) which is wide spread, default on Linux, Cygwin, MinGW, and
# DJGPP.  The groff specific escape sequences may not work with other *roff
# implementations, but they display OK when used in a Windows Command Prompt
# using DJGPP's or MinGW's groff. Although sometimes characters are displayed
# without their diacritics.

# One day everything will be in UTF-8...
# For the English manual it all makes no difference, because the English text
# is plain ASCII.

%.1 : %.pod
	# make target - create manual page from a *.pod page
	podchecker $<
	LC_CTYPE=C $(POD2MAN) $(POD2MAN_FLAGS) \
		--center="$(PODCENTER)" \
		--name="$(PACKAGE)" \
		--section="$(MANSECT)" \
		$< \
	| perl -p -e 's/[Pp]erl v[0-9.]+/$(PACKAGE)/;' \
	  > $@ && \
	rm -f pod*.tmp
# fix for bug http://rt.perl.org/rt3//Public/Bug/Display.html?id=79410
# "Pod2man creates wrong ROFF esc sequences for Latin-1 characters."
# Create groff (specific) escape sequences which work also on DOS/Windows.
# See also: https://rt.cpan.org/Public/Bug/Display.html?id=73804
	perl -pli.bak \
		-e s/A\\\\\\*\'/\\\\[\'A]/g\; \
		-e s/a\\\\\\*\'/\\\\[\'a]/g\; \
		-e s/E\\\\\\*\'/\\\\[\'E]/g\; \
		-e s/e\\\\\\*:/\\\\[:e]/g\; \
		-e s/e\\\\\\*\'/\\\\[\'e]/g\; \
		-e s/i\\\\\\*\'/\\\\[\'i]/g\; \
		-e s/n\\\\\\*~/\\\\[~n]/g\; \
		-e s/O\\\\\\*\'/\\\\[\'O]/g\; \
		-e s/o\\\\\\*\'/\\\\[\'o]/g\; \
		-e s/u\\\\\\*\'/\\\\[\'u]/g\; \
		$@



# The .pod files under the 'nonlatin' folder are encoded in UTF-8.
# For these manuals pod2man needs to support the =encoding command
# and the --utf8 option. This is supported since perl 5.10.1.
# Erwin W.

nonlatin: $(MAN_OBJECTS_NONLATIN)


../nonlatin/ru/%.1 : ../nonlatin/ru/%.pod
	# make target - create manual page from a *.pod page
	podchecker $<
	$(POD2MAN) $(POD2MAN_FLAGS) \
                --utf8 \
		--center="$(PODCENTER)" \
		--name="$(PACKAGE)" \
		--section="$(MANSECT)" \
		$< \
	| perl -p -e 's/[Pp]erl v[0-9.]+/$(PACKAGE)/;' \
	  > $@ && \
	rm -f pod*.tmp

clean:
	rm -f $(MAN_OBJECTS)
	rm -f $(MAN_OBJECTS_NONLATIN)

# End of of Makefile part
