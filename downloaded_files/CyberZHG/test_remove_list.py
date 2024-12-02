import unittest
from wiki_dump_reader import Cleaner


class TestRemoveLists(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.cleaner = Cleaner()

    def test_remove_lists(self):
        text = "=== 航空 ===\n*[[南昌昌北国际机场]]\n*[[赣州黄金机场]]\n*[[景德镇罗家机场]]\n*[[九江庐山机场]]\n*[[吉" \
               "安井冈山机场]]\n*[[宜春明月山机场]]\n*[[上饶三清山机场]]"
        expected = "=== 航空 ===\n[[南昌昌北国际机场]]\n[[赣州黄金机场]]\n[[景德镇罗家机场]]\n[[九江庐山机场]]\n[[吉安井" \
                   "冈山机场]]\n[[宜春明月山机场]]\n[[上饶三清山机场]]"
        actual = self.cleaner._remove_lists(text)
        self.assertEqual(expected, actual)

        text = "=== 散文 ===\n{{Main article|散文}}\n#[[散文]]是一种没有严格的韵律和篇幅限制的文学形式，与[[韵文]]相对。中国" \
               "的散文从先秦[[诸子散文]]发展而来，代有散文[[名家]][[名作]]。其中历史散文和[[赋]]体以及奏议文告等[[应用文]]体，" \
               "对后代产生了深远影响。\n#[[应用文]]是針對特定需求而有的文體，例如公告、廣告等。\n#[[小品文]]是从作者的观点来讨论" \
               "某一议题。\n#[[文言文]]，常指非八股文的文體。\n#[[骈文]]是句式多為四六句及對仗的文言文文體。\n#[[随笔]]，兼有議" \
               "論和抒情兩種特性的散文。\n#[[笔记]]\n#[[遊记]]"
        expected = "=== 散文 ===\n{{Main article|散文}}\n[[散文]]是一种没有严格的韵律和篇幅限制的文学形式，与[[韵文]]相对。" \
                   "中国的散文从先秦[[诸子散文]]发展而来，代有散文[[名家]][[名作]]。其中历史散文和[[赋]]体以及奏议文告等[[应用" \
                   "文]]体，对后代产生了深远影响。\n[[应用文]]是針對特定需求而有的文體，例如公告、廣告等。\n[[小品文]]是从作者的" \
                   "观点来讨论某一议题。\n[[文言文]]，常指非八股文的文體。\n[[骈文]]是句式多為四六句及對仗的文言文文體。\n[[随笔" \
                   "]]，兼有議論和抒情兩種特性的散文。\n[[笔记]]\n[[遊记]]"
        actual = self.cleaner._remove_lists(text)
        self.assertEqual(expected, actual)
