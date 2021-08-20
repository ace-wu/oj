from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self.left or self.right:
            lhs = str(self.left) if self.left else '()'
            rhs = str(self.right) if self.right else '()'
            return f'({self.val} {lhs} {rhs})'
        else:
            return f'({self.val})'

    def __repr__(self):
        return str(self)


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum_set = set()
        total_sum = self.get_sum(root, sum_set)
        #print(total_sum, sum_set)
        return max([partial_sum * (total_sum - partial_sum) for partial_sum in sum_set]) % (10**9 + 7)

    def get_sum(self, root, sum_set):
        if not root:
            return 0
        lhs = self.get_sum(root.left, sum_set)
        rhs = self.get_sum(root.right, sum_set)
        my_sum = lhs + rhs + root.val
        sum_set.add(my_sum)
        return my_sum


def build_tree(value_list):
    from collections import deque
    value_iter = iter(value_list)
    root = TreeNode(next(value_iter))
    queue = deque([root])
    try:
        while queue:
            node = queue.pop()
            lhs = next(value_iter)
            if lhs is not None:
                node.left = TreeNode(lhs)
                queue.appendleft(node.left)
            rhs = next(value_iter)
            if rhs is not None:
                node.right = TreeNode(rhs)
                queue.appendleft(node.right)
    except StopIteration:
        pass
    return root


## TC: O(n)
## SC: O(n)

s = Solution()

print(s.maxProduct(build_tree([1,2,3,4,5,6])))
print(s.maxProduct(build_tree([1,None,2,3,4,None,None,5,6])))
print(s.maxProduct(build_tree([2,3,9,10,7,8,6,5,4,11,1])))
print(s.maxProduct(build_tree([1,1])))
print(s.maxProduct(build_tree([3434,4223,2441,6764,5911,7094,1827,9223,3580,6615,8446,2770,5112,718,3292,4092,3269,377,7407,4515,4512,6098,282,2197,9833,5285,5841,9643,8708,500,1834,7466,1360,8075,9353,804,656,8645,2445,4648,1194,2185,7883,None,3282,2067,8329,4847,1363,1037,2829,3789,1321,8183,2392,8978,436,7776,2286,8635,587,4391,5075,7307,8431,2236,3588,None,None,6968,6324,None,2149,None,5868,7401,None,8175,7064,1404,8772,None,None,2259,3610,2455,7961,None,3397,8996,7112,1316,4197,8704,2391,227,4720,9266,3273,3503,None,5237,7905,1921,8540,1886,6681,4740,6134,8408,3442,None,3830,2786,5382,3499,4469,1260,1456,6568,746,8076,1665,None,5700,7959,209,2485,None,3253,6181,1080,8731,4829,7285,None,2136,3995,3153,4968,549,3290,627,7812,4406,254,8382,None,None,None,None,4246,5958,8358,1853,2260,3188,1963,9753,None,8976,None,1244,None,None,9473,8385,None,2370,3469,2059,9616,1238,3089,9857,None,3873,2465,1945,6202,7906,9853,2006,None,None,None,9707,4539,4815,3158,4493,5941,7648,7964,6534,9843,7333,409,5246,None,None,7899,None,2515,5559,2888,None,9258,9370,9767,None,4140,9421,5873,6398,1152,6895,9101,2652,6053,721,None,None,None,303,4819,1605,3110,5366,5363,6173,6188,7605,6414,None,1038,3255,870,798,217,1880,76,726,8296,4856,None,581,None,None,3247,261,7183,5597,6299,None,6591,None,2059,4841,3925,None,None,None,8182,3954,4280,5532,None,None,1900,1084,1704,459,4312,None,None,5370,6139,5517,1806,2949,3257,None,7820,7347,None,None,1224,1430,9544,1349,3583,5668,None,2646,3945,1422,9511,None,None,5411,8568,None,5311,7155,9720,1904,3772,None,3186,None,None,9768,2530,None,None,None,7092,None,7664,None,6784,2692,2031,9754,9864,4004,None,4518,4412,8741,5750,9149,None,6613,1859,None,784,2634,6172,4635,None,None,2675,None,None,718,5809,584,None,4540,1547,5399,None,2446,None,3829,None,None,None,8734,6278,8937,5207,2497,None,4524,502,9879,778,409,1892,None,7085,9924,2346,None,8991,None,None,9519,None,None,384,None,3435,5565,None,4053,7290,None,None,None,4105,2830,5815,8548,None,None,9641,8344,3660,None,9721,115,8064,3557,7344,6233,None,6000,9789,8861,3678,1170,1082,6525,6463,9355,None,None,None,1227,7890,9396,None,None,2978,7651,None,None,None,None,7948,3720,3218,1878,None,None,None,None,None,3308,None,None,None,None,None,None,None,201,4360,3255,None,None,2568,3229,None,3261,6406,None,5929,9516,None,None,None,9247,5988,2073,None,None,None,8689,None,None,None,None,5819,None,None,None,1352,None,9355,1350,None,None,9825,6797,1522,None,9138,None,None,1040,None,None,8289,6770,6913,7863,5710,6803,None,2297,None,None,None,9738,None,None,1004,None,None,None,None,4112,2947,913,8498,8879,None,None,8526,2609,3486,7499,None,None,9878,1833,309,5298,6989,3188,8401,7437,2560,831,None,4949,None,None,5723,8576,1991,None,7982,4985,4376,4170,5564,5641,None,None,1139,2392,None,None,None,4040,None,None,None,None,None,9909,None,None,2298,None,None,2294,496,9336,304,8230,None,6056,None,None,5382,759,7933,5960,3873,4548,6075,2686,7177,None,4091,None,767,None,4877,1756,1717,4537,None,None,None,None,2095,7406,870,None,None,None,1509,8381,None,3923,5682,667,4522,None,1869,7024,9323,1579,None,None,None,None,None,None,None,2951,3890,None,2131,None,8785,757,None,5912,2230,7837,4311,1439,6591,5966,None,2452,7591,2279,9438,8189,2293,8306,2934,3316,7320,4994,4027,None,6188,2554,None,9148,None,None,None,None,None,1252,5554,7583,1552,3862,None,8131,None,745,None,None,8880,16,7642,7181,None,None,2739,None,4819,None,None,None,None,None,1490,None,9057,None,None,None,1775,None,None,None,None,None,3482,None,7145,None,2374,9308,None,None,8204,None,None,None,928,None,None,None,None,None,3209,6076,None,None,9683,None,4879,None,7874,None,4504,69,None,None,None,1,362,None,1404,8888,1875,6483,6565,8395,2214,8420,4913,7525,7657,327,5459,2016,6299,5042,8558,876,4798,None,7907,4536,None,4508,None,None,814,6337,None,2782,3291,5829,None,7395,9107,9361,1260,10000,769,8659,None,None,9771,None,1160,5252,4088,3967,2779,7333,None,None,872,None,None,None,None,None,None,None,None,8543,None,None,9733,5123,4585,None,2880,9590,None,None,None,5920,None,5902,7266,None,9077,None,None,3794,None,2867,None,1822,None,None,3104,4782,9380,3245,None,8841,29,None,None,4115,4113,9770,4838,None,None,None,4573,None,None,None,5290,None,None,8254,None,None,5139,6,None,None,None,None,None,None,9066,None,4679,1378,1120,6088,2864,None,None,4555,None,None,4250,9565,7891,8402,3625,None,2381,None,None,None,None,None,980,None,5230,6426,5967,750,None,None,4537,None,None,None,None,None,3030,None,None,864,None,2600,None,8858,1373,2775,6504,None,5279,None,None,None,3933,9352,8292,1023,None,None,5354,3052,None,6710,None,2240,None,None,2165,None,None,None,2958,None,4988,None,5882,None,None,None,8686,3471,244,9758,96,None,3855,None,None,None,None,3210,None,8274,None,None,None,None,None,None,None,4513,None,None,5767,None,None,None,None,9506,None,None,None,None,None,None,None,None,None,6745,5337,None,3575,9091,None,None,None,9830,None,9738,7999,None,6138,None,9425,4203,3839,3824,None,9591,9675,None,6884,56,2355,5197,8046,4136,6357,None,8317,4117,None,1842,7985,6869,None,None,9812,8336,None,None,None,None,None,None,None,7511,1385,None,2986,None,8634,308,4008,7522,None,None,None,None,5879,None,None,2858,None,4856,5299,8482,5326,2624,858,4350,7321,521,8806,6941,3319,None,8915,1065,3453,6126,5694,None,None,None,None,9768,123,6371,None,None,2088,5298,782,9818,None,8197,1175,1146,1945,None,None,None,None,None,None,None,4079,None,None,None,3231,None,None,None,None,8841,8371,8971,None,1755,1891,None,None,None,None,3016,None,None,3136,None,678,None,7919,644,None,None,None,None,8769,None,3159,None,None,None,6179,None,None,None,None,None,2913,7271,None,733,3795,None,None,None,None,None,None,7164,2469,2744,5399,None,None,None,None,None,None,None,None,None,8888,7666,None,6396,1148,2642,None,4113,555,1669,None,None,None,None,3039,9576,7126,None,263,None,None,None,None,9748,None,None,9176,5235,222,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,6188,None,None,None,6012,8488,None,None,None,None,888,None,None,2384,None,6752,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,8105,1530,8038,None,None,None,9791,5982,4757,2791,9973,None,1030,None,None,None,5403,2796,None,None,4324,4362,1124,7488,4436,2556,5331,None,8660,1594,7398,8895,9023,None,None,577,5560,5592,None,3838,None,336,None,None,None,None,5396,None,5866,None,None,None,2308,None,None,9077,None,None,1270,None,1593,1990,None,None,6756,None,None,9650,None,None,5707,1106,None,5615,6076,825,None,None,6629,None,None,None,None,1502,4739,None,None,688,None,5134,4677,None,None,None,None,9885,1152,None,None,None,None,1619,8418,7699,8855,None,None,8402,9539,None,None,None,None,None,None,None,9468,None,None,None,None,None,5624,None,9683,None,None,None,2742,None,None,None,None,None,8847,7327,None,2759,2537,None,None,None,1981,None,None,4756,5394,1265,2611,None,4864,7675,None,None,None,None,None,213,None,None,None,151,None,None,None,7739,5814,130,None,None,None,481,1623,4669,None,8861,9953,5835,1593,4338,8037,2690,7015,6100,652,1497,None,None,None,None,None,None,6487,None,None,None,None,None,None,None,None,None,None,None,None,None,4692,2297,None,5542,None,None,None,None,9787,None,None,None,149,2236,4955,None,None,None,None,6703,None,5427,4698,2349,4578,9504,None,None,None,None,9921,473,None,None,None,None,None,None,None,None,None,None,2242,6092,4113,6763,None,None,8592,None,None,None,None,None,None,None,9095,None,None,None,9075,None,None,None,None,8514,None,None,5463,4782,2528,1399,None,3188,None,None,8314,None,None,None,None,None,None,3321,1832,8620,4797,9036,None,1243,None,None,None,7464,None,None,9351,None,None,None,None,None,7468,425,None,3747,None,None,None,7599,None,3724,None,742,9578,6532,2358,8082,340,9320,9391,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5069,None,None,None,3669,None,598,629,None,None,None,None,None,None,None,None,None,2557,None,None,None,None,7496,6361,None,3693,None,1769,5807,4896,3384,2709,8316,3453,None,8683,6104,1462,None,3274,5488,None,9127,1830,None,None,None,4329,None,8761,None,None,None,None,1267,None,6006,2603,None,8455,None,None,312,None,5447,9453,None,7068,5531,4462,None,None,None,None,None,None,None,None,None,None,None,None,None,4103,None,None,3212,2659,None,None,None,None,1520,1032,None,None,None,None,None,None,1495,3098,709,9217,None,None,None,None,None,None,None,8529,4539,2454,8339,2077,6314,5155,7575,5197,7167,None,None,None,9379,None,None,None,9393,8408,None,8633,None,None,None,None,6241,8583,None,82,None,None,None,429,9391,6592,418,6105,5964,None,9746,8472,None,None,None,5501,None,3570,None,None,None,None,9490,None,None,None,None,None,None,None,None,None,None,None,3962,None,None,2299,7952,356,None,None,None,5180,8541,1860,None,None,None,None,4862,None,1825,None,3981,None,None,None,5022,None,None,None,None,None,6694,None,None,5648,2911,5099,None,None,None,None,None,None,None,None,8719,3130,None,None,None,None,None,None,None,None,9453,None,None,None,None,None,5808,None,None,None,None,None,None,None,None,9101,877,5009,1889,9232,3699,None,None,None,None,None,None,None,None,None,None,2971,6579,None,None,None,None,None,3152,None,None,8947,None,7526,None,None,8076,None,None,None,None,None,None,4827,4544,None,None,None,None,1373,None,None,None,None,None,None,None,None,9681,None,None,None,None,None,None,None,None,3068,None,4929,None,None,None,None,None,None,None,None,None,None,None,None,None,None,1447,None,171,None,4767,None,None,None,7197,None,None,3116,2056,5742,None,7142,7645,692,None,None,None,None,None,None,None,None,None,None,7244,None,None,None,None,9336,9541,1885,None,None,None,None,1095,None,None,None,None,None,None,None,8997,None,None,3604,4473,None,None,None,7284,298,None,None,None,None,None,None,9330,None,None,None,None,None,None,5501,None,None,None,None,2950,5479,None,None,None,None,None,None,None,None,None,8774,5861,None,2043])))
