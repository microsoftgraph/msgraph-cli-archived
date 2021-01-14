# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from unittest import TestCase
import tempfile

from msgraph.cli.core.util import get_file_json, shell_safe_json_parse


class TestUtils(TestCase):
    def test_load_json_from_file(self):
        _, pathname = tempfile.mkstemp()

        # test good case
        with open(pathname, 'w') as good_file:
            good_file.write('{"key1":"value1", "key2":"value2"}')
        result = get_file_json(pathname)
        self.assertEqual('value2', result['key2'])

        # test error case
        with open(pathname, 'w') as bad_file:
            try:
                bad_file.write('{"key1":"value1" "key2":"value2"}')
                get_file_json(pathname)
                self.fail('expect throw on reading from badly formatted file')
            except Exception as ex:  # pylint: disable=broad-except
                self.assertTrue(
                    str(ex).find('contains error: Expecting value: line 1 column 1 (char 0)'))

    def test_shell_safe_json_parse(self):
        dict_obj = {'a': 'b & c'}
        list_obj = [{'a': 'b & c'}]
        failed_strings = []

        valid_dict_strings = ['{"a": "b & c"}', "{'a': 'b & c'}", "{\"a\": \"b & c\"}"]
        for string in valid_dict_strings:
            actual = shell_safe_json_parse(string)
            try:
                self.assertEqual(actual, dict_obj)
            except AssertionError:
                failed_strings.append(string)

        valid_list_strings = ['[{"a": "b & c"}]', "[{'a': 'b & c'}]", "[{\"a\": \"b & c\"}]"]
        for string in valid_list_strings:
            actual = shell_safe_json_parse(string)
            try:
                self.assertEqual(actual, list_obj)
            except AssertionError:
                failed_strings.append(string)

        self.assertEqual(len(failed_strings), 0,
                         'The following patterns failed: {}'.format(failed_strings))
