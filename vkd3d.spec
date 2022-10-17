#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCEFAC8EAAF17519D (julliard@winehq.org)
#
Name     : vkd3d
Version  : 1.5
Release  : 7
URL      : https://dl.winehq.org/vkd3d/source/vkd3d-1.5.tar.xz
Source0  : https://dl.winehq.org/vkd3d/source/vkd3d-1.5.tar.xz
Source1  : https://dl.winehq.org/vkd3d/source/vkd3d-1.5.tar.xz.sign
Summary  : The vkd3d 3D Graphics Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: vkd3d-bin = %{version}-%{release}
Requires: vkd3d-lib = %{version}-%{release}
Requires: vkd3d-license = %{version}-%{release}
BuildRequires : SPIRV-Tools
BuildRequires : SPIRV-Tools-dev
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Loader-dev32
BuildRequires : bison
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : llvm-dev
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(32SPIRV-Tools-shared)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xcb-event)
BuildRequires : pkgconfig(32xcb-icccm)
BuildRequires : pkgconfig(32xcb-keysyms)
BuildRequires : pkgconfig(SPIRV-Tools-shared)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-event)
BuildRequires : pkgconfig(xcb-icccm)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : sed
BuildRequires : wine-bin

%description
=============================
The vkd3d 3D Graphics Library
=============================

%package bin
Summary: bin components for the vkd3d package.
Group: Binaries
Requires: vkd3d-license = %{version}-%{release}

%description bin
bin components for the vkd3d package.


%package dev
Summary: dev components for the vkd3d package.
Group: Development
Requires: vkd3d-lib = %{version}-%{release}
Requires: vkd3d-bin = %{version}-%{release}
Provides: vkd3d-devel = %{version}-%{release}
Requires: vkd3d = %{version}-%{release}

%description dev
dev components for the vkd3d package.


%package dev32
Summary: dev32 components for the vkd3d package.
Group: Default
Requires: vkd3d-lib32 = %{version}-%{release}
Requires: vkd3d-bin = %{version}-%{release}
Requires: vkd3d-dev = %{version}-%{release}

%description dev32
dev32 components for the vkd3d package.


%package lib
Summary: lib components for the vkd3d package.
Group: Libraries
Requires: vkd3d-license = %{version}-%{release}

%description lib
lib components for the vkd3d package.


%package lib32
Summary: lib32 components for the vkd3d package.
Group: Default
Requires: vkd3d-license = %{version}-%{release}

%description lib32
lib32 components for the vkd3d package.


%package license
Summary: license components for the vkd3d package.
Group: Default

%description license
license components for the vkd3d package.


%prep
%setup -q -n vkd3d-1.5
cd %{_builddir}/vkd3d-1.5
pushd ..
cp -a vkd3d-1.5 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666025063
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --with-spirv-tools \
--enable-tests
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --with-spirv-tools \
--enable-tests   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1666025063
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vkd3d
cp %{_builddir}/vkd3d-%{version}/COPYING %{buildroot}/usr/share/package-licenses/vkd3d/a4e7ae8a6406fc3281e206c589ccdb890d33fec9 || :
cp %{_builddir}/vkd3d-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/vkd3d/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/vkd3d-compiler

%files dev
%defattr(-,root,root,-)
/usr/include/vkd3d/vkd3d.h
/usr/include/vkd3d/vkd3d_d3d12.h
/usr/include/vkd3d/vkd3d_d3d12sdklayers.h
/usr/include/vkd3d/vkd3d_d3d9types.h
/usr/include/vkd3d/vkd3d_d3dcommon.h
/usr/include/vkd3d/vkd3d_d3dcompiler.h
/usr/include/vkd3d/vkd3d_d3dx9shader.h
/usr/include/vkd3d/vkd3d_dxgibase.h
/usr/include/vkd3d/vkd3d_dxgiformat.h
/usr/include/vkd3d/vkd3d_shader.h
/usr/include/vkd3d/vkd3d_types.h
/usr/include/vkd3d/vkd3d_utils.h
/usr/include/vkd3d/vkd3d_windows.h
/usr/lib64/libvkd3d-shader.so
/usr/lib64/libvkd3d-utils.so
/usr/lib64/libvkd3d.so
/usr/lib64/pkgconfig/libvkd3d-shader.pc
/usr/lib64/pkgconfig/libvkd3d-utils.pc
/usr/lib64/pkgconfig/libvkd3d.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvkd3d-shader.so
/usr/lib32/libvkd3d-utils.so
/usr/lib32/libvkd3d.so
/usr/lib32/pkgconfig/32libvkd3d-shader.pc
/usr/lib32/pkgconfig/32libvkd3d-utils.pc
/usr/lib32/pkgconfig/32libvkd3d.pc
/usr/lib32/pkgconfig/libvkd3d-shader.pc
/usr/lib32/pkgconfig/libvkd3d-utils.pc
/usr/lib32/pkgconfig/libvkd3d.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvkd3d-shader.so.1
/usr/lib64/libvkd3d-shader.so.1.3.0
/usr/lib64/libvkd3d-utils.so.1
/usr/lib64/libvkd3d-utils.so.1.3.1
/usr/lib64/libvkd3d.so.1
/usr/lib64/libvkd3d.so.1.5.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvkd3d-shader.so.1
/usr/lib32/libvkd3d-shader.so.1.3.0
/usr/lib32/libvkd3d-utils.so.1
/usr/lib32/libvkd3d-utils.so.1.3.1
/usr/lib32/libvkd3d.so.1
/usr/lib32/libvkd3d.so.1.5.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vkd3d/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/vkd3d/a4e7ae8a6406fc3281e206c589ccdb890d33fec9
