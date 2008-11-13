%define	_lang	pl
%define	_reg	PL
%define _lare	%{_lang}-%{_reg}
Summary:	Polish resources for Iceape
Summary(pl.UTF-8):	Polskie pliki językowe dla Iceape
Name:		iceape-lang-%{_lang}
Version:	1.1.13
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	d53383be51890160407d9fb661eed28e
Source1:	http://www.mozilla-enigmail.org/download/release/0.95/enigmail-%{_lare}-0.95.xpi
# Source1-md5:	3ac349c7b6a1ebbd80f11c8911f5102d
Source2:	gen-installed-chrome.sh
URL:		http://www.seamonkey-project.org/
BuildRequires:	unzip
BuildRequires:	util-linux
Requires(post,postun):	iceape >= %{version}
Requires(post,postun):	textutils
Requires:	iceape >= %{version}
Obsoletes:	mozilla-lang-pl
Obsoletes:	seamonkey-lang-pl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/iceape/chrome

%description
Polish resources for Iceape.

%description -l pl.UTF-8
Polskie pliki językowe dla Iceape.

%prep
%setup -q -c
%{__unzip} -o -qq %{SOURCE1}
install %{SOURCE2} .
./gen-installed-chrome.sh locale bin/chrome/{%{_reg},%{_lare},%{_lang}-unix}.jar \
	> lang-%{_lang}-installed-chrome.txt
./gen-installed-chrome.sh locale chrome/enigmail-%{_lare}.jar \
	>> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{%{_reg},%{_lare},%{_lang}-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install chrome/enigmail-%{_lare}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/{searchplugins,defaults,dictionaries} $RPM_BUILD_ROOT%{_datadir}/iceape
rm $RPM_BUILD_ROOT%{_datadir}/iceape/searchplugins/google.*

# rebrand locale for iceape
cd $RPM_BUILD_ROOT%{_chromedir}
unzip %{_lare}.jar locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties \
	locale/%{_lare}/communicator/search/default.htm locale/%{_lare}/navigator/navigator.properties \
	locale/%{_lare}/venkman/venkman.properties locale/%{_lare}/sroaming/transfer.properties  \
	locale/%{_lare}/global/about.dtd locale/%{_lare}/global/appstrings.properties  \
	locale/%{_lare}/communicator/profile/profileManager.properties \
	locale/%{_lare}/communicator/pref/pref-history.dtd \
	locale/%{_lare}/communicator/pref/pref-languages.dtd \
	locale/%{_lare}/communicator/pref/pref-smartupdate.dtd
sed -i -e 's/SeaMonkey/Iceape/g;' locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties \
	locale/%{_lare}/communicator/search/default.htm locale/%{_lare}/navigator/navigator.properties \
	locale/%{_lare}/venkman/venkman.properties locale/%{_lare}/sroaming/transfer.properties  \
	locale/%{_lare}/global/about.dtd locale/%{_lare}/global/appstrings.properties  \
	locale/%{_lare}/communicator/profile/profileManager.properties \
	locale/%{_lare}/communicator/pref/pref-history.dtd \
	locale/%{_lare}/communicator/pref/pref-languages.dtd \
	locale/%{_lare}/communicator/pref/pref-smartupdate.dtd
zip -0 %{_lare}.jar locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties \
	locale/%{_lare}/communicator/search/default.htm locale/%{_lare}/navigator/navigator.properties \
	locale/%{_lare}/venkman/venkman.properties locale/%{_lare}/sroaming/transfer.properties  \
	locale/%{_lare}/global/about.dtd locale/%{_lare}/global/appstrings.properties  \
	locale/%{_lare}/communicator/profile/profileManager.properties \
	locale/%{_lare}/communicator/pref/pref-history.dtd \
	locale/%{_lare}/communicator/pref/pref-languages.dtd \
	locale/%{_lare}/communicator/pref/pref-smartupdate.dtd
rm -f locale/%{_lare}/branding/brand.dtd locale/%{_lare}/branding/brand.properties \
	locale/%{_lare}/communicator/search/default.htm locale/%{_lare}/navigator/navigator.properties \
	locale/%{_lare}/venkman/venkman.properties locale/%{_lare}/sroaming/transfer.properties  \
	locale/%{_lare}/global/about.dtd locale/%{_lare}/global/appstrings.properties  \
	locale/%{_lare}/communicator/profile/profileManager.properties \
	locale/%{_lare}/communicator/pref/pref-history.dtd \
	locale/%{_lare}/communicator/pref/pref-languages.dtd \
	locale/%{_lare}/communicator/pref/pref-smartupdate.dtd

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/iceape-chrome+xpcom-generate

%postun
%{_sbindir}/iceape-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/enigmail-%{_lare}.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/iceape/searchplugins/*
# dir not provided
#%{_datadir}/iceape/defaults/isp/%{_reg}
%{_datadir}/iceape/defaults/messenger/%{_reg}
%{_datadir}/iceape/defaults/profile/%{_reg}
%{_datadir}/iceape/dictionaries/*
