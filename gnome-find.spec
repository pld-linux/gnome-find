Summary:	A GNOME version of the GNU "find" utility
Summary(es):	Una versión gráfica para GNOME de la utilidad GNU "find"
Summary(pl):	Graficzna wersja "find" dla ¶rodowiska GNOME
Name:		gnome-find
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://download.sourceforge.net/gnome-find/%{name}-%{version}.tar.gz
URL:		http://gnome-find.sourceforge.net/
BuildRequires:	gnome-libs-devel >= 1.0.53
BuildRequires:	libglade-devel >= 0.11
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	glib-devel >= 1.2.0
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
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README TODO ChangeLog
%attr(755,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1
%{_applnkdir}/Utilities/%{name}.desktop
%{_datadir}/%{name}
