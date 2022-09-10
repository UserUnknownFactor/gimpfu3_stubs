# -*- coding:utf-8 -*-
import unittest, os, re, datetime, tempfile, copy
from module_redeclarator import *

#sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

class TestModuleRedeclarator(unittest.TestCase):
    mc = ModuleRedeclarator("test", "test", "test", "test")

    def test_parse_func_do(self):
            self.assertEqual(
                self.mc.parse_func_doc(
                "get_display(self, info:Gio.AppInfo, files:list) -> str or None", \
                "do_get_display", "do_get_display", "TestClass", "staticmethod"
                ),
                ('do_get_display(self, info:Gio.AppInfo, files:list)', None, \
                'Union[str, None]', 'restored from __doc__')
            )

    def test_parse_func_new(self):
            self.assertEqual(
                self.mc.parse_func_doc(
                "new(checksum_type:GLib.ChecksumType) -> GLib.Checksum or None", \
                "__new__", "__new__", "TestClass", "staticmethod"
                ),
                ('__new__(checksum_type:GLib.ChecksumType)', None, \
                'Union[GLib.Checksum, None]', 'restored from __doc__')
            )

    def test_parse_func_doc_ret_named(self):
            self.assertEqual(
                self.mc.parse_func_doc(
                "lower_bound(str:str, base:int, min:int, max:int) -> bool, out_num:int", \
                "lower_bound", "lower_bound", "TestClass"
                ),
                ('lower_bound(str:str, base:int, min:int, max:int)', None, \
                'tuple[bool, out_num:int]', 'restored from __doc__')
            )
    
    def test_parse_func_doc_ret_or(self):
            self.assertEqual(
                self.mc.parse_func_doc(
                "lower_bound(str:str, base:int, min:int, max:int) -> bool, out_num:int or None", \
                "lower_bound", "lower_bound", "TestClass"
                ),
                ('lower_bound(str:str, base:int, min:int, max:int)', None, \
                'Union[tuple[bool, out_num:int], None]', 'restored from __doc__')
           )

    def test_parse_func_doc_param_middle(self):
            self.assertEqual(
                self.mc.parse_func_doc(
                "lower_bound(str:str, base:int=0, min:int, max:int)", \
                "lower_bound", "lower_bound", "TestClass"
                ),
                ('lower_bound(str:str, base:int, min:int, max:int)', None, \
                '', 'restored from __doc__')

           )

"""
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertEqual('foo'.upper(), 'FOO')
        with self.assertRaises(TypeError):
            s.split(2)
"""

if __name__ == '__main__':
    unittest.main()