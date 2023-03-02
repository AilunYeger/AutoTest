import pytest
from operation.operation import operator
from utils.logger import logger
from testcase.conftest import case_data


class TestAuth:
    @pytest.mark.parametrize("param", case_data('test_auth'))
    def test_auth(self, param):
        logger.info("*************** 开始执行用例 ***************")
        result = operator.do_auth(**param)
        