%global goipath     github.com/mattn/go-zglob
%global commit      254b632af962d02711182299973af169f291925c

%gometa

%global common_description %{expand:
globbing utility}

%global golicenses    LICENSE
%global godocs        *.md

Name:       %{goname}
Version:    0.0.3
Release:    %autorelease
Summary:    globbing utility
License:    MIT
URL:        %{gourl}
Source:     %{gosource}

BuildRequires: go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

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
%{_bindir}/zglob

%gopkgfiles

%changelog
%autochangelog
