#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ragg
Version  : 1.1.2
Release  : 9
URL      : https://cran.r-project.org/src/contrib/ragg_1.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ragg_1.1.2.tar.gz
Summary  : Graphic Devices Based on AGG
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: R-ragg-lib = %{version}-%{release}
Requires: R-systemfonts
Requires: R-textshaping
BuildRequires : R-systemfonts
BuildRequires : R-textshaping
BuildRequires : buildreq-R
BuildRequires : freetype-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : tiff-dev

%description
2D drawing library. The 'ragg' package provides a set of graphic devices 
    based on AGG to use as alternative to the raster devices provided through
    the 'grDevices' package.

%package lib
Summary: lib components for the R-ragg package.
Group: Libraries

%description lib
lib components for the R-ragg package.


%prep
%setup -q -c -n ragg
cd %{_builddir}/ragg

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615993750

%install
export SOURCE_DATE_EPOCH=1615993750
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ragg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ragg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ragg
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ragg || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ragg/DESCRIPTION
/usr/lib64/R/library/ragg/INDEX
/usr/lib64/R/library/ragg/LICENSE
/usr/lib64/R/library/ragg/Meta/Rd.rds
/usr/lib64/R/library/ragg/Meta/features.rds
/usr/lib64/R/library/ragg/Meta/hsearch.rds
/usr/lib64/R/library/ragg/Meta/links.rds
/usr/lib64/R/library/ragg/Meta/nsInfo.rds
/usr/lib64/R/library/ragg/Meta/package.rds
/usr/lib64/R/library/ragg/NAMESPACE
/usr/lib64/R/library/ragg/NEWS.md
/usr/lib64/R/library/ragg/R/ragg
/usr/lib64/R/library/ragg/R/ragg.rdb
/usr/lib64/R/library/ragg/R/ragg.rdx
/usr/lib64/R/library/ragg/help/AnIndex
/usr/lib64/R/library/ragg/help/aliases.rds
/usr/lib64/R/library/ragg/help/figures/README-unnamed-chunk-3-1.png
/usr/lib64/R/library/ragg/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/ragg/help/figures/logo.png
/usr/lib64/R/library/ragg/help/paths.rds
/usr/lib64/R/library/ragg/help/ragg.rdb
/usr/lib64/R/library/ragg/help/ragg.rdx
/usr/lib64/R/library/ragg/html/00Index.html
/usr/lib64/R/library/ragg/html/R.css
/usr/lib64/R/library/ragg/tests/testthat.R
/usr/lib64/R/library/ragg/tests/testthat/test-circle.R
/usr/lib64/R/library/ragg/tests/testthat/test-jpeg.R
/usr/lib64/R/library/ragg/tests/testthat/test-line.R
/usr/lib64/R/library/ragg/tests/testthat/test-path.R
/usr/lib64/R/library/ragg/tests/testthat/test-png.R
/usr/lib64/R/library/ragg/tests/testthat/test-polygon.R
/usr/lib64/R/library/ragg/tests/testthat/test-polyline.R
/usr/lib64/R/library/ragg/tests/testthat/test-ppm.R
/usr/lib64/R/library/ragg/tests/testthat/test-raster.R
/usr/lib64/R/library/ragg/tests/testthat/test-rect.R
/usr/lib64/R/library/ragg/tests/testthat/test-text.R
/usr/lib64/R/library/ragg/tests/testthat/test-tiff.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ragg/libs/ragg.so
