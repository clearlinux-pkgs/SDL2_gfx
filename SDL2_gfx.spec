#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x231D4B58E1DDB871 (aschiffler@ferzkopp.net)
#
Name     : SDL2_gfx
Version  : 1.0.4
Release  : 14
URL      : http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.tar.gz
Source0  : http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.tar.gz
Source99 : http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.tar.gz.asc
Summary  : drawing and graphical effects extension for SDL
Group    : Development/Tools
License  : Zlib
Requires: SDL2_gfx-lib = %{version}-%{release}
BuildRequires : SDL2-dev

%description
/*!
\mainpage SDL2_gfx - Graphics primitives and surface functions for SDL2
\section contact_sec Contact and License

%package dev
Summary: dev components for the SDL2_gfx package.
Group: Development
Requires: SDL2_gfx-lib = %{version}-%{release}
Provides: SDL2_gfx-devel = %{version}-%{release}

%description dev
dev components for the SDL2_gfx package.


%package lib
Summary: lib components for the SDL2_gfx package.
Group: Libraries

%description lib
lib components for the SDL2_gfx package.


%prep
%setup -q -n SDL2_gfx-1.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542067917
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542067917
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL2_framerate.h
/usr/include/SDL2/SDL2_gfxPrimitives.h
/usr/include/SDL2/SDL2_imageFilter.h
/usr/include/SDL2/SDL2_rotozoom.h
/usr/lib64/libSDL2_gfx.so
/usr/lib64/pkgconfig/SDL2_gfx.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_gfx-1.0.so.0
/usr/lib64/libSDL2_gfx-1.0.so.0.0.2
