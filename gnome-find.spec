Summary:	A GNOME version of the GNU "find" utility
Summary(es):	Una versión gráfica para GNOME de la utilidad GNU "find"
Summary(pl):	Graficzna wersja "find" dla ¶rodowiska GNOME
Name:		gnome-find
Version:	0.3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	cdfe78acd65bd42a85e8594853098e5e
URL:		http://gnome-find.sourceforge.net/
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	gnome-libs-devel >= 1.0.53
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libglade-devel >= 0.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-find is a graphical, GNOME version of the GNU "find" utility.

%description -l es
gnome-find es una versión gráfica para GNOME de la utilidad GNU
"find".

%description -l pl
gnome-find to graficzna wersja wersja programu "find" przeznaczona dla
¶rodowiska GNOME.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
install gnome-find.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README TODO ChangeLog
%attr(755,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_applnkdir}/Utilities/%{name}.desktop
%{_datadir}/%{name}
