from text_functions.block_to_block_type import *
import unittest

class TestBlockToBlockType(unittest.TestCase):
    def case(self, text, expected):
        result = block_to_block_type(text)  
        super().assertEqual(expected, result)
    
    def test_paragraph(self):
        self.case("test paragrahp", BlockType.PARAGRAPH)

    def test_header(self):
        self.case("# test paragrahp", BlockType.HEADING)
    def test_header_no_space_paragraph(self):
        self.case("#test paragrahp", BlockType.PARAGRAPH)
    def test_header_2(self):
        self.case("## test paragrahp", BlockType.HEADING)
    def test_header_3(self):
        self.case("### test paragrahp", BlockType.HEADING)
    def test_header_4(self):
        self.case("#### test paragrahp", BlockType.HEADING)
    def test_header_5(self):
        self.case("##### test paragrahp", BlockType.HEADING)
    def test_header_6(self):
        self.case("###### test paragrahp", BlockType.HEADING)
    def test_header_7_paragraph(self):
        self.case("####### test paragrahp", BlockType.PARAGRAPH)


    def test_code(self):
        self.case("```\ntest code\n```", BlockType.CODE)
    def test_code_multiline(self):
        self.case("```\ntest \nmore code\ncode\n```", BlockType.CODE)
    def test_code_no_end(self):
        self.case("```\ntest \nmore code\ncode\n", BlockType.PARAGRAPH)

    def test_quote(self):
        self.case(">quote3\n> quote2", BlockType.QUOTE)
    def test_quote_missed_mid_paragraph(self):
        self.case(">quote 3\n quote 2\n>quote 3", BlockType.PARAGRAPH)
    
    def test_unordered(self):
        self.case("- text\n- test 2\n- test 3", BlockType.UNORDERED_LIST)
    def test_unordered_missed_mid_paragraph(self):
        self.case("- text\n test 2\n- test 3", BlockType.PARAGRAPH)
    def test_unordered_no_space_paragraph(self):
        self.case("- text\n-test 2\n- test 3", BlockType.PARAGRAPH)

    def test_ordered(self):
        self.case("1. ordered\n2. ordered 2\n3. ordered", BlockType.ORDERED_LIST)
    def test_ordered_wrong_order_paragraph(self):
        self.case("1. ordered\n3. ordered 2\n2. ordered", BlockType.PARAGRAPH)
    def test_ordered_missed_space_paragraph(self):
        self.case("1. ordered\n2.ordered 2\n3. ordered", BlockType.PARAGRAPH)
        
        

    