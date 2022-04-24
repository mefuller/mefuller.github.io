%global goipath     github.com/go-task/task
%global forgeurl    https://github.com/go-task/task
Version:            3.12.0

%gometa

%global common_description %{expand:
Task is a task runner / build tool that aims to be simple and easy to use.}

%global golicenses    LICENSE
%global godocs        *.md

Name:       %{goname}
Release:    %autorelease
Summary:    First go package
License:    MIT
URL:        https://taskfile.dev/#/
Source0:    %{gosource}
Source1:    https://github.com/go-task/slim-sprig/archive/master.tar.gz
Source2:    https://github.com/radovskyb/watcher/archive/refs/tags/v1.0.7.tar.gz
Source3:    https://github.com/mattn/go-zglob/archive/master.tar.gz

BuildRequires: go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/Task

%gopkgfiles

%changelog
%autochangelog
