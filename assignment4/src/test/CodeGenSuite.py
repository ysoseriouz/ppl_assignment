import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test_1(self):
        input = r"""
Function: main
Body:
    print(string_of_int(1));
EndBody.
"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 500))


    def test_2(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(1));
EndBody.
"""
        expect = r"""1
"""
        self.assertTrue(TestCodeGen.test(input, expect, 501))


    def test_3(self):
        input = r"""
Function: main
Body:
    print(string_of_float(1.5));
EndBody.
"""
        expect = r"""1.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 502))


    def test_4(self):
        input = r"""
Function: main
Body:
    print(string_of_float(0.5));
EndBody.
"""
        expect = r"""0.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 503))


    def test_5(self):
        input = r"""
Function: main
Body:
    print(string_of_float(0.005));
EndBody.
"""
        expect = r"""0.005"""
        self.assertTrue(TestCodeGen.test(input, expect, 504))


    def test_6(self):
        input = r"""
Function: main
Body:
    print(string_of_float(1000.0001));
EndBody.
"""
        expect = r"""1000.0001"""
        self.assertTrue(TestCodeGen.test(input, expect, 505))


    def test_7(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_float(999.8999999));
EndBody.
"""
        expect = r"""999.9
"""
        self.assertTrue(TestCodeGen.test(input, expect, 506))


    def test_8(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(True));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 507))


    def test_9(self):
        input = r"""
Function: main
Body:
    print("falSE");
EndBody.
"""
        expect = r"""falSE"""
        self.assertTrue(TestCodeGen.test(input, expect, 508))


    def test_10(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_bool(False));
EndBody.
"""
        expect = r"""false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 509))


    def test_11(self):
        input = r"""
Function: main
Body:
    print(string_of_int(1 + 2));
EndBody.
"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))


    def test_12(self):
        input = r"""
Function: main
Body:
    print(string_of_int(1+2+3+4+5));
EndBody.
"""
        expect = r"""15"""
        self.assertTrue(TestCodeGen.test(input, expect, 511))


    def test_13(self):
        input = r"""
Function: main
Body:
    print(string_of_int(2 - 1));
EndBody.
"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 512))


    def test_14(self):
        input = r"""
Function: main
Body:
    print(string_of_int(1 - 2));
EndBody.
"""
        expect = r"""-1"""
        self.assertTrue(TestCodeGen.test(input, expect, 513))


    def test_15(self):
        input = r"""
Function: main
Body:
    print(string_of_int(1+2-3+4-5+6-7-8-9));
EndBody.
"""
        expect = r"""-19"""
        self.assertTrue(TestCodeGen.test(input, expect, 514))


    def test_16(self):
        input = r"""
Function: main
Body:
    print(string_of_int(4 * 6));
EndBody.
"""
        expect = r"""24"""
        self.assertTrue(TestCodeGen.test(input, expect, 515))


    def test_17(self):
        input = r"""
Function: main
Body:
    print(string_of_int(4*6*9*1*2));
EndBody.
"""
        expect = r"""432"""
        self.assertTrue(TestCodeGen.test(input, expect, 516))


    def test_18(self):
        input = r"""
Function: main
Body:
    print(string_of_int(4*6*9 - 9*4*6));
EndBody.
"""
        expect = r"""0"""
        self.assertTrue(TestCodeGen.test(input, expect, 517))


    def test_19(self):
        input = r"""
Function: main
Body:
    print(string_of_int(1*2*3 + 4*5*6 - 5*6 + 123-456));
EndBody.
"""
        expect = r"""-237"""
        self.assertTrue(TestCodeGen.test(input, expect, 518))


    def test_20(self):
        input = r"""
Function: main
Body:
    print(string_of_int(5 \ 2));
EndBody.
"""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input, expect, 519))


    def test_21(self):
        input = r"""
Function: main
Body:
    print(string_of_int(198 \ 8));
EndBody.
"""
        expect = r"""24"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))


    def test_22(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123.5 +. 456.0));
EndBody.
"""
        expect = r"""579.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 521))


    def test_23(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123.5 +. 456.1));
EndBody.
"""
        expect = r"""579.6"""
        self.assertTrue(TestCodeGen.test(input, expect, 522))


    def test_24(self):
        input = r"""
Function: main
Body:
    print(string_of_float(1.2 +. 3.4 -. 5.6 +. 7.8));
EndBody.
"""
        expect = r"""6.8000007"""
        self.assertTrue(TestCodeGen.test(input, expect, 523))


    def test_25(self):
        input = r"""
Function: main
Body:
    print(string_of_float(1.2 *. 5.4));
EndBody.
"""
        expect = r"""6.4800005"""
        self.assertTrue(TestCodeGen.test(input, expect, 524))


    def test_26(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123 \. 2));
EndBody.
"""
        expect = r"""61.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 525))


    def test_27(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123 \. 2));
EndBody.
"""
        expect = r"""61.5"""
        self.assertTrue(TestCodeGen.test(input, expect, 526))


    def test_28(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123 \. 3 +. 46 \. 5 \. 1 \. 1 \. 1 \. 2 \. 4));
EndBody.
"""
        expect = r"""42.15"""
        self.assertTrue(TestCodeGen.test(input, expect, 527))


    def test_29(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123 \. 2.3));
EndBody.
"""
        expect = r"""53.478264"""
        self.assertTrue(TestCodeGen.test(input, expect, 528))


    def test_30(self):
        input = r"""
Function: main
Body:
    print(string_of_float(123.1 \. 5 +. 123 \. 5.1 -. (123 *. 5.1 +. 123.1 *. 5) -. 123 \. (123 \. 123 *. 123 +. 1) -. 123.123 *. 321.213 -. 1));
EndBody.
"""
        expect = r"""-40744.766"""
        self.assertTrue(TestCodeGen.test(input, expect, 529))


    def test_31(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(True && False));
EndBody.
"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 530))


    def test_32(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(False || True));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 531))


    def test_33(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(False || True && True));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 532))


    def test_34(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(False || True && False || (False && True)));
EndBody.
"""
        expect = r"""false"""
        self.assertTrue(TestCodeGen.test(input, expect, 533))


    def test_35(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(False || True && False || (False || True)));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 534))


    def test_36(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(1 > 2));
    print(string_of_bool(1 < 2));
    print(string_of_bool(1 == 2));
    print(string_of_bool(1 >= 2));
    print(string_of_bool(1 <= 2));
    print(string_of_bool(1 != 2));
EndBody.
"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 535))


    def test_37(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(2 > 2));
    print(string_of_bool(2 < 2));
    print(string_of_bool(2 == 2));
    print(string_of_bool(2 >= 2));
    print(string_of_bool(2 <= 2));
    print(string_of_bool(2 != 2));
EndBody.
"""
        expect = r"""falsefalsetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 536))


    def test_38(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(3 > 2));
    print(string_of_bool(3 < 2));
    print(string_of_bool(3 == 2));
    print(string_of_bool(3 >= 2));
    print(string_of_bool(3 <= 2));
    print(string_of_bool(3 != 2));
EndBody.
"""
        expect = r"""truefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 537))


    def test_39(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(1.0 >. 2.0));
    print(string_of_bool(1 <. 2.));
    print(string_of_bool(1. >=. 2));
    print(string_of_bool(1 <=. 2));
    print(string_of_bool(1 =/= 2));
EndBody.
"""
        expect = r"""falsetruefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 538))


    def test_40(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(1.9 >. 2));
    print(string_of_bool(1.9 <. 2));
    print(string_of_bool(1.9 >=. 2));
    print(string_of_bool(1.0 <=. 2));
    print(string_of_bool(1.9 =/= 2));
EndBody.
"""
        expect = r"""falsetruefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 539))


    def test_41(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(2.1 >. 2));
    print(string_of_bool(2.1 <. 2));
    print(string_of_bool(2.1 >=. 2));
    print(string_of_bool(2.1 <=. 2));
    print(string_of_bool(2.1 =/= 2));
EndBody.
"""
        expect = r"""truefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 540))


    def test_42(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(2. >. 2));
    print(string_of_bool(2 <. 2.));
    print(string_of_bool(2.0 >=. 2.0));
    print(string_of_bool(2. <=. 2.));
    print(string_of_bool(2 =/= 2));
EndBody.
"""
        expect = r"""falsefalsetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 541))


    def test_43(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(2.1 >. 2.1));
    print(string_of_bool(2.1 <. 2.1));
    print(string_of_bool(2.1 >=. 2.1));
    print(string_of_bool(2.1 <=. 2.1));
    print(string_of_bool(2.1 =/= 2.1));
EndBody.
"""
        expect = r"""falsefalsetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 542))


    def test_44(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(2 >. 2.1));
    print(string_of_bool(2 <. 2.1));
    print(string_of_bool(2 >=. 2.1));
    print(string_of_bool(2 <=. 2.1));
    print(string_of_bool(2 =/= 2.1));
EndBody.
"""
        expect = r"""falsetruefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))


    def test_45(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(1 + 2 > 3));
    print(string_of_bool(1 + 2 < 3));
    print(string_of_bool(1 + 2 == 3));
    print(string_of_bool(1 + 2 >= 3));
    print(string_of_bool(1 + 2 <= 3));
    print(string_of_bool(1 + 2 != 3));
EndBody.
"""
        expect = r"""falsefalsetruetruetruefalse"""
        self.assertTrue(TestCodeGen.test(input, expect, 544))


    def test_46(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(1.5 +. 2 >. 3));
    print(string_of_bool(1.5 +. 2 <. 3));
    print(string_of_bool(1.5 +. 2 == 3));
    print(string_of_bool(1.5 +. 2 >=. 3));
    print(string_of_bool(1.5 +. 2 <=. 3));
    print(string_of_bool(1.5 +. 2 =/= 3));
EndBody.
"""
        expect = r"""truefalsefalsetruefalsetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 545))


    def test_47(self):
        input = r"""
Function: main
Body:
    ** 1.5*.2 +. 2 -. 5.3*.2.1 = -6.13 **
    ** 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1 = 16.94 **
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 >. 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 <. 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 == 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 >=. 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 <=. 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 =/= 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
EndBody.
"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 546))


    def test_48(self):
        input = r"""
Function: main
Body:
    ** 1.5*.2 +. 2 -. 5.3*.2.1 = -6.13 **
    ** 3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1 = 16.94 **
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1) >. 0));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1) <. 0));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1) == 0));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1) >=. 0));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1) <=. 0));
    print(string_of_bool(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1) =/= 0));
EndBody.
"""
        expect = r"""falsetruefalsefalsetruetrue"""
        self.assertTrue(TestCodeGen.test(input, expect, 547))


    def test_49(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(5 % 4));
    printStrLn(string_of_int(15 % 4));
    printStrLn(string_of_int(52 % 6));
    printStrLn(string_of_int(56 % 5));
    printStrLn(string_of_int(9 % 12));
    printStrLn(string_of_int(2000 % 46));
    printStrLn(string_of_int(2000 % 54));
    printStrLn(string_of_int(2000 % 87));
EndBody.
"""
        expect = r"""1
3
4
1
9
22
2
86
"""
        self.assertTrue(TestCodeGen.test(input, expect, 548))


    def test_50(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(5 \ 4));
    printStrLn(string_of_int(15 \ 4));
    printStrLn(string_of_int(52 \ 6));
    printStrLn(string_of_int(56 \ 5));
    printStrLn(string_of_int(9 \ 12));
    printStrLn(string_of_int(2000 \ 46));
    printStrLn(string_of_int(2000 \ 54));
    printStrLn(string_of_int(2000 \ 87));
EndBody.
"""
        expect = r"""1
3
8
11
0
43
37
22
"""
        self.assertTrue(TestCodeGen.test(input, expect, 549))


    def test_51(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_float(5 \. 4));
    printStrLn(string_of_float(15 \. 4));
    printStrLn(string_of_float(52 \. 6));
    printStrLn(string_of_float(56 \. 5));
    printStrLn(string_of_float(9 \. 12));
EndBody.
"""
        expect = r"""1.25
3.75
8.666667
11.2
0.75
"""
        self.assertTrue(TestCodeGen.test(input, expect, 550))


    def test_52(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_float(1.5*.2 +. 2 -. 5.3*.2.1));
    printStrLn(string_of_float(3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1));
    printStrLn(string_of_float(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1)));
EndBody.
"""
        expect = r"""-6.13
16.942858
-23.072857
"""
        self.assertTrue(TestCodeGen.test(input, expect, 551))


    def test_53(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(1));
    printLn();
    printLn();
    printLn();
    printLn();
    print(string_of_int(2));
EndBody.
"""
        expect = r"""1




2"""
        self.assertTrue(TestCodeGen.test(input, expect, 552))


    def test_54(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(1000));
    printLn();
    printLn();
    printLn();
    printLn();
    print(string_of_int(2000));
EndBody.
"""
        expect = r"""1000




2000"""
        self.assertTrue(TestCodeGen.test(input, expect, 553))


    def test_55(self):
        input = r"""
Function: main
Body:
    print("Hello World");
EndBody.
"""
        expect = r"""Hello World"""
        self.assertTrue(TestCodeGen.test(input, expect, 554))


    def test_56(self):
        input = r"""
Function: main
Body:
    printStrLn("Hello World 1");
    printStrLn("Hello World 2");
    printStrLn("3");
    printStrLn("4.5");
    printStrLn("-0.6");
EndBody.
"""
        expect = r"""Hello World 1
Hello World 2
3
4.5
-0.6
"""
        self.assertTrue(TestCodeGen.test(input, expect, 555))


    def test_57(self):
        input = r"""
Function: main
Body:
    printStrLn("Error: A JNI error has occurred, please check your installation and try again\nException in thread \'main\' java.lang.VerifyError: (class: MPClass, method: main signature: ([Ljava/lang/String;)V) Illegal type in constant pool");
EndBody.
"""
        expect = r"""Error: A JNI error has occurred, please check your installation and try again
Exception in thread 'main' java.lang.VerifyError: (class: MPClass, method: main signature: ([Ljava/lang/String;)V) Illegal type in constant pool
"""
        self.assertTrue(TestCodeGen.test(input, expect, 556))


    def test_58(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(-1));
    printStrLn(string_of_int(-100));
    printStrLn(string_of_float(-.1.0));
    printStrLn(string_of_float(-.10));
    printStrLn(string_of_float(-.10000.0));
EndBody.
"""
        expect = r"""-1
-100
-1.0
-10.0
-10000.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 557))


    def test_59(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(--1));
    printStrLn(string_of_int(--100));
    printStrLn(string_of_float(-.-.1.0));
    printStrLn(string_of_float(-.-.10000.0));
    printStrLn(string_of_int(---1));
    printStrLn(string_of_int(---100));
    printStrLn(string_of_float(-.-.-.1.0));
    printStrLn(string_of_float(-.-.-.10000.0));
EndBody.
"""
        expect = r"""1
100
1.0
10000.0
-1
-100
-1.0
-10000.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 558))


    def test_60(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_float(-.(1.5*.2 +. 2 -. 5.3*.2.1 -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1))));
    printStrLn(string_of_float(-.(1.5*.2 +. 2 -. 5.3*.2.1) -. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1)));
    printStrLn(string_of_float(-.-.(1.5*.2 +. 2 -. 5.3*.2.1) -.-.-. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1)));
    printStrLn(string_of_float(-.(-.(-.(-.(1.5*.2 +. 2 -. 5.3*.2.1)))) -.-.-.-. (3*.5 +. 2*.3\.2 -. 4*.7.2\.14 +. 1)));
EndBody.
"""
        expect = r"""23.072857
-10.812858
-23.072857
10.812858
"""
        self.assertTrue(TestCodeGen.test(input, expect, 559))


    def test_61(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_bool(!False));
    printStrLn(string_of_bool(!True));
    printStrLn(string_of_bool(!!False));
    printStrLn(string_of_bool(!!True));
    printStrLn(string_of_bool(!!!False));
    printStrLn(string_of_bool(!!!True));
    printStrLn(string_of_bool(!False && True));
    printStrLn(string_of_bool(!True && False));
    printStrLn(string_of_bool(!!False && !!!True || False && True));
    printStrLn(string_of_bool(!!True || False));
EndBody.
"""
        expect = r"""true
false
false
true
true
false
true
false
false
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 560))


    def test_62(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_bool(True && False));
    printStrLn(string_of_bool(False && True));
    printStrLn(string_of_bool(True && (False && True)));
    printStrLn(string_of_bool(True && (False && True) && False));
    printStrLn(string_of_bool(True || False));
    printStrLn(string_of_bool(False || True));
    printStrLn(string_of_bool(True || (False || True)));
    printStrLn(string_of_bool(True || (False || True) || False));
EndBody.
"""
        expect = r"""false
false
false
false
true
true
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 561))


    def test_63(self):
        input = r"""
Function: main
Body:
    print(string_of_bool(False || False || True && (True || False) && (False || True)));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 562))


    def test_64(self):
        input = r"""
Function: main
Body:
    Var: a = 1;
    Var: b = 2;
    printStrLn(string_of_int(a));
    a = b;
    printStrLn(string_of_int(b));
    printStrLn(string_of_int(a));
    a = b + 1;
    printStrLn(string_of_int(a));
EndBody.
"""
        expect = r"""1
2
2
3
"""
        self.assertTrue(TestCodeGen.test(input, expect, 563))


    def test_65(self):
        input = r"""
Function: main
Body:
    Var: a = 1.0;
    Var: b = 2.0;
    printStrLn(string_of_float(a));
    a = b;
    printStrLn(string_of_float(b));
    printStrLn(string_of_float(a));
    a = b +. 1;
    printStrLn(string_of_float(a));
EndBody.
"""
        expect = r"""1.0
2.0
2.0
3.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 564))


    def test_66(self):
        input = r"""
Function: main
Body:
    Var: a = 1.0;
    Var: b = 2.0;
    printStrLn(string_of_float(a));
    printStrLn(string_of_float(b));
    a = b *. 0;
    printStrLn(string_of_float(a));
EndBody.
"""
        expect = r"""1.0
2.0
0.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 565))


    def test_67(self):
        input = r"""
Function: main
Body:
    Var: a=0.0, b=0.0, x=0, y=0;
    a = 1.05 *. 25.4;
    b = 2.05 +. a;
    printStrLn(string_of_float(a));
    printStrLn(string_of_float(b));
    a = a +. 100 -. b;
    printStrLn(string_of_float(a));
    x = 1000;
    y = 1;
    x = x + y * 1000 \ 5;
    printStrLn(string_of_int(x));
    printStrLn(string_of_int(y));
    y = x * y + x * 2 + 2 * x - y * 2 + 2 * y;
    printStrLn(string_of_int(y));
    x = x * y * 2 * 5;
    printStrLn(string_of_int(x));
    a = (a *. b +. x) \. y +. y \. (a *. b +. 2 % x);
    printStrLn(string_of_float(a));
EndBody.
"""
        expect = r"""26.669998
28.719997
97.95
1200
1
6000
72000000
12002.601
"""
        self.assertTrue(TestCodeGen.test(input, expect, 566))


    def test_68(self):
        input = r"""
Function: main
Body:
    Var: a="1", b=2, c=0;
    c = int_of_string(a) + b;
    print(string_of_int(c));
EndBody.
"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input, expect, 567))


    def test_69(self):
        input = r"""
Function: main
Body:
    Var: a=5., b=2., c=0.;
    b = a +. b \. 2 +. 1;
    a = b;
    printStrLn(string_of_float(a));
    printStrLn(string_of_float(b));
    b = (a +. b) \. 4 +. (a -. b) \. 4 *. 2 +. 1;
    a = b;
    c = a;
    printStrLn(string_of_float(a));
    printStrLn(string_of_float(b));
    printStrLn(string_of_float(c));
EndBody.
"""
        expect = r"""7.0
7.0
4.5
4.5
4.5
"""
        self.assertTrue(TestCodeGen.test(input, expect, 568))


    def test_70(self):
        input = r"""
Function: main
Body:
    Var: a=5., b=2., c=1000;
    b = c +. 1;
    a = b;
    printStrLn(string_of_float(a));
    printStrLn(string_of_float(a));
    printStrLn(string_of_int(c));
EndBody.
"""
        expect = r"""1001.0
1001.0
1000
"""
        self.assertTrue(TestCodeGen.test(input, expect, 569))


    def test_71(self):
        input = r"""
Function: main
Body:
    Var: a = 5.2;
    print(string_of_int(int_of_float(a)));
EndBody.
"""
        expect = r"""5"""
        self.assertTrue(TestCodeGen.test(input, expect, 570))


    def test_72(self):
        input = r"""
Function: main
Body:
    Var: a = 5;
    printStrLn(string_of_int(a));
    printStrLn(string_of_float(float_to_int(a)));
    printStrLn(string_of_float(a +. 5.0));
EndBody.
"""
        expect = r"""5
5.0
10.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 571))


    def test_73(self):
        input = r"""
Function: foo
Body:
    Return 100;
EndBody.

Function: main
Body:
    print(string_of_int(foo()));
EndBody.
"""
        expect = r"""100"""
        self.assertTrue(TestCodeGen.test(input, expect, 572))


    def test_74(self):
        input = r"""
Function: foo
Body:
    Var: a = 1000;
    Return a;
EndBody.

Function: main
Body:
    print(string_of_int(foo()));
EndBody.
"""
        expect = r"""1000"""
        self.assertTrue(TestCodeGen.test(input, expect, 573))


    def test_75(self):
        input = r"""
Function: main
Body:
    printStrLn(string_of_int(fi()));
    printStrLn(string_of_float(ff()));
    printStrLn(string_of_bool(fb()));
EndBody.

Function: fi
Body:
    Return 1;
EndBody.
Function: ff
Body:
    Return 5.0;
EndBody.
Function: fb
Body:
    Return False;
EndBody.
"""
        expect = r"""1
5.0
false
"""
        self.assertTrue(TestCodeGen.test(input, expect, 574))


    def test_76(self):
        input = r"""
Function: main
Body:
    Var: a = 0;
    a = foo(3, 2);
    print(string_of_int(a));
EndBody.
Function: foo
Parameter: a, b
Body:
    Return (a + b) \ 2;
EndBody.
"""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input, expect, 575))


    def test_77(self):
        input = r"""
Function: main
Body:
    Var: a=0.;
    a = foo(2., False);
    print(string_of_float(a));
EndBody.
Function: foo
Parameter: a, b
Body:
    Return a*.a*.a +. a\.2;
EndBody.
"""
        expect = r"""9.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 576))


    def test_78(self):
        input = r"""
Var: a;
Function: main
Body:
    a = 100;
    print(string_of_int(a));
EndBody.
"""
        expect = r"""100"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))


    def test_79(self):
        input = r"""
Var: a;
Function: main
Body:
    Var: a = 100;
    printStrLn(string_of_int(a));
    a = foo();
    printStrLn(string_of_int(a));
    bar();
EndBody.
Function: foo
Body:
    a = 10;
    Return a * 5;
EndBody.
Function: bar
Body:
    printStrLn(string_of_int(a));
EndBody.
"""
        expect = r"""100
50
10
"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))


    def test_80(self):
        input = r"""
Var: a=0.;
Function: main
Body:
    Var: a = 100.;
    printStrLn(string_of_float(a));
    a = foo();
    printStrLn(string_of_float(a));
    bar();
EndBody.
Function: foo
Body:
    a = 10.;
    Return a *. 5;
EndBody.
Function: bar
Body:
    printStrLn(string_of_float(a));
EndBody.
"""
        expect = r"""100.0
50.0
10.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))


    def test_81(self):
        input = r"""
Var: a;
Function: main
Body:
    Var: a;
    a = 10 < 5;
    printStrLn(string_of_bool(a));
    a = foo();
    printStrLn(string_of_bool(a));
    bar();
EndBody.
Function: foo
Body:
    a = 10 > 5;
    Return a || True;
EndBody.
Function: bar
Body:
    printStrLn(string_of_bool(a));
EndBody.
"""
        expect = r"""false
true
true
"""
        self.assertTrue(TestCodeGen.test(input, expect, 580))


    def test_82(self):
        input = r"""
Function: main
Body:
    If 1 == 2 Then
        print(string_of_int(100));
    Else
        print(string_of_int(300));
    EndIf.
EndBody.
"""
        expect = r"""300"""
        self.assertTrue(TestCodeGen.test(input, expect, 581))


    def test_83(self):
        input = r"""
Function: main
Body:
    If True Then
        print(string_of_int(100));
    ElseIf True Then
        print(string_of_int(200));
    Else
        print(string_of_int(300));
    EndIf.

    If False Then
        print(string_of_int(100));
    ElseIf True Then
        print(string_of_int(200));
    Else
        print(string_of_int(300));
    EndIf.

    If False Then
        print(string_of_int(100));
    ElseIf False Then
        print(string_of_int(200));
    Else
        print(string_of_int(300));
    EndIf.
EndBody.
"""
        expect = r"""100200300"""
        self.assertTrue(TestCodeGen.test(input, expect, 582))


    def test_84(self):
        input = r"""
Function: main
Body:
    If True Then
        print(string_of_int(100));
        If False Then
            print(string_of_int(100));
        ElseIf True Then
            print(string_of_int(200));
        Else
            print(string_of_int(300));
        EndIf.
    ElseIf True Then
        print(string_of_int(200));
    Else
        print(string_of_int(300));
    EndIf.

    If False Then
        print(string_of_int(100));
    ElseIf True Then
        print(string_of_int(200));
        If False Then
            print(string_of_int(100));
        ElseIf True Then
            print(string_of_int(200));
        Else
            print(string_of_int(300));
        EndIf.
    Else
        print(string_of_int(300));
    EndIf.
EndBody.
"""
        expect = r"""100200200200"""
        self.assertTrue(TestCodeGen.test(input, expect, 583))


    def test_85(self):
        input = r"""
Function: main
Body:
    Var: a = 5;
    While a > 0 Do
        print(string_of_int(a));
        a = a - 1;
    EndWhile.
EndBody.
"""
        expect = r"""54321"""
        self.assertTrue(TestCodeGen.test(input, expect, 584))


    def test_86(self):
        input = r"""
Function: main
Body:
    Var: a = 5;
    While a > 0 Do
        Var: b = 0;
        printStrLn(string_of_int(a));
        a = a - 1;
        While b < a Do
            b = b + 1;
            print(string_of_int(b));
        EndWhile.
        printLn();
    EndWhile.
EndBody.
"""
        expect = r"""5
1234
4
123
3
12
2
1
1

"""
        self.assertTrue(TestCodeGen.test(input, expect, 585))


    def test_87(self):
        input = r"""
Function: main
Body:
    Var: i=0;
    For (i = 1, i <= 5, 1) Do
        print(string_of_int(i));
    EndFor.
EndBody.
"""
        expect = r"""12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))


    def test_88(self):
        input = r"""
Function: main
Body:
    Var: i=0;
    For (i = 1, i <= 5, 1) Do
        print(string_of_int(i));
    EndFor.
    print(string_of_int(i));
EndBody.
"""
        expect = r"""123456"""
        self.assertTrue(TestCodeGen.test(input, expect, 587))


    def test_89(self):
        input = r"""
Function: main
Body:
    Var: i = 0;
    For (i = 1, i <= 5, 1) Do
        print(string_of_int(i));
    EndFor.
    printStrLn(string_of_int(i));

    For (i = 1, i <= 1, 1) Do
        print(string_of_int(i));
    EndFor.
    printStrLn(string_of_int(i));

    For (i = 5, i >= 1, -1) Do
        print(string_of_int(i));
    EndFor.
    printStrLn(string_of_int(i));
EndBody.
"""
        expect = r"""123456
12
543210
"""
        self.assertTrue(TestCodeGen.test(input, expect, 588))


    def test_90(self):
        input = r"""
Function: main
Body:
    Var: arr[6] = {2,6,1,2,0};
    Var: i = 0;
    For(i = 0, i < 6, 1) Do
        print(string_of_int(arr[i]));
    EndFor.
EndBody.
"""
        expect = r"""261200"""
        self.assertTrue(TestCodeGen.test(input, expect, 589))


############################### Test useful program ###############################

    def test_palindrome_string(self):
        input = \
r"""
Function: isPalindrome
Parameter: str[100], size
Body:
    Var: len=0, i=0;
    len = size;
    For(i = 0, i < len \ 2, 1) Do
        If str[i] != str[len - i - 1] Then
            Return False;
        EndIf.
    EndFor.
    Return True;
EndBody.

Function: main
Body:
    Var: str[5] = {1,2,3,2,1};
    print(string_of_bool(isPalindrome(str, 5)));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    def test_prime_number_program_iteration(self):
        input = \
r"""
Function: isPrime
Parameter: n
Body:
    Var: i=0;
    If n <= 1 Then Return False; EndIf.

    For(i = 2, i <= n \ 2, 1) Do
        If n % i == 0 Then
            Return False;
        EndIf.
    EndFor.
    Return True;
EndBody.

Function: main
Body:
    print(string_of_bool(isPrime(7)));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_prime_number_program_recursion(self):
        input = \
r"""
Function: isPrime
Parameter: n, i         ** Default: i = 2 **
Body:
    If n == 2 Then
        Return True;
    ElseIf n < 2 Then
        Return False;
    EndIf.
    
    If n % i == 0 Then
        Return False;
    EndIf.
    
    If i * i > n Then
        Return True;
    EndIf.

    Return isPrime(n, i + 1);
EndBody.

Function: main
Body:
    print(string_of_bool(isPrime(31, 2)));
EndBody.
"""
        expect = r"""true"""
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    def test_factorial_recursion(self):
        input = \
r"""
Function: factorial
Parameter: n
Body:
    If n <= 1 Then
        Return 1;
    Else
        Return n * factorial(n - 1);
    EndIf.
EndBody.

Function: main
Body:
    print(string_of_int(factorial(9)));
EndBody.
"""
        expect = r"""362880"""
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_factorial_iteration(self):
        input = \
r"""
Function: factorial
Parameter: n
Body:
    Var: i=0;
    Var: fact = 1;

    If n <= 1 Then
        Return 1;
    EndIf.
    
    For (i = 1, i <= n, 1) Do
        fact = fact * i;
    EndFor.
    Return fact;
EndBody.

Function: main
Body:
    print(string_of_int(factorial(9)));
EndBody.
"""
        expect = r"""362880"""
        self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    def test_fizzbuzz_program(self):
        input = \
r"""
Function: fizz_buzz
Body:
    Var: i=0;
    For (i = 1, i <= 10, 1) Do
        If i % 15 == 0 Then
            printStrLn("FizzBuzz\t");
        ElseIf i % 3 == 0 Then
            printStrLn("Fizz\t");
        ElseIf i % 5 == 0 Then
            printStrLn("Buzz\t");
        Else
            printStrLn(string_of_int(i));
        EndIf.
    EndFor.
EndBody.

Function: main
Body:
    fizz_buzz();
EndBody.
"""
        expect = r"""1
2
Fizz	
4
Buzz	
Fizz	
7
8
Fizz	
Buzz	
"""
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_blackjack_program(self):
        input = \
r"""
Function: blackjack
Parameter: a, b
Body:
    Var: sum = 0;
    sum = a + b;
    If sum > 21 Then
        If a == 11 Then
            sum = 1 + b;
        ElseIf b == 11 Then
            sum = 1 + a;
        Else
            sum = 0;
        EndIf.
    EndIf.
    Return sum;
EndBody.

Function: main
Body:
    print(string_of_int(blackjack(10, 11)));
EndBody.
"""
        expect = r"""21"""
        self.assertTrue(TestCodeGen.test(input, expect, 596))
    
    def test_search_array(self):
        input = \
r"""
Function: search
Parameter: target
Body:
    Var: idx = 0;
    Var: arr[5] = {2, 4, 6, 8, 10};
    For (idx = 0, idx < 5, 1) Do
        If arr[idx] == target Then
            Return idx;
        EndIf.
    EndFor.
    Return -1;
EndBody.

Function: main
Body:
    print(string_of_int(search(6)));
EndBody.
"""
        expect = r"""2"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    def test_gcd_program(self):
        input = \
r"""
Function: gcd
Parameter: a, b
Body:
    While a != b Do
        If a > b Then
            a = a - b;
        Else
            b = b - a;
        EndIf.
    EndWhile.
    Return a;
EndBody.

Function: main
Body:
    print(string_of_int(gcd(123, 35)));
EndBody.
"""
        expect = r"""1"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_binary_search_program(self):
        input = r"""
Function: binarySearch
Parameter: arr[100], leftIdx, rightIdx, target
Body:
    ** Assume array is sorted **
    Var: mid=0;
    If rightIdx >= leftIdx Then
        mid = leftIdx + (rightIdx - leftIdx) \ 2;

        ** If found target **
        If arr[mid] == target Then
            Return mid;
        EndIf.

        ** Target is at left branch **
        If arr[mid] > target Then
            Return binarySearch(arr, 1, mid - 1, target);
        EndIf.

         ** Target is at right branch **
        Return binarySearch(arr, mid + 1, rightIdx, target);
    EndIf.
    Return -1;
EndBody.

Function: main
Body:
    Var: arr[10] = {1,2,3,4,5,6,7,8,9,10};
    print(string_of_int(binarySearch(arr,0,9,4)));
EndBody.
"""
        expect = r"""3"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))