"""
class ListNode:
	def __init__(self,val):
		self.val = val


n = ListNode(10)
if hasattr(n, 'x'):
	print "Found"
else:
	n.x = 10

print n.x
"""

	nums = [1,1]#[1, 3, 3, 3, 1]#[1, 3, 3, 4, 3, 1]#[1, 3, 2, 2, 2, 3, 4, 3, 1]
	maxI = 0
	maxCont = 1

	startCont = 0
	curMax = 1
	for i in range(1, len(nums)):
		if nums[i] == nums[i-1]:
			curMax += 1
			if curMax > maxCont:
				maxCont = curMax
				maxI = startCont
		else:
			startCont = i
			curMax = 1

	print "Max starts at {0}, and goes for {1}".format(maxI, maxCont)				




[849,61,224,453,433,257,282,93,826,441,164,854,195,506,628,916,197,340,482,305,721,412,542,719,947,333,472,48,514,168,64,362,580,288,814,364,544,448,809,888,972,927,434,830,554,349,26,894,682,966,594,36,540,556,508,587,69,27,651,782,958,290,596,321,185,395,129,258,634,184,67,737,415,11,982,597,692,190,915,335,81,470,842,668,538,868,670,320,825,311,267,497,495,13,626,752,646,430,935,63,24,73,5,426,764,304,967,31,638,400,500,831,419,390,698,88,874,398,679,370,244,691,347,996,688,776,751,657,932,614,14,710,730,317,28,760,306,427,611,136,845,352,284,58,681,90,277,132,126,624,171,253,905,273,443,914,205,408,489,243,293,600,900,720,211,35,564,562,219,848,326,880,767,54,899,531,131,421,784,694,578,949,898,985,875,163,469,455,425,368,526,635,754,442,549,324,641,226,951,520,992,356,242,887,158,663,545,599,605,583,71,119,891,573,610,451,363,892,686,532,296,988,51,344,529,582,940,543,603,836,201,33,135,103,895,346,897,79,955,249,318,238,355,769,615,695,254,953,783,971,325,925,575,125,111,428,566,505,263,648,217,994,886,231,503,593,999,287,521,723,676,473,857,998,716,533,922,795,107,8,174,513,436,285,447,653,630,890,860,484,210,768,203,235,792,270,65,462,673,464,846,101,334,780,286,718,762,175,577,245,138,901,867,571,161,714,280,106,592,778,968,413,420,746,225,153,883,372,62,422,281,265,358,209,206,677,621,181,367,437,978,530,693,683,417,547,183,609,689,463,823,440,861,745,1000,418,620,598,338,34,581,704,110,55,738,595,380,744,45,743,471,817,52,632,815,264,742,222,353,396,765,386,486,360,766,567,980,310,664,404,841,118,906,876,169,800,525,700,893,98,53,859,493,330,528,945,511,173,747,576,758,939,15,725,250,601,302,50,354,116,522,872,402,777,49,30,202,930,40,631,822,796,130,47,82,699,303,25,833,248,678,481,444,384,75,666,127,705,749,948,240,941,991,804,394,452,828,23,636,866,799,633,917,759,665,707,501,608,492,454,411,237,590,541,16,856,862,843,9,476,539,929,586,946,644,684,755,6,260,124,438,516,713,409,728,546,771,753,877,834,697,869,675,165,60,934,289,801,1,896,496,339,100,128,642,827,943,504,154,21,565,309,806,661,660,741,969,824,460,507,379,407,120,990,43,272,918,337,239,331,669,790,152,791,97,658,643,902,750,572,793,327,650,625,855,936,498,458,156,207,727,920,510,445,536,38,230,294,871,708,779,218,908,315,179,873,142,724,524,907,416,802,431,191,76,960,241,385,348,259,187,7,853,923,397,810,359,560,405,952,91,449,973,299,913,485,674,414,266,149,84,942,208,588,993,680,4,392,166,612,839,95,712,619,275,772,702,931,247,818,735,561,711,557,151,864]

{1: [1, 896, 128, 4], 4: [4, 392], 5: [5, 400, 800, 50, 25, 1, 100], 6: [6, 438, 1], 7: [7, 560], 8: [8, 768, 384, 16, 1, 128, 4], 9: [9, 684, 1], 11: [11, 825, 33, 165, 1], 13: [13, 390, 65, 780, 130, 1], 14: [14, 28, 784, 1, 7, 392], 15: [15, 30, 930, 1], 16: [16, 1, 896, 128, 4], 21: [21, 294, 7, 588], 23: [23, 759, 1], 24: [24, 624, 8, 1, 4], 25: [25, 75, 675, 1], 26: [26, 13, 390, 780, 130, 1], 27: [27, 81, 243, 486, 9, 1], 28: [28, 784, 1, 7, 392], 30: [30, 930, 6, 1], 31: [31, 899, 1], 33: [33, 231, 462, 1], 34: [34, 476, 1, 952], 35: [35, 875, 175, 1, 7], 36: [36, 540, 9, 1], 38: [38, 76], 40: [40, 240, 1, 120, 960, 4], 43: [43], 45: [45, 765, 15, 1], 47: [47, 705, 1], 48: [48, 288, 24, 8, 576, 1, 4], 49: [49, 833, 1, 7], 50: [50, 25, 1, 100], 51: [51, 867, 1], 52: [52, 260, 1, 4], 53: [53, 636, 1], 54: [54, 324, 648, 9, 1], 55: [55, 330, 165, 1, 660], 58: [58, 754, 1], 60: [60, 1, 660, 4], 61: [61, 854, 427, 1], 62: [62, 620, 310, 1], 63: [63, 126, 630, 9, 1], 64: [64, 448, 8, 16, 1, 896, 4], 65: [65, 780, 130, 260, 1], 67: [67, 737, 1], 69: [69, 897, 23, 1], 71: [71, 355, 1], 73: [73, 657, 219, 1], 75: [75, 675, 1], 76: [76, 4], 79: [79, 632, 1], 81: [81, 243, 486, 9, 1], 82: [82, 492, 1], 84: [84, 588, 4], 88: [88, 352, 8, 704, 1, 4], 90: [90, 900, 45, 15, 1], 91: [91], 93: [93, 651, 31, 1], 95: [95], 97: [97, 873], 98: [98, 49, 1, 294, 7, 588], 100: [100, 4], 101: [101, 404, 202, 1], 103: [103, 206, 1, 824], 106: [106, 530, 53, 1], 107: [107, 749, 1], 110: [110, 55, 330, 1, 660], 111: [111, 999, 1], 116: [116, 1, 348, 4], 118: [118, 354, 1, 708], 119: [119, 238, 714, 1, 7], 120: [120, 960, 4], 124: [124, 1, 496, 4], 125: [125, 1000, 250, 25, 1], 126: [126, 630, 9, 1], 127: [127, 1], 128: [128, 4], 129: [129, 258, 516, 1, 43], 130: [130, 260, 1], 131: [131, 917, 1], 132: [132, 33, 792, 264, 1], 135: [135, 270, 45, 15, 1, 810], 136: [136, 408, 8, 1, 4], 138: [138, 828, 23, 1, 414], 142: [142], 149: [149], 151: [151], 152: [152, 38, 76], 153: [153, 765, 9, 1], 154: [154, 7], 156: [156, 4], 158: [158, 79, 632, 1], 161: [161, 23, 644, 1], 163: [163, 978, 1], 164: [164, 82, 492, 1], 165: [165, 1, 660], 166: [166], 168: [168, 24, 8, 1, 504, 4], 169: [169, 1, 507], 171: [171, 513, 9, 1], 173: [173, 1], 174: [174, 522, 6, 1], 175: [175, 525, 25, 1], 179: [179], 181: [181, 1, 724], 183: [183, 1], 184: [184, 368, 8, 1, 4], 185: [185, 5, 370, 1], 187: [187, 561], 190: [190, 5, 760, 380, 1, 95], 191: [191], 195: [195, 13, 390, 65, 780, 1], 197: [197, 985, 1], 201: [201, 402, 804, 1], 202: [202, 1], 203: [203, 609, 1, 7], 205: [205, 615, 1], 206: [206, 1, 824], 207: [207, 414], 208: [208, 4], 209: [209, 418, 1], 210: [210, 420, 15, 30, 1], 211: [211, 422, 1], 217: [217, 1, 7], 218: [218], 219: [219, 876, 438, 1], 222: [222, 444, 6, 1], 224: [224, 448, 14, 28, 1, 896, 7], 225: [225, 45, 15, 675, 1], 226: [226, 678, 1], 230: [230], 231: [231, 462, 1, 21, 7], 235: [235, 47, 705, 1], 237: [237, 1, 711], 238: [238, 714, 34, 1], 239: [239], 240: [240, 16, 1, 960, 4], 241: [241], 242: [242, 484, 968, 1], 243: [243, 486, 9, 1], 244: [244, 1, 4], 245: [245, 980, 49, 1, 7], 247: [247], 248: [248, 124, 1, 496, 4], 249: [249, 747, 1], 250: [250, 50, 25, 1, 750], 253: [253, 23, 759, 1], 254: [254, 762, 127, 1], 257: [257, 514, 1], 258: [258, 6, 516, 1], 259: [259, 7], 260: [260, 1, 4], 263: [263, 1], 264: [264, 528, 6, 1], 265: [265, 530, 53, 1], 266: [266], 267: [267, 801, 1], 270: [270, 45, 15, 1, 810], 272: [272, 4], 273: [273, 546, 1, 21, 7], 275: [275], 277: [277, 1], 280: [280, 40, 1, 560, 4], 281: [281, 843, 1], 282: [282, 564, 47, 1], 284: [284, 71, 1, 142], 285: [285, 15, 1, 855], 286: [286, 1, 572], 287: [287, 861, 1, 7], 288: [288, 36, 576, 9, 1], 289: [289, 1], 290: [290, 5, 1], 293: [293, 586, 1], 294: [294, 7, 588], 296: [296, 8, 592, 1, 4], 299: [299], 302: [302, 1, 151], 303: [303, 1], 304: [304, 8, 608, 16, 1, 4], 305: [305, 915, 5, 1], 306: [306, 51, 153, 1, 918], 309: [309], 310: [310, 930, 1], 311: [311, 1], 315: [315, 7], 317: [317, 951, 1], 318: [318, 106, 53, 636, 1], 320: [320, 5, 40, 1, 960], 321: [321, 107, 1, 642], 324: [324, 648, 9, 1], 325: [325, 65, 1, 650], 326: [326, 163, 978, 1], 327: [327], 330: [330, 15, 30, 1, 660], 331: [331, 993], 333: [333, 111, 999, 1], 334: [334, 1], 335: [335, 670, 5, 1], 337: [337, 674], 338: [338, 169, 1], 339: [339], 340: [340, 5, 1, 680], 344: [344, 8, 1, 4], 346: [346, 173, 1], 347: [347, 694, 1], 348: [348, 4], 349: [349, 698, 1], 352: [352, 8, 704, 16, 1, 4], 353: [353, 1], 354: [354, 6, 1, 708], 355: [355, 1], 356: [356, 1, 4, 712], 358: [358, 1, 179], 359: [359], 360: [360, 15, 30, 60, 1, 120], 362: [362, 181, 1, 724], 363: [363, 33, 1], 364: [364, 26, 13, 52, 728, 1], 367: [367, 1], 368: [368, 8, 16, 1, 4], 370: [370, 1], 372: [372, 62, 744, 124, 1], 379: [379], 380: [380, 1, 38, 76], 384: [384, 16, 1, 128, 4], 385: [385, 7], 386: [386, 1, 772], 390: [390, 65, 780, 130, 1], 392: [392], 394: [394, 1], 395: [395, 5, 1, 790], 396: [396, 9, 1], 397: [397], 398: [398, 796, 1], 400: [400, 8, 800, 40, 1, 4], 402: [402, 804, 6, 1], 404: [404, 202, 1], 405: [405], 407: [407], 408: [408, 51, 1], 409: [409, 1, 818], 411: [411, 1], 412: [412, 103, 206, 1, 824], 413: [413, 1, 7], 414: [414], 415: [415, 5, 1], 416: [416, 208, 4], 417: [417, 834, 1], 418: [418, 1, 38], 419: [419, 1], 420: [420, 15, 30, 60, 1], 421: [421, 1], 422: [422, 1], 425: [425, 25, 1], 426: [426, 71, 1, 142], 427: [427, 1, 7], 428: [428, 107, 856, 1], 430: [430, 5, 860, 1], 431: [431], 433: [433, 866, 1], 434: [434, 868, 31, 217, 1], 436: [436, 872, 1, 218], 437: [437, 23, 1], 438: [438, 1], 440: [440, 110, 55, 1], 441: [441, 63, 9, 1], 442: [442, 34, 1], 443: [443, 886, 1], 444: [444, 6, 1], 445: [445], 447: [447, 1, 149], 448: [448, 14, 28, 1, 896, 7], 449: [449], 451: [451, 1, 902], 452: [452, 1, 4], 453: [453, 906, 1, 151], 454: [454, 1, 908], 455: [455, 65, 1], 458: [458], 460: [460, 920, 230], 462: [462, 6, 1], 463: [463, 1], 464: [464, 116, 1, 4], 469: [469, 1, 7], 470: [470, 5, 940, 235, 1], 471: [471, 1, 942], 472: [472, 8, 1, 4], 473: [473, 946, 1, 43], 476: [476, 1, 7, 952], 481: [481, 1], 482: [482, 1, 241], 484: [484, 968, 1, 4], 485: [485], 486: [486, 9, 1], 489: [489, 163, 978, 1], 492: [492, 6, 1], 493: [493, 1], 495: [495, 5, 55, 165, 1, 990], 496: [496, 4], 497: [497, 71, 994, 1], 498: [498, 166], 500: [500, 125, 1000, 250, 25, 1], 501: [501, 1], 503: [503, 1], 504: [504, 21, 7, 84], 505: [505, 101, 1], 506: [506, 11, 253, 1], 507: [507], 508: [508, 254, 127, 1], 510: [510], 511: [511, 1, 7], 513: [513, 9, 1], 514: [514, 1], 516: [516, 1, 43], 520: [520, 8, 40, 1, 4], 521: [521, 1], 522: [522, 9, 1], 524: [524, 4], 525: [525, 15, 75, 1], 526: [526, 263, 1], 528: [528, 16, 1, 4], 529: [529, 23, 1], 530: [530, 53, 1], 531: [531, 9, 1], 532: [532, 1, 38, 76], 533: [533, 1], 536: [536, 4], 538: [538, 1], 539: [539, 1, 7], 540: [540, 27, 54, 270, 9, 1], 541: [541, 1], 542: [542, 1], 543: [543, 181, 1], 544: [544, 136, 8, 1, 272, 4], 545: [545, 1], 546: [546, 1, 21, 7], 547: [547, 1], 549: [549, 183, 1], 554: [554, 277, 1], 556: [556, 1, 4], 557: [557], 560: [560, 4], 561: [561], 562: [562, 281, 1], 564: [564, 47, 1], 565: [565], 566: [566, 1], 567: [567, 9, 1], 571: [571, 1], 572: [572, 4], 573: [573, 1, 191], 575: [575, 25, 1], 576: [576, 16, 1, 4], 577: [577, 1], 578: [578, 34, 1], 580: [580, 290, 5, 1], 581: [581, 1, 7], 582: [582, 6, 1], 583: [583, 53, 1], 586: [586, 1], 587: [587, 1], 588: [588, 4], 590: [590, 1], 592: [592, 16, 1, 4], 593: [593, 1], 594: [594, 27, 54, 9, 1], 595: [595, 1, 7], 596: [596, 1, 149], 597: [597, 1], 598: [598, 23, 1, 299], 599: [599, 1], 600: [600, 8, 40, 1, 120, 4], 601: [601, 1], 603: [603, 201, 1], 605: [605, 55, 1], 608: [608, 16, 1, 4], 609: [609, 1, 21, 7], 610: [610, 1], 611: [611, 47, 1], 612: [612], 614: [614, 1], 615: [615, 15, 1], 619: [619], 620: [620, 310, 1], 621: [621, 23, 1, 207], 624: [624, 8, 16, 1, 208, 4], 625: [625], 626: [626, 1], 628: [628, 1, 4], 630: [630, 210, 15, 30, 1], 631: [631, 1], 632: [632, 1, 4], 633: [633, 1], 634: [634, 317, 1], 635: [635, 127, 1], 636: [636, 6, 1], 638: [638, 58, 1], 641: [641, 1], 642: [642], 643: [643], 644: [644, 1, 7], 646: [646, 34, 1], 648: [648, 8, 1, 4], 650: [650], 651: [651, 31, 217, 1], 653: [653, 1], 657: [657, 219, 1], 658: [658, 7], 660: [660, 4], 661: [661], 663: [663, 51, 1], 664: [664, 1, 4], 665: [665, 1, 7], 666: [666, 9, 1], 668: [668, 334, 1], 669: [669], 670: [670, 5, 1], 673: [673, 1], 674: [674], 675: [675, 1], 676: [676, 338, 169, 1], 677: [677, 1], 678: [678, 6, 1], 679: [679, 1, 97], 680: [680, 4], 681: [681, 1], 682: [682, 11, 1], 683: [683, 1], 684: [684, 6, 1], 686: [686, 98, 49, 1, 7], 688: [688, 344, 8, 1, 4], 689: [689, 53, 1], 691: [691, 1], 692: [692, 346, 173, 1], 693: [693, 9, 1], 694: [694, 1], 695: [695, 1], 697: [697, 1], 698: [698, 1], 699: [699, 1], 700: [700, 50, 25, 1, 100], 702: [702], 704: [704, 16, 1, 4], 705: [705, 1], 707: [707, 1, 7], 708: [708, 4], 710: [710, 71, 355, 1], 711: [711], 712: [712], 713: [713, 1], 714: [714, 34, 1], 716: [716, 358, 1, 179], 718: [718, 1, 359], 719: [719, 1], 720: [720, 8, 360, 40, 1, 120, 4], 721: [721, 103, 1], 723: [723, 1, 241], 724: [724, 4], 725: [725, 25, 1], 727: [727], 728: [728, 1, 7, 91], 730: [730, 1], 735: [735], 737: [737, 11, 1], 738: [738, 82, 1], 741: [741, 247], 742: [742, 53, 1], 743: [743, 1], 744: [744, 248, 124, 1, 4], 745: [745, 1, 149], 746: [746, 1], 747: [747, 9, 1], 749: [749, 1, 7], 750: [750], 751: [751, 1], 752: [752, 8, 16, 1, 4], 753: [753, 1], 754: [754, 1], 755: [755, 1, 151], 758: [758, 1, 379], 759: [759, 1], 760: [760, 8, 40, 1, 4], 762: [762, 127, 1], 764: [764, 1, 191], 765: [765, 15, 1], 766: [766, 1], 767: [767, 1], 768: [768, 384, 16, 1, 128, 4], 769: [769, 1], 771: [771, 1], 772: [772], 776: [776, 8, 1, 4], 777: [777, 1, 21, 7], 778: [778, 1], 779: [779], 780: [780, 52, 260, 1, 4], 782: [782, 34, 1], 783: [783, 9, 1], 784: [784, 8, 16, 1, 4], 790: [790], 791: [791, 7], 792: [792, 264, 6, 1], 793: [793], 795: [795, 265, 53, 1], 796: [796, 1, 4], 799: [799, 1], 800: [800, 50, 25, 1, 100], 801: [801, 1], 802: [802], 804: [804, 6, 1], 806: [806], 809: [809, 1], 810: [810, 405], 814: [814, 11, 1, 407], 815: [815, 1], 817: [817, 1, 43], 818: [818], 822: [822, 411, 1], 823: [823, 1], 824: [824, 4], 825: [825, 5, 55, 165, 1], 826: [826, 14, 1, 7], 827: [827], 828: [828, 23, 1, 207, 414], 830: [830, 415, 5, 1], 831: [831, 277, 1], 833: [833, 1, 7], 834: [834, 1], 836: [836, 209, 418, 1], 839: [839], 841: [841, 1], 842: [842, 421, 1], 843: [843, 1], 845: [845, 65, 1], 846: [846, 47, 1], 848: [848, 8, 16, 1, 4], 849: [849, 1], 853: [853], 854: [854, 14, 1, 7], 855: [855, 95], 856: [856, 1, 4], 857: [857, 1], 859: [859, 1], 860: [860, 1, 43], 861: [861, 1, 21, 7], 862: [862, 1, 431], 864: [864], 866: [866, 1], 867: [867, 289, 1], 868: [868, 31, 217, 1], 869: [869, 1], 871: [871], 872: [872, 1, 218], 873: [873], 874: [874, 437, 23, 1], 875: [875, 125, 25, 1], 876: [876, 6, 438, 1], 877: [877, 1], 880: [880, 8, 440, 40, 1, 4], 883: [883, 1], 886: [886, 1], 887: [887, 1], 888: [888, 24, 8, 1, 4], 890: [890, 1, 445], 891: [891, 33, 1], 892: [892, 1, 4], 893: [893, 47, 1], 894: [894, 447, 1, 149], 895: [895, 1, 179], 896: [896, 128, 4], 897: [897, 23, 1, 299], 898: [898, 1, 449], 899: [899, 1], 900: [900, 225, 45, 15, 1], 901: [901, 53, 1], 902: [902], 905: [905, 181, 1], 906: [906, 302, 1, 151], 907: [907], 908: [908, 4], 913: [913], 914: [914, 1], 915: [915, 5, 15, 1], 916: [916, 1, 458], 917: [917, 1, 7], 918: [918], 920: [920, 230], 922: [922, 1], 923: [923], 925: [925, 25, 1], 927: [927, 103, 1, 309], 929: [929, 1], 930: [930, 6, 1], 931: [931], 932: [932, 1, 4], 934: [934, 1], 935: [935, 5, 55, 1], 936: [936, 156, 4], 939: [939, 1], 940: [940, 235, 47, 1], 941: [941, 1], 942: [942], 943: [943], 945: [945, 15, 1, 315], 946: [946, 1, 43], 947: [947, 1], 948: [948, 237, 1], 949: [949, 1], 951: [951, 1], 952: [952, 4], 953: [953, 1], 955: [955, 1, 191], 958: [958, 1], 960: [960, 4], 966: [966, 69, 138, 23, 1], 967: [967, 1], 968: [968, 1, 4], 969: [969], 971: [971, 1], 972: [972, 36, 324, 9, 1], 973: [973], 978: [978, 6, 1], 980: [980, 98, 49, 1, 7], 982: [982, 1], 985: [985, 1], 988: [988, 52, 1, 4], 990: [990], 991: [991, 1], 992: [992, 8, 248, 1, 496, 4], 993: [993], 994: [994, 1, 142], 996: [996, 249, 1, 498], 998: [998, 1], 999: [999, 9, 1], 1000: [1000, 250, 50, 25, 1]}



