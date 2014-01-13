Name:           dos2unix
Version:        6.0.4
Release:        0
License:        BSD-3-Clause
Summary:        Text converters to and from DOS/MAC to UNIX
Url:            http://waterlan.home.xs4all.nl/dos2unix.html
Group:          System/Utilities
Source:         http://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz
Source1001:     dos2unix.manifest
BuildRequires:  gettext-tools
BuildRequires:  perl
Provides:       unix2dos = %{version}
Obsoletes:      unix2dos < %{version}

%description
Dos2unix is used to convert plain text from DOS (CR/LF) format. Mac2unix
converts plain text from MAC (CR) format to UNIX format (LF).

Unix2dos converts plain text files from UNIX
format to DOS format and unix2dos converts from UNIX to MAC format.

%prep
%setup -q
cp %{SOURCE1001} .
find . -type f | xargs chmod -x

%build
export RPM_OPT_FLAGS
make %{?_smp_mflags} CC="gcc" HTMLEXT="html"

%install
%make_install
%{find_lang} %{name} --all-name --with-man

%files -f %{name}.lang
%manifest %{name}.manifest
%defattr(-,root,root,0755)
%doc /usr/share/doc/%{name}-%{version}
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2mac
%{_bindir}/unix2dos
%{_mandir}/man1/dos2unix.1.gz
%{_mandir}/man1/mac2unix.1.gz
%{_mandir}/man1/unix2dos.1.gz
%{_mandir}/man1/unix2mac.1.gz
