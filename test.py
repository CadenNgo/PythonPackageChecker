from unittest.mock import Mock 
mock = Mock()

import pkg_resources

pkg_resources = mock
print(dir(pkg_resources))