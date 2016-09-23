#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xinit
Version  : 1.3.4
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/app/xinit-1.3.4.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/xinit-1.3.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xinit-bin
Requires: xinit-data
Requires: xinit-doc
BuildRequires : openssl-dev
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
Patch1: starxfce4.patch

%description
The xinit program is used to start the X Window System server and a first
client program on systems that are not using a display manager such as xdm.

%package bin
Summary: bin components for the xinit package.
Group: Binaries
Requires: xinit-data

%description bin
bin components for the xinit package.


%package data
Summary: data components for the xinit package.
Group: Data

%description data
data components for the xinit package.


%package doc
Summary: doc components for the xinit package.
Group: Documentation

%description doc
doc components for the xinit package.


%prep
%setup -q -n xinit-1.3.4
%patch1 -p1

%build
%configure --disable-static --with-xterm=xfce4-terminal \
--with-xinitdir=/usr/share/defaults/xinit
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/startx
/usr/bin/xinit

%files data
%defattr(-,root,root,-)
/usr/share/defaults/xinit/xinitrc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
