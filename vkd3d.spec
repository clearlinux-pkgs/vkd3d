#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vkd3d
Version  : 1c7df3f
Release  : 3
URL      : https://github.com/d3d12/vkd3d/archive/1c7df3f.tar.gz
Source0  : https://github.com/d3d12/vkd3d/archive/1c7df3f.tar.gz
Summary  : The vkd3d 3D Graphics Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: vkd3d-lib = %{version}-%{release}
Requires: vkd3d-license = %{version}-%{release}
BuildRequires : SPIRV-Headers-dev
BuildRequires : SPIRV-Tools
BuildRequires : SPIRV-Tools-dev
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Loader-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32SPIRV-Tools-shared)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xcb-keysyms)
BuildRequires : pkgconfig(SPIRV-Tools-shared)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : sed
BuildRequires : util-linux
BuildRequires : wine-bin
Patch1: backport-vulkan-range.patch

%description
=============================
The vkd3d 3D Graphics Library
=============================

%package dev
Summary: dev components for the vkd3d package.
Group: Development
Requires: vkd3d-lib = %{version}-%{release}
Provides: vkd3d-devel = %{version}-%{release}
Requires: vkd3d = %{version}-%{release}

%description dev
dev components for the vkd3d package.


%package dev32
Summary: dev32 components for the vkd3d package.
Group: Default
Requires: vkd3d-lib32 = %{version}-%{release}
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
%setup -q -n vkd3d-1c7df3f
cd %{_builddir}/vkd3d-1c7df3f
%patch1 -p1
pushd ..
cp -a vkd3d-1c7df3f build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589209621
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --with-spirv-tools \
--enable-tests
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static --with-spirv-tools \
--enable-tests  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
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
export SOURCE_DATE_EPOCH=1589209621
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vkd3d
cp %{_builddir}/vkd3d-1c7df3f/COPYING %{buildroot}/usr/share/package-licenses/vkd3d/b02df56a2b74d40e71f032ae77634b125a51f1a5
cp %{_builddir}/vkd3d-1c7df3f/LICENSE %{buildroot}/usr/share/package-licenses/vkd3d/01a6b4bf79aca9b556822601186afab86e8c4fbf
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
/usr/include/vkd3d/vkd3d.h
/usr/include/vkd3d/vkd3d_d3d12.h
/usr/include/vkd3d/vkd3d_d3dcommon.h
/usr/include/vkd3d/vkd3d_dxgibase.h
/usr/include/vkd3d/vkd3d_dxgiformat.h
/usr/include/vkd3d/vkd3d_utils.h
/usr/include/vkd3d/vkd3d_windows.h
/usr/lib64/libvkd3d-utils.so
/usr/lib64/libvkd3d.so
/usr/lib64/pkgconfig/libvkd3d-utils.pc
/usr/lib64/pkgconfig/libvkd3d.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libvkd3d-utils.so
/usr/lib32/libvkd3d.so
/usr/lib32/pkgconfig/32libvkd3d-utils.pc
/usr/lib32/pkgconfig/32libvkd3d.pc
/usr/lib32/pkgconfig/libvkd3d-utils.pc
/usr/lib32/pkgconfig/libvkd3d.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvkd3d-utils.so.1
/usr/lib64/libvkd3d-utils.so.1.0.0
/usr/lib64/libvkd3d.so.1
/usr/lib64/libvkd3d.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libvkd3d-utils.so.1
/usr/lib32/libvkd3d-utils.so.1.0.0
/usr/lib32/libvkd3d.so.1
/usr/lib32/libvkd3d.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vkd3d/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/vkd3d/b02df56a2b74d40e71f032ae77634b125a51f1a5