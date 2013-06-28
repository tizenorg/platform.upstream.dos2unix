Name:           dos2unix
Version:        6.0
Release:        0
License:        BSD-3-Clause
Summary:        Text converters to and from DOS/MAC to UNIX
Url:            http://waterlan.home.xs4all.nl/dos2unix.html
Group:          Productivity/Text/Convertors
Source:         http://waterlan.home.xs4all.nl/dos2unix/dos2unix-%{version}.tar.gz
Source1001: 	dos2unix.manifest
BuildRequires:  gettext-tools
Provides:       unix2dos = %{version}
Obsoletes:      unix2dos < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%make_install docdir=%{_defaultdocdir}/%{name}
%{find_lang} dos2unix --all-name --with-man

%files -f dos2unix.lang
%manifest %{name}.manifest
%defattr(-,root,root,0755)
%doc /usr/share/doc/%{name}-%{version}
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2mac
%{_bindir}/unix2dos
%doc %{_mandir}/*/dos2unix.1*
%doc %{_mandir}/*/mac2unix.1*
%doc %{_mandir}/*/unix2mac.1*
%doc %{_mandir}/*/unix2dos.1*
%doc %lang(nl) %dir %{_mandir}/nl
