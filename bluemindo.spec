# TODO:
# - doesn't appear the gui
Summary:	Bluemindo is a very simple audio player
Summary(hu.UTF-8):	Bluemindo egy nagyon egyszerű audió lejátszó
Name:		bluemindo
Version:	0.3
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	http://codingteam.net/project/bluemindo/download/file/%{name}-%{version}.tar.gz
# Source0-md5:	d30c30e6a27a4ac63f57e06627b28e37
URL:		http://bluemindo.codingteam.net/
BuildRequires:	python-gstreamer
BuildRequires:	python-pygtk-glade
BuildRequires:	python-pygtk-gtk
BuildRequires:	python-pynotify-devel
BuildRequires:	python-tagpy
BuildRequires:	python-xmpppy
Requires:	python-tagpy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bluemindo is a very simple audio player.

%description -l hu.UTF-8
Bluemindo egy nagyon egyszerű audió lejátszó.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_desktopdir},%{_pixmapsdir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/src/%{name}.py
%{_datadir}/%{name}/src/extensionsloader.py
%{_datadir}/%{name}/src/mainapplication.py
%{_datadir}/%{name}/src/common
%{_datadir}/%{name}/src/gui
%{_datadir}/%{name}/src/handlers
%{_datadir}/%{name}/src/media
%{_datadir}/%{name}/src/modules
%{_datadir}/%{name}/src/plugins
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/image
%{_desktopdir}/Bluemindo.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/*
