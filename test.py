from unittest.mock import Mock 
mock = Mock()
import _json

import pkg_resources

class mockObject:
    def __init__(self,project_name,version):
        self.project_name = project_name
        self.version = version

pkg_resources = mock
pkg_resources.working_set = [mockObject('test','1.0.0'),mockObject('test','1.0.0')]

localPackages = [(e.project_name, e.version) for e in pkg_resources.working_set]

print(localPackages)