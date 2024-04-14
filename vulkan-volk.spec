Summary:	Meta-loader for Vulkan
Summary(pl.UTF-8):	Meta-loader dla Vulkana
Name:		vulkan-volk
Version:	1.3.280.0
%define	gitref	vulkan-sdk-%{version}
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/zeux/volk/tags
Source0:	https://github.com/zeux/volk/archive/%{gitref}/volk-%{gitref}.tar.gz
# Source0-md5:	2154f24cd28be1adcf48ac34cb0daa59
URL:		https://github.com/zeux/volk
BuildRequires:	cmake >= 3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
volk is a meta-loader for Vulkan. It allows you to dynamically load
entrypoints required to use Vulkan without linking to Vulkan DLL or
statically linking Vulkan loader. Additionally, volk simplifies the
use of Vulkan extensions by automatically loading all associated
entrypoints. Finally, volk enables loading Vulkan entrypoints directly
from the driver which can increase performance by skipping loader
dispatch overhead.

%description -l pl.UTF-8
volk to meta-loader dla Vulkana. Pozwala dynamicznie ładować punkty
wejściowe wymagane do używania Vulkana bez konsolidacji z biblioteką
dynamiczną Vulkana ani statycznej konsolidacji z loaderem Vulkana.
Ponadto volk upraszcza używanie rozszerzeń Vulkana automatycznie
ładując wszystkie powiązane punkty wejściowe. Pozwala także ładować
punkty wejściowe Vulkana bezpośrednio ze sterownika, co może zwiększyć
wydajność poprzez pominięcie narzutu przekazywania w loaderze.

%package devel
Summary:	Header file and static Vulkan volk library
Summary(pl.UTF-8):	Plik nagłówkowy i biblioteka statyczna Vulkan volk
Group:		Development/Libraries
Conflicts:	gnuradio-devel < 3.9.0.0
Conflicts:	volk-devel

%description devel
volk is a meta-loader for Vulkan. It allows you to dynamically load
entrypoints required to use Vulkan without linking to Vulkan DLL or
statically linking Vulkan loader. Additionally, volk simplifies the
use of Vulkan extensions by automatically loading all associated
entrypoints. Finally, volk enables loading Vulkan entrypoints directly
from the driver which can increase performance by skipping loader
dispatch overhead.

%description devel -l pl.UTF-8
volk to meta-loader dla Vulkana. Pozwala dynamicznie ładować punkty
wejściowe wymagane do używania Vulkana bez konsolidacji z biblioteką
dynamiczną Vulkana ani statycznej konsolidacji z loaderem Vulkana.
Ponadto volk upraszcza używanie rozszerzeń Vulkana automatycznie
ładując wszystkie powiązane punkty wejściowe. Pozwala także ładować
punkty wejściowe Vulkana bezpośrednio ze sterownika, co może zwiększyć
wydajność poprzez pominięcie narzutu przekazywania w loaderze.

%prep
%setup -q -n volk-%{gitref}

%build
install -d build
cd build
%cmake .. \
	-DVOLK_INSTALL=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%{_libdir}/libvolk.a
%{_includedir}/volk.c
%{_includedir}/volk.h
%{_libdir}/cmake/volk
