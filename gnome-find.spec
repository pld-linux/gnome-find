%define    ver     0.3
%define    rel     1
%define    prefix  /usr

Summary: A GNOME version of the GNU "find" utility.
Summary(es): Una versión gráfica para GNOME de la utilidad GNU "find".
Name: gnome-find
Version: %{ver}
Release: %{rel}
Copyright: GPL
Url: http://gnome-find.sourceforge.net
Group: Utilities/System
Source: %{name}-%{ver}.tar.gz
Requires: gnome-libs >= 1.0.53 libglade >= 0.11 gtk+ >= 1.2.0 glib >= 1.2.0
BuildRoot: /var/tmp/%{name}-root

%description
gnome-find is a graphical, GNOME version of the GNU "find" utility.

%description -l es
gnome-find es una versión gráfica para GNOME de la utilidad GNU "find".

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT%{prefix}/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS HACKING NEWS README TODO ChangeLog
%attr(755,root,root)
%{prefix}/bin/%{name}
%{prefix}/man/man1/%{name}.1
%{prefix}/share/gnome/apps/Utilities/%{name}.desktop
%{prefix}/share/%{name}

%changelog
* Wed May 17 2000 Andy C. Kahn <ackahn@netapp.com>
- Various fixes so that the RPM file actually builds.
- Spanish translation from Joel Barrios <linux@jjnet.prohosting.com>

* Mon May 08 2000 Andy C. Kahn <ackahn@netapp.com>
- Initial package
