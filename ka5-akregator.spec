%define		kdeappsver	20.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		akregator
Summary:	A KDE Feed Reader
Name:		ka5-%{kaname}
Version:	20.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	548cdc99ac47e8a55d23d6e3c9bb09bd
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
BuildRequires:	ka5-grantleetheme-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-syndication-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
%attr(755,root,root) %{_datadir}/kconf_update/akregator-15.08-kickoff.sh
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
%{_datadir}/kservices5/feed.protocol
%dir %{_libdir}/qt5/plugins/kontact5
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact5/kontact_akregatorplugin.so
# TODO proper package for dir
%dir %{_datadir}/kservices5/kontact
%{_datadir}/kservices5/kontact/akregatorplugin.desktop
%{_datadir}/kservicetypes5/akregator_plugin.desktop
%{_datadir}/metainfo/org.kde.akregator.appdata.xml
%{_datadir}/qlogging-categories5/akregator.categories
%{_datadir}/qlogging-categories5/akregator.renamecategories
