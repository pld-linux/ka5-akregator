%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		akregator
Summary:	A KDE Feed Reader
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	87ab23e58cafc571bac9e2df3ff453c3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt5-devel >= 5.1
BuildRequires:	ka5-akonadi-mime-devel
BuildRequires:	ka5-grantleetheme-devel >= 18.12.0
BuildRequires:	ka5-kontactinterface-devel >= 18.12.0
BuildRequires:	ka5-kpimtextedit-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	ka5-libkleo-devel >= 18.12.0
BuildRequires:	ka5-messagelib-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcmutils-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-knotifications-devel >= 5.51.0
BuildRequires:	kf5-knotifyconfig-devel >= 5.51.0
BuildRequires:	kf5-kparts-devel >= 5.53.0
BuildRequires:	kf5-ktexteditor-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	kf5-syndication-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE Feed Reader.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/akregator.categories
/etc/xdg/akregator.renamecategories
%attr(755,root,root) %{_bindir}/akregator
%attr(755,root,root) %{_bindir}/akregatorstorageexporter
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so
%attr(755,root,root) %ghost %{_libdir}/libakregatorinterfaces.so.5
%attr(755,root,root) %{_libdir}/libakregatorinterfaces.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libakregatorprivate.so.5
%attr(755,root,root) %{_libdir}/libakregatorprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_config_advanced.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_config_appearance.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_config_archive.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_config_browser.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_config_general.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_config_plugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregator_mk4storage_plugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregatorpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_akregatorplugin.so
%{_datadir}/akregator
%{_desktopdir}/org.kde.akregator.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.akregator.part.xml
%{_iconsdir}/hicolor/128x128/apps/akregator.png
%{_iconsdir}/hicolor/16x16/apps/akregator.png
%{_iconsdir}/hicolor/16x16/apps/akregator_empty.png
%{_iconsdir}/hicolor/22x22/apps/akregator.png
%{_iconsdir}/hicolor/32x32/apps/akregator.png
%{_iconsdir}/hicolor/48x48/apps/akregator.png
%{_iconsdir}/hicolor/64x64/apps/akregator.png
%{_iconsdir}/hicolor/scalable/apps/akregator.svg
%{_datadir}/kconf_update/akregator-15.08-kickoff.sh
%{_datadir}/kconf_update/akregator.upd
%{_datadir}/knotifications5/akregator.notifyrc
# TODO proper package for dirs
%dir %{_datadir}/kontact
%dir %{_datadir}/kontact/ksettingsdialog
%{_datadir}/kontact/ksettingsdialog/akregator.setdlg
%{_datadir}/kservices5/akregator_config_advanced.desktop
%{_datadir}/kservices5/akregator_config_appearance.desktop
%{_datadir}/kservices5/akregator_config_archive.desktop
%{_datadir}/kservices5/akregator_config_browser.desktop
%{_datadir}/kservices5/akregator_config_general.desktop
%{_datadir}/kservices5/akregator_config_plugins.desktop
%{_datadir}/kservices5/akregator_mk4storage_plugin.desktop
%{_datadir}/kservices5/akregator_part.desktop
%{_datadir}/kservices5/feed.protocol
# TODO proper package for dir
%dir %{_datadir}/kservices5/kontact
%{_datadir}/kservices5/kontact/akregatorplugin.desktop
%{_datadir}/kservicetypes5/akregator_plugin.desktop
%{_datadir}/metainfo/org.kde.akregator.appdata.xml
