#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-wrapt
Version  : 1.14.1
Release  : 74
URL      : https://files.pythonhosted.org/packages/11/eb/e06e77394d6cf09977d92bff310cb0392930c08a338f99af6066a5a98f92/wrapt-1.14.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/eb/e06e77394d6cf09977d92bff310cb0392930c08a338f99af6066a5a98f92/wrapt-1.14.1.tar.gz
Summary  : Module for decorators, wrappers and monkey patching.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-wrapt-filemap = %{version}-%{release}
Requires: pypi-wrapt-lib = %{version}-%{release}
Requires: pypi-wrapt-license = %{version}-%{release}
Requires: pypi-wrapt-python = %{version}-%{release}
Requires: pypi-wrapt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
wrapt
=====
|Actions| |PyPI|
The aim of the **wrapt** module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package filemap
Summary: filemap components for the pypi-wrapt package.
Group: Default

%description filemap
filemap components for the pypi-wrapt package.


%package lib
Summary: lib components for the pypi-wrapt package.
Group: Libraries
Requires: pypi-wrapt-license = %{version}-%{release}
Requires: pypi-wrapt-filemap = %{version}-%{release}

%description lib
lib components for the pypi-wrapt package.


%package license
Summary: license components for the pypi-wrapt package.
Group: Default

%description license
license components for the pypi-wrapt package.


%package python
Summary: python components for the pypi-wrapt package.
Group: Default
Requires: pypi-wrapt-python3 = %{version}-%{release}

%description python
python components for the pypi-wrapt package.


%package python3
Summary: python3 components for the pypi-wrapt package.
Group: Default
Requires: pypi-wrapt-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(wrapt)

%description python3
python3 components for the pypi-wrapt package.


%prep
%setup -q -n wrapt-1.14.1
cd %{_builddir}/wrapt-1.14.1
pushd ..
cp -a wrapt-1.14.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361320
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-wrapt
cp %{_builddir}/wrapt-1.14.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-wrapt/af810b42f86441de738d81955141690f9a198a62
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-wrapt

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-wrapt/af810b42f86441de738d81955141690f9a198a62

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
