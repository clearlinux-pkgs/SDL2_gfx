#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x231D4B58E1DDB871 (aschiffler@ferzkopp.net)
#
Name     : SDL2_gfx
Version  : 1.0.4
Release  : 18
URL      : http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.tar.gz
Source0  : http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.tar.gz
Source1 : http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.tar.gz.asc
Summary  : drawing and graphical effects extension for SDL
Group    : Development/Tools
License  : Zlib
Requires: SDL2_gfx-lib = %{version}-%{release}
BuildRequires : SDL2-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config

%description
/*!
\mainpage SDL2_gfx - Graphics primitives and surface functions for SDL2
\section contact_sec Contact and License

%package dev
Summary: dev components for the SDL2_gfx package.
Group: Development
Requires: SDL2_gfx-lib = %{version}-%{release}
Provides: SDL2_gfx-devel = %{version}-%{release}
Requires: SDL2_gfx = %{version}-%{release}

%description dev
dev components for the SDL2_gfx package.


%package dev32
Summary: dev32 components for the SDL2_gfx package.
Group: Default
Requires: SDL2_gfx-lib32 = %{version}-%{release}
Requires: SDL2_gfx-dev = %{version}-%{release}

%description dev32
dev32 components for the SDL2_gfx package.


%package lib
Summary: lib components for the SDL2_gfx package.
Group: Libraries

%description lib
lib components for the SDL2_gfx package.


%package lib32
Summary: lib32 components for the SDL2_gfx package.
Group: Default

%description lib32
lib32 components for the SDL2_gfx package.


%prep
%setup -q -n SDL2_gfx-1.0.4
pushd ..
cp -a SDL2_gfx-1.0.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568875891
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568875891
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
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

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_gfx.so
/usr/lib32/pkgconfig/32SDL2_gfx.pc
/usr/lib32/pkgconfig/SDL2_gfx.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2_gfx-1.0.so.0
/usr/lib64/libSDL2_gfx-1.0.so.0.0.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL2_gfx-1.0.so.0
/usr/lib32/libSDL2_gfx-1.0.so.0.0.2
