#!/usr/bin/python
# -*- coding: utf-8 -*-
goodstr = "I come in peace."
evilstr = "Prepare to be destroyed!"
blob = """
         ]��:Ƶ��^`b�c��2�p �"DrC�Q�&�4���/�K
f�≧#�����ŃX�F^&9��ا�t��1�֡�	��8��~ ś�QbY�{���m֖�h�ύ҄舩�1��32��숨�)x
"""
goodhex = """
         ]��:Ƶ��^`b�c��2�p �"DrC�Q�&�4���/�K
f�≧#�����ŃX�F^&9��ا�t��1�֡�	��8��~ ś�QbY�{���m֖�h�ύ҄舩�1��32��숨�)x
"""
evilhex = """
         ]��:Ƶ��^`b�c��2rp �"DrC�Q�&�4���/�K
f��	�#�����ŃX��^&9��ا�t��1�֡�	��8I�~ ś�QbY�{���m֖�h�ύR�舩�1��32�����)x
"""
if(blob == goodhex):
	print goodstr
else:
	print evilstr
