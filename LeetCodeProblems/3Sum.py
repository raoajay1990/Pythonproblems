# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

def threeSum(nums):
    three_sum_List = set()
    nums.sort()

    i = 0
    try:
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:

                sum_of_3_numbers = nums[i]+nums[j]+nums[k]
                if sum_of_3_numbers == 0:                     
                    three_sum_List.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif sum_of_3_numbers > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
    except ValueError as e:
        print(e)

    return list(three_sum_List)

nums = [41204,6323,5021,27767,-18684,89279,16935,-10093,-9753,-5202,83041,9491,35206,-3786,25148,-989,1290,68246,-13583,-3574,-8125,-2680,80013,47302,-8711,45233,5497,13996,-8707,61757,27122,-544,-3638,-12466,80860,86309,-4842,74323,74240,29760,98678,23623,98540,-7551,-18859,88487,82031,-17613,71005,73696,-8448,53294,-10696,-929,62455,74509,93579,-11159,11536,34075,29519,-6394,29421,-18852,-4961,-2334,-8317,59554,-1801,64592,20842,-19027,-524,-6596,-1414,-9478,6543,27221,-11680,-16476,88651,27805,-16367,17146,11928,36835,-99,-6949,44255,52382,28303,99208,46608,-3067,13065,-5331,-4633,48678,-9613,-18268,-4377,-17956,14915,56875,22797,-18734,-10635,-3348,-9211,97693,-10507,23534,-14942,77612,58511,-9194,-19819,-13038,94266,96461,-3897,-6247,-785,-12829,5269,17991,-12346,-9287,51982,98503,-3490,12742,24162,-1390,-6575,-670,83307,61945,-12620,-12110,-15201,-10278,-5947,34532,55069,48334,22250,-4370,29072,-16625,-18186,60743,36203,35731,15655,-9106,-5734,-8486,-18688,-10956,55323,-17637,-16699,40430,31738,-2606,67304,86606,-11082,84814,97802,-4539,-5724,-10162,-11103,-5814,-3475,-15929,-12242,-3171,-632,96688,43135,-1371,16611,33,-6713,-13057,-8712,-12406,82814,65391,-13261,26526,-12659,39875,-17915,-14485,-10922,-16085,95980,45573,-16364,-302,8883,-7677,-8509,86579,-17516,5895,36203,42776,-8548,91988,-19282,-3541,-14395,-2986,29311,14573,89469,80989,-869,86805,-12341,15157,-10109,69639,71687,-9862,1965,-13909,83567,-13164,54106,-9985,41727,2149,7209,37164,20572,-19903,59087,99083,40075,80674,10693,-1080,48281,-1108,40199,57201,-10288,54627,-5412,-9827,-2940,-19116,-5586,9914,46748,-6699,4024,51474,-10278,-2162,-2406,-13267,-16252,42640,-12786,-754,65940,43914,-6146,66860,-18563,41498,-1900,94604,-1182,-6328,85304,-5220,-17410,19908,56469,11683,45706,80250,-2898,-12869,-16308,-7314,44244,-18931,-7237,11129,-12367,76445,-17037,-14660,-10551,-17869,20456,69766,-4589,-4895,-17174,55100,-14959,48293,92543,74769,61873,59670,88651,-19865,70642,62860,-13581,8967,42036,2441,-19111,-16917,17215,-2916,-5856,-11499,77121,5813,-13496,-15678,79113,-11730,-16907,36757,-7305,-11141,6141,64009,90023,-4781,-16983,78346,88914,16245,88398,-16144,-7004,-17474,10779,-18484,71493,-487,-15844,89127,71995,54286,83892,-7736,-17228,-4392,76857,-15715,93791,-16374,-10989,-19857,43347,69990,5825,74336,-12509,68009,70902,7558,21916,-16682,78644,61188,25934,6335,-10959,-7870,-18908,44593,19322,74475,-17351,18575,340,45409,-9581,32353,83706,25413,-6647,92758,15758,44202,35153,85568,-6341,21249,32239,38101,-7245,5764,96301,-4239,9664,-5372,16172,-9256,-15698,-10630,95825,38219,80885,-3902,86851,-2397,-19475,99144,74193,39028,14783,72340,6476,-13418,-5853,49551,-33,71753,50629,-17077,-3455,-7771,-8998,21796,27367,40841,-11139,-387,67403,28396,45993,-14724,25195,97971,50627,99346,-3196,46754,26201,66961,82184,-4794,-12840,21725,18882,-14267,-15895,58727,31893,-7219,34790,-3680,72248,-8838,32165,73606,7082,-10323,25187,88976,36010,70084,-12259,-14278,-8716,91401,60870,58325,90445,51126,98205,28572,-18215,-11293,-6647,-17037,-2110,-4970,28691,27761,-16805,-19745,78203,-7066,-16500,-6674,78200,68203,-3255,-3454,-10462,26824,65609,76178,63060,-19051,82792,98701,14685,-16147,39226,-14345,-2402,81994,85292,-5171,8712,-6137,-10806,10517,37261,-13103,-4933,-15236,9540,53356,60803,23842,76247,7186,57607,-9077,11063,45147,-5787,-18250,-893,-4641,20106,-16012,-5595,-363,18807,69647,-19426,66874,9371,43183,39326,71542,-6600,-19349,25667,-15442,-16758,-12651,88353,78529,76144,27629,-4621,-12946,-15840,-6496,19191,-3464,-2625,9328,74993,-17537,-1076,24736,11239,-4779,41765,67797,-8977,99341,13330,23257,40761,99368,51071,66426,-12311,22589,-15737,-15298,-637,-11014,-4988,-18636,-6008,-11771,-8039,-9200,74396,-7356,-11291,33217,-7374,59320,-14827,-3324,56603,15046,57219,-13465,-13320,24641,1586,-15424,-18545,62005,82807,-12863,-16365,-9724,-19489,-3592,-12894,45576,50716,1462,-16972,45684,37841,98881,-19226,18737,4231,25864,95998,94269,32708,54028,49155,25020,-8656,-11677,-17276,-17214,6041,45000,-13829,-8402,42639,-16132,4943,-8106,-4929,-5924,-16893,3323,17114,42804,-3023,-15527,25668,65871,91218,-28,3783,95685,38256,55859,-3662,95448,-17663,92509,23663,76589,-11826,3473,-11317,12526,-10285,-15634,88712,34696,-10289,1773,-7865,-11427,48129,-13425,-11732,-10929,-15182,-9073,40992,76315,51939,-9062,-11380,-19665,-7365,-13144,-7456,-1270,77295,81927,-13823,-277,-8343,-15311,-12281,-8726,-12181,-9150,99296,-16790,-1067,68375,-7011,66104,44067,-17728,-17966,-5792,-15351,74123,-4199,-12980,43225,65874,54441,-13523,3015,-5803,10488,45306,-6384,48444,45180,-5654,-2540,3146,-18093,34706,-19423,25292,34233,-9532,37978,78259,-6552,84143,-7826,13970,27030,-15568,-19956,-15994,-14045,-17263,59186,51485,40010,10083,2636,45412,-15393,17904,-9269,-4728,22603,94813,88879,81322,-13659,-14678,-18077,-19884,80850,75999,33430,-11693,91480,36788,47333,-1103,-16957,25961,-7291,73563,24102,97270,6513,13762,-10715,-8286,-14153,23908,39530,-10301,61818,4452,99627,-16041,-16316,58028,-8242,12560,-14613,-11546,97292,79208,62990,-9382,-4969,2408,-7444,-8433,-9677,78054,43510,-13841,-15987,37851,-605,-10297,-16117,-8545,-7740,82293,-12878,-18395,97884,47992,63482,-12769,65786,49392,-1655,26893,-18369,-4923,-1057,14760,-8698,45173,8258,63082,21176,-11828,56132,-6689,30448,26675,-16430,31934,55417,-5067,-5647,6024,26856,-2981,70652,-10049,44977,49430,70586,97701,-7293,2423,-1361,25735,79078,-9582,-7526,-18578,-5975,-6597,-17621,71770,-5171,-4486,-3402,55058,-638,-17488,27989,-3584,-1383,16045,-6217,-14112,-11507,-14121,-4578,6584,-9611,-57,-18690,55561,-16989,-8448,-2419,58368,30571,93825,83289,-9474,22625,-12208,-19945,37657,56284,-19655,-5840,49506,96648,2229,60235,55904,40563,-4088,-5834,61168,-42,-3992,32847,28469,-6065,21264,70379,-4445,89861,-4290,52401,1367,80437,42900,-18282,13836,-13512,61723,-14267,97349,-4226,85429,34533,-2833,74918,10809,52425,-6329,14183,-13690,-100,-11767,29761,2835,66797,-19571,13036,-777,39483,11557,-3411,-16670,3083,53132,48194,61345,-10191,-19789,-5020,83959,-16030,-6572,-329,17359,81925,-2781,-6230,-6566,-14550,12603,59998,87973,-292,13874,-4265,47968,-3687,15003,-2064,-10135,98940,988,-9032,15015,17741,8352,35124,13416,60201,72820,81201,18309,-12692,-19432,22857,85523,-842,-17572,45800,-8168,-6962,62581,55642,86850,-18418,-16371,-132,-15763,-3901,76515,-3605,87684,-2453,13434,81920,57977,-10750,74482,37098,48842,91748,-18584,-10876,-1281,63943,90433,-6660,-7949,23224,51775,-15848,-14179,-13348,-19631,57050,58520,95934,45804,77369,91409,-16363,-8856,42941,75616,52238,17278,82177,-15119,-19823,-1997,70052,73702,71040,27732,6953,-2328,4225,-3290,-4696,-2309,42409,26734,11930,70080,-4791,81381,-8371,-13813,82081,79402,82745,-18557,86296,-7724,-9286,31461,-14323,51848,93742,51236,11206,-14640,97091,28732,-10175,-10554,-9676,28221,41653,-3096,58349,19740,-4731,-17319,-5591,16272,-1483,97819,47879,-15831,6853,-8051,-9252,77290,20975,-9027,2520,-16983,46562,-10552,-12494,30140,-12334,40701,-10100,36364,-5111,69294,-19831,-11933,-11417,49532,97335,-12277,52381,94271,34941,65601,57898,-13539,-12362,78522,-11137,-3342,22991,-15472,32319,94899,-19597,-16796,28148,-11855,-2492,-12593,91477,-705,-7055,-19441,-16144,69164,-13747,-11660,-5184,-18665,61877,46240,17631,25376,-11408,-5732,-16730,-11353,6821,-837,-15522,-12155,7812,21805,-10036,20930,-7936,-14954,43414,-7970,40384,-4074,-2478,-7664,-18539,-8210,-1795,88096,-5698,71225,29024,-8315,2408,22177,-12246,-11496,-15293,45291,1794,79665,93307,-12458,81778,60803,15733,-261,-11111,-16294,-6148,-4666,34377,-8559,-7174,-10589,32613,27064,-7009,-16984,-2799,16331,-12484,-1447,-4,10904,-8399,31725,-16260,-16510,11774,33380,-13941,-18956,17268,88040,-13604,57968,65411,-10392,83839,91436,54241,-18437,77195,-2219,44777,38709,-2958,71806,-4357,-3344,-16219,24044,58296,22439,-3603,96019,89321,-19821,28711,-6146,92535,50815,-18738,-11375,58098,7446,-7640,91508,73549,48042,68591,6,-10687,38334,-4927,-13531,74784,62777,48950,87298,-14499,-5966,-14426,-11917,-13131,-8421,51109,-7436,23928,15971,-6869,59525,20956,66428,-7267,-6327,46260,79423,56001,71599,-9936,-1871,70680,-13475,-7375,-11752,67586,-7807,71747,-19161,99499,-13645,-963,-12253,-9050,-1910,57557,-11007,71106,30868,39771,30189,-6546,71910,-12226,-3647,42324,-4940,-3525,-2374,75783,43071,-5047,-13671,-7665,-19489,-8093,68706,-1924,-16536,-11952,61287,-2939,-10964,-9475,-5625,38593,-1188,-19989,-5994,53463,84570,-11645,2402,20225,-10511,-6325,-10271,-4671,-10529,9957,-4729,26764,-1748,-829,37419,-6480,-5339,-19292,-15949,41625,16091,75631,-4854,99021,65475,57940,-15635,77599,18926,-1203,-12626,-5620,-16802,29791,29665,-13175,62683,-18954,-12748,-8783,70157,-7082,71767,96082,80739,-18473,89126,-18752,51742,75228,67056,74541,20356,1623,57375,18779,-16435,41373,61276,-9906,46046,-10480,-19570,-12635,87505,-13695,56202,-9925,3247,-9096,-8116,-17710,11985,49927,-16827,98297,43702,-8602,-8995,-15196,98239,16382,-15335,75538,63923,76235,-34,-17161,-3205,-4546,65331,88828,-16589,-1753,46631,95976,-16505,1011,-8921,80590,-15457,-9557,-12694,-19279,89299,80255,17780,77023,-8857,-15678,19313,-8726,-4547,-14775,65735,88262,62344,30923,85279,-16566,47316,88764,91012,15578,61569,-5282,-15655,-5471,76512,81532,-16171,6003,76777,-3711,68408,70037,-15722,40506,16955,97638,-19980,-12136,57346,48522,9069,12799,54866,38123,58595,11480,-8304,97909,-6133,48114,77104,-19384,26739,34864,39833,-19272,-11049,-17188,-12416,-13889,-12924,-11268,-15425,39495,-42,33786,55099,94765,98965,-4247,51397,-18290,-17675,28862,-3835,-13753,66533,-1859,-10792,-2765,20897,-12776,82453,12888,-5362,-5437,-18194,27571,60617,11849,7029,43565,14684,-684,-1853,-13133,46895,90558,18294,-5284,-153,95069,68699,-17953,-10711,-2173,-3886,89189,21772,93878,-3404,-10283,-10903,35594,69557,-7595,-11474,31216,44276,43602,-14211,35215,21810,61186,6287,25585,30021,78565,73419,-7867,38091,27228,-12180,82530,85218,18795,-15500,-7646,-2889,-13701,47291,-19675,-11179,-3762,-9268,42764,6319,84919,-14838,-6542,-8613,61737,-3893,-7105,-9790,-17531,80520,56113,8217,31664,29188,-16695,-8491,-17594,46013,84098,-2328,97638,-8823,-13725,66627,73889,-12457,26821,-15140,-3757,-9848,-3536,38883,62743,-6207,-256,59800,2905,49744,-16279,78153,32030,9351,-8524,-13103,-832,-15589,-5543,72003,17803,20748,-9862,-17909,-3256,-10341,87141,83905,39991,-9230,45135,92630,-8624,-13780,-18150,-1936,58711,-17075,-14372,-17396,-12121,-17498,94136,-18752,48900,50285,87381,63398,-14649,36274,19001,-12398,7572,84529,-12798,-11003,11941,-13551,60425,-13774,8509,-18888,-18023,-12183,21704,-8368,36013,-14783,90904,-19665,15747,-14317,88544,20136,-13212,94538,-3262,-3070,45369,8864,-4314,-11783,9491,78437,-16908,-15304,43150,-3019,40073,-4329,49857,5692,75732,28369,53032,5818,79081,-10022,-9881,-17734,12120,-5121,-13238,-17956,-7691,-7409,-12401,-7870,-1043,71115,-8501,-3973,99152,29688,-9212,23837,21381,-2854,98079,-8082,-7578,-1606,20462,5945,89019,34431,12567,-9760,18033,-12245,-4619,-15627,24089,-11099,-17425,-17707,31273,-49,-7966,17971,59192,-7732,11815,52540,70532,94281,40882,38864,12590,-5588,76557,-19235,11802,-6514,84431,-608,-566,-8566,-18550,-12846,-16230,-6691,11189,-16599,63194,20006,-13995,60370,-18653,-18701,-19426,-19652,-3283,26370,-12220,-11871,-5862,-12395,73528,49661,-11275,-13556,-17963,-17156,-17979,53705,-16263,83089,49817,-6204,-2808,6418,-10962,18039,-2641,-3335,22108,-12440,-491,70362,38066,27969,-10326,-17281,-13918,11751,70821,56320,49030,20229,-13043,22308,-15987,-6238,-10585,-1782,71212,-10676,48781,-981,-11465,-10946,-18632,-5190,63611,47771,-18449,-4323,-11065,41183,-619,-13501,-1320,78346,91950,75743,478,55826,-622,26981,88819,52913,-10403,-7117,-2837,-15495,-15424,34493,-14971,90029,26379,80083,76120,91346,25100,-15426,79205,-16588,80674,-5508,-927,-6559,50544,49666,46973,-14439,68509,-17747,-5086,17988,94836,3693,-12469,-14578,-7744,28416,-12535,-2279,10175,36796,8927,-9120,68125,-3309,40848,29311,17592,8861,91670,80063,83343,26072,82786,-10877,-9044,1986,67335,-18657,11746,-15395,-159,66555,-14735,-17611,48486,-1171,14043,-5738,30911,-13368,79802,77324,-6517,-9166,-19443,85757,76857,38770,-2947,60785,-6179,24830,-1779,6867,-17946,41596,311,-17584,90377,-18905,-18040,71974,53751,-5982,-7287,-1037,-8572,39273,46551,67974,-7758,50217,-15446,-11177,-10787,-10898,67678,-13709,71377,-4904,60437,98150,63250,-11480,35094,61544,-15995,-8581,41636,-3255,82499,17921,-11604,32616,46176,91037,43495,87697,48059,-8117,-1706,92336,-19824,77357,-5697,-15149,59313,-6367,-18728,-5814,31642,-14613,-11066,-13593,-1573,-19249,46800,68951,37129,-2403,-14665,-11900,40853,98322,16519,48660,-12696,-17473,17126,35234,54033,-14384,12154,31573,-9983,-769,-3146,9547,-12820,-6518,-5827,40745,-17002,31023,-3571,-7095,16399,-6467,-9449,22465,-19868,30176,-4240,26518,-9651,3089,-10860,-19406,20130,52697,83249,65813,28976,-16848,78818,98995,96682,14391,92098,20549,62006,16942,99046,49677,82237,34011,-8258,31283,49866,35016,86832,35397,24752,51140,-19690,40592,78211,52479,89030,-6606,57947,15471,-14625,-10722,2903,-18108,-2326,40812,-4970,55582,-1070,97680,-8940,-11557,37586,21978,-16676,63181,60481,-7747,-16713,59103,-5732,73955,-5220,14269,96437,-8671,-12870,28507,-13511,66421,-6657,93069,-7631,-16774,78470,-19669,-18035,-5350,57985,-12261,66799,-11017,-12812,97206,87761,-13846,81024,-654,-15552,-15536,87577,-8573,70561,35099,-10846,-16476,88207,90908,69361,93189,65717,37706,96959,21296,-18648,-735,-18949,22281,-13687,57357,-14505,3501,-18275,14463,-8906,-18335,-26,-16592,35290,-2330,-8528,469,-19087,99302,-15478,-5711,-9106,-7331,-1051,33870,26941,37597,-4600,5833,38089,42938,-11051,-13086,61693,11747,67821,-15037,-10379,-16657,-11535,-921,96164,-10116,-6825,224,29700,-17909,-13640,50586,-8878,81335,65027,-15000,85312,63632,62394,-14032,-3577,49220,97205,-15382,-9876,-19099,-6009,-5405,-17133,5019,58666,37271,63494,47254,20774,41622,76172,28636,67466,-5790,84191,76212,-8816,20513,-18351,-14190,-10623,-1574,-16922,29826,34697,-11553,1245,-13649,78628,2470,-18882,2016,-17412,-19473,2037,-3747,-7394,-12842,-6173,-5845,-204,28893,-1084,-15747,-6469,-6308,64298,40037,-3213,57131,34649,70196,-8574,-3367,-17384,11019,-10327,-17110,48817,-2988,-6484,-4276,16777,-2136,-2820,-19960,-11446,-18247,14834,69449,-11174,17624,46126,-4855,-11143,-2768,-2771,41411,-19789,-19327,33731,51223,-19183,-3846,13814,-13606,-19171,-3099,-11090,89482,-5401,-1154,83358,19692,-7658,60959,-14311,-19173,53903,55513,97372,-16530,54701,-12875,-5125,62242,-17949,52323,20537,-3851,2800,-10891,84686,49733,-4360,54634,-19647,-6602,-19018,97088,-10054,14902,-9875,-13660,31049,27230,-5251,82920,65276,23589,-13118,66250,-4078,91845,94747,-1405,5350,-2278,55679,16194,-11105,98423,-2780,-1081,390,1557,36911,89394,68291,-4301,71834,-17218,70978,14197,-1900,-2341,-16091,-14360,36892,85015,12130,69902,-16840,58202,-7954,84874,8617,88449,-15708,64367,56192,23823,9256,-5005,-6097,90697,-7137,70056,-14213,52729,-4374,-5756,93343,79789,38047,50758,77430,-2532,-9861,57826,-958,70156,-5757,-13093,25090,-7035,-15005,26058,98167,97062,85552,-12534,32153,-7810,-13702,-18116,90612,25945,-1137,-6245,-2870,75742,14657,15379,-12999,74021,-15473,33450,4899,-5907,-13607,45875,-18708,88552,81234,79112,30980,71988,56623,43299,-660,15809,63151,18758,77195,-4413,-11297,-7888,67040,12304,23414,12276,22128,11361,-14340,25746,35884,98899,43885,-18579,-19285,-3397,-17753,-5142,37664,-5704,51612,67032,91822,-1394,20430,77271,9523,-6973,-13282,-9391,90421,69484,-6900,95900,5180,-1429,-9145,-19650,42646,65282,96176,-5883,27795,26488,96190,63431,36519,64385,89361,-1418,51629,5810,-9559,-14856,-18432,40358,-9546,-17729,56738,-12517,82914,-3578,67159,-16650,85689,-3023,-4277,-10691,-426,25416,22148,64962,54893,96319,-17963,61491,-19317,-8582,13342,982,-11294,-3956,-7099,-19923,2742,22527,-2578,52301,23514,67150,23089,-14206,9558,64081,37522,-3630,-7379,-14101,-7118,6906,74836,95174,85179,59680,-18908,94284,27393,-17005,-7639,14798,-8834,-6853,-10307,-15058,36503,25685,-6676,-17930,14845,-3510,29190,-6678,-6086,-12252,-10068,-1039,73125,8968,-12779,-6717,46036,-7176,91649,36422,94458,-13567,-16388,-445,-13166,-13455,-18463,35116,-18339,68075,-10444,87043,32692,-11196,96384,73615,-15784,16341,-3383,77166,31440,-5796,-7312,-6386,-10992,44953,-7074,-12282,-9789,23232,87418,16169,90817,-10999,-7334,64342,41648,-4776,83135,54557,-6614,51659,96190,-6403,-17190,47953,50440,-283,-17932,97943,-11797,66437,-6662,42552,86939,96800,-3696,53528,-10159,74624,-8511,-7116,-1248,54189,69744,14223,25487,92242,90968,6909,34526,52928,80234,-4325,-5328,-6536,81696,-2737,10523,21832,62423,-151,-8429,76342,5136,-14793,-16729,75829,97199,-1165,20678,81158,6749,30367,-14442,-18768,90248,-18945,62434,-14037,32128,73831,-7230,49846,1210,85461,73950,-14677,92558,86982,-12133,-2209,14523,-15165,13217,83906,85120,-3058,-15961,-17400,-2042,-12409,28082,-3601,47051,-8302,89360,-19333,-19374,-17899,70681,-8875,-10088,-18964,35664,-13036,-11763,46944,-7544,18427,-10274,5274,-14804,-13403,94087,1616,82658,29800,-5539,-14246,72318,88244,-4418,35211,-10147,60401,68810,93623,-14898,-2676,-9385,24046,-9233,17125,-19741,18238,91652,2199,30146,-7806,-16572,-15850,-1413,67893,18336,93039,-17131,-14197,-8161,-20,78433,77434,-9752,33759,28179,-2170,4552,19862,-18782,53388,88049,72758,-953,15071,-14749,-1480,36826,-6133,-3459,6179,-3614,-19654,68853,76628,26938,70517,92101,52534,-17649,-7738,63602,963,58930,-5909,-6287,47004,-10255,-2209,9008,-9229,-17176,-7284,-4624,58214,18713,79087,73016,-3528,44707,-16105,62143,36866,-18479,23093,-3414,-19321,-11643,72348,28598,48862,-17279,-2450,-19936,-420,-3303,36048,98944,38668,-14061,70525,-7638,25438,44647,11049,56580,-18257,76762,-15263,94369,84868,78860,-2503,-6401,-13341,-6103,-18725,-3955,-12331,-7086,-10190,-15101,-10901,-5294,-6000,-15158,69607,-18961,96044,48110,92077,49905,94944,-19046,-26,-4244,-48,-17759,38988,-15623,-19208,8269,-13924,-12542,84119,60076,71797,60469,-10024,91043,81527,80409,14716,-3724,-10942,-15686,-8608,-11374,13264,-13307,-18169,91993,-7206,92758,60849,-666,90864,-8190,30560,56583,62915,9076,244,-13023,-1,-15635,-2924,52173,-3106,-2095,87307,6715,-17210,-4062,-15473,-19325,-2919,64924,55253,-10676,66387,68025,-18830,27488,-10433,-13028,-8227,25567,21928,23831,-19901,42203,-6015,-4271,-9100,-15427,43855,5162,-12299,48842,-8259,-14822,-4344,-17633,-2417,-5217,-5834,-18711,44825,-9018,50437,-14074,13361,6411,-19604,24067,-5139,44330,-10482,59661,95914,95207,9935,571,-766,34095,-10042,-4040,47314,-2186,-10619,88611,12427,-6094,99030,87592,64055,15913,33051]
print(f"3 Sum combinations in List - {threeSum(nums)}")
nums = [-1,0,1,2,-1,-4]
print(f"3 Sum combinations in List - {threeSum(nums)}")
nums = [0,1,1]
print(f"3 Sum combinations in List - {threeSum(nums)}")
nums =[0,0,0]
print(f"3 Sum combinations in List - {threeSum(nums)}")