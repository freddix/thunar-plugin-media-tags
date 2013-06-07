%define		org_name	thunar-media-tags-plugin

Summary:	Media Tags plugin for the Thunar file manager
Name:		thunar-plugin-media-tags
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/0.2/%{org_name}-%{version}.tar.bz2
# Source0-md5:	0106e900714f86ccbafdc72238d3cf8d
URL:		http://goodies.xfce.org/projects/thunar-plugins/thunar-media-tags-plugin
BuildRequires:	Thunar-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	taglib-devel
BuildRequires:	xfce4-dev-tools
Requires:	Thunar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin adds special features for media files to the Thunar file
manager. It includes a special media file page for the file properties
dialog, a tag editor for ID3 or Ogg/Vorbis tags and a so-called bulk
renamer, which allows users to rename multiple audio files at once,
based on their tags.

%prep
%setup -qn %{org_name}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/thunarx-2/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/thunarx-2/%{org_name}.so

