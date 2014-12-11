Name:           ros-indigo-ueye-cam
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS ueye_cam package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-camera-calibration-parsers
Requires:       ros-indigo-camera-info-manager
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-camera-calibration-parsers
BuildRequires:  ros-indigo-camera-info-manager
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
A ROS nodelet and node that wraps the driver API for UEye cameras by IDS Imaging
Development Systems GMBH.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 11 2014 Anqi Xu <anqixu@cim.mcgill.ca> - 1.0.5-0
- Autogenerated by Bloom

* Mon Dec 01 2014 Anqi Xu <anqixu@cim.mcgill.ca> - 1.0.4-0
- Autogenerated by Bloom

* Wed Nov 05 2014 Anqi Xu <anqixu@cim.mcgill.ca> - 1.0.3-0
- Autogenerated by Bloom

* Thu Oct 16 2014 Anqi Xu <anqixu@cim.mcgill.ca> - 1.0.2-0
- Autogenerated by Bloom

