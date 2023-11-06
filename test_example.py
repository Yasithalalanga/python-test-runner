'''
Copyright (c) 2022, WSO2 Inc. (http://www.wso2.com). All Rights Reserved.

This software is the property of WSO2 Inc. and its suppliers, if any.
Dissemination of any information or reproduction of any material contained
herein is strictly forbidden, unless permitted by WSO2 in accordance with
the WSO2 Commercial License available at http://wso2.com/licenses.
For specific language governing the permissions and limitations under
this license, please see the license as well as any agreement you’ve
entered into with WSO2 governing the purchase of this software and any
associated services.
'''
# test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

# Pickup environment variables and log them
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Environment variables:')
for key, value in os.environ.items():
    logger.info(f'{key}={value}')
