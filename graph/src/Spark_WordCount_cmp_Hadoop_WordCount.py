import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


benchmark1 = "Benchmark: Spark WordCount"
benchmark2 = "Benchmark: Hadoop WordCount"
# WordCount 18G18U CPU_overall
t1 = "18G18U"  
benchmark1_a1 = "1547716780000,99.8876144665,0.0457870260592,0.00832448859668,0.0582740188184,0.0 1547716785000,99.6710123967,0.0208166812365,0.279023512524,0.0291474095599,0.0 1547716790000,99.9542145331,0.0249739855184,0.0124864730309,0.00832500832501,0.0 1547716795000,99.8375864103,0.0166567771441,0.0124916729115,0.13326513963,0.0 1547716800000,99.5669009128,0.0458104283793,0.133267220621,0.233199036543,0.0208224016245 1547716805000,97.0768330718,0.490635826047,1.32100612703,1.0192812308,0.0922437443083 1547716810000,97.5431232435,0.563262106237,1.05145586875,0.829640003358,0.0125187781673 1547716815000,96.8271716505,0.685504130734,1.31238019931,1.17073738982,0.00420662964833 1547716820000,94.2073511232,5.17361979497,0.589880632955,0.0166562565064,0.0124921923798 1547716825000,91.801963953,6.35169899973,1.35655410883,0.468855952576,0.0209269858547 1547716830000,84.1859436754,13.4880723096,2.27991294499,0.0251361796492,0.0209348903601"
benchmark1_b1 = "1547716780000,37844132,7938844,3512244 1547716785000,37839840,7938808,3516572 1547716790000,37838764,7938816,3517640 1547716795000,37839212,7938828,3517180 1547716800000,37805032,7965232,3524956 1547716805000,37237876,8512536,3544808 1547716810000,36783600,8955588,3556032 1547716815000,36908556,8757904,3628760 1547716820000,36318356,8970284,4006580 1547716825000,35440216,9253324,4601680 1547716830000,34026772,9269176,5999272"
benchmark2_a1 = "1547716695000,98.2932643813,1.57728629171,0.196074353045,-0.0666250260254,0.0 1547716700000,92.8094981909,6.15722750133,0.928779075658,0.100310781562,0.00418445058164 1547716705000,76.5809570954,20.3374983972,2.80263797111,0.270544982721,0.00836155357665 1547716710000,75.1451175997,17.7352744762,4.38407549387,2.72594837805,0.00958405213724 1547716715000,70.3003361716,23.6759805178,5.10856236527,0.90163931405,0.0134816312774 1547716720000,84.1676076961,9.14825853484,2.22131854749,4.45186713673,0.0109480848695 1547716725000,90.1877328368,4.66626369989,4.46574484828,0.676081505585,0.00417710944027 1547716730000,94.3512040976,2.12150528214,2.47725491951,1.05003570078,0.0 1547716735000,89.4100798797,3.24438442579,4.65807863861,2.67570548412,0.0117515717727 1547716740000,83.4041952614,9.35347665118,6.84094849853,0.274917369507,0.126462219412 1547716745000,80.51499409,14.7610223282,4.56386851056,0.147289625529,0.0128254456842 1547716750000,86.5153920606,10.3982641445,3.04041556667,0.0416541760346,0.00427405222892 1547716755000,92.7804044323,6.57358476586,0.537693217465,0.104138903991,0.00417868037274 1547716760000,95.6340538816,3.57317220413,0.554995883664,0.221090495752,0.0166875348382"
benchmark2_b1 = "1547716695000,37795632,7938168,3561420 1547716700000,37245240,7939820,4110160 1547716705000,36198876,7940096,5156248 1547716710000,36788944,7940508,4565768 1547716715000,35815964,7942020,5537236 1547716720000,34999016,7942944,6353260 1547716725000,34356376,7943208,6995636 1547716730000,34509516,7943128,6842576 1547716735000,34250460,7943180,7101580 1547716740000,34464852,7943224,6887144 1547716745000,34350852,7943052,7001316 1547716750000,35707044,7943044,5645132 1547716755000,36019616,7942752,5332852 1547716760000,37583144,7941336,3770740"
# WordCount 24G24U CPU_overall
t2 = "24G24U"
benchmark1_a2 = "1547800730000,99.8834327251,0.0291385693731,0.0291390893612,0.0582896161212,0.0 1547800735000,99.8584665407,0.0208135605288,0.0208146002451,0.0999052984815,0.0 1547800740000,99.9084269872,0.020812001214,0.00416198443418,0.0665990271434,0.0 1547800745000,98.9349371305,0.258911307917,0.488629396395,0.250720822364,0.0668013427939 1547800750000,96.5793391559,1.50209175675,1.06646201431,0.789412610731,0.0626944622742 1547800755000,94.7528342706,4.48834716317,0.392098083581,0.354226729519,0.0124937531234 1547800760000,93.6703390547,5.4425044412,0.862076450763,0.0167148181102,0.00836523527252 1547800765000,83.3114343843,15.3821396554,0.774564169709,0.5109305944,0.0209311962204"
benchmark1_b2 = "1547800730000,35442524,10107584,3745112 1547800735000,35442492,10107528,3745200 1547800740000,35442368,10107536,3745316 1547800745000,35133388,10407524,3754308 1547800750000,34535500,10926452,3833268 1547800755000,33974832,11105104,4215284 1547800760000,33303000,11216660,4775560 1547800765000,31604556,11437152,6253512"
benchmark2_a2 = "1547731215000,97.3169393279,1.77448441082,0.262951039257,0.645625221979,0.0 1547731220000,93.7924265328,3.16568788834,0.769263767368,2.27262181151,0.0 1547731225000,70.6182565104,27.7741939293,1.54058572754,0.054369374237,0.0125944584383 1547731230000,76.6809053617,22.9506409864,0.33084675752,0.0166583439986,0.0209485503603 1547731235000,88.9396777157,10.7681779655,0.212841930608,0.075137803765,0.00416458437448 1547731240000,80.0027377429,15.0345629215,4.9332163019,0.0294830336701,0.0 1547731245000,90.6351178592,6.49878108733,2.54397033615,0.301107596559,0.0210231207344"
benchmark2_b2 = "1547731215000,35898028,9824028,3573164 1547731220000,35773020,9824368,3697832 1547731225000,33029456,9826516,6439248 1547731230000,32929836,9826536,6538848 1547731235000,35767404,9825308,3702508 1547731240000,34619632,9827188,4848400 1547731245000,35762776,9827388,3705056"
# WordCount 30G30U CPU_overall
t3 = "30G30U"
benchmark1_a3 = "1547796285000,99.7960596444,0.02497346579,0.0291354502242,0.14983143963,0.0 1547796290000,99.8001883611,0.0124880326053,0.0124895921798,0.174834014102,0.0 1547796295000,97.0995329747,0.578422892654,1.11072209048,1.07301788176,0.138304160422 1547796300000,95.8814492616,2.85950586254,0.642827212452,0.612043169568,0.00417449384262 1547796305000,94.1921426958,3.96951104595,1.76332117576,0.058344315537,0.0166807669748 1547796310000,97.8659236396,0.108334922973,2.00490861989,0.0166645877588,0.00416822975282 1547796315000,96.7215686699,1.56574416907,1.55819905827,0.137800576721,0.0166875260743 1547796320000,86.6497507307,11.8816147029,0.887063653305,0.564837311227,0.0167336018618"
benchmark1_b3 = "1547796285000,31915624,13427108,3952488 1547796290000,31913792,13426996,3954432 1547796295000,31280528,14041984,3972708 1547796300000,30836208,14245988,4213024 1547796305000,30334780,14391744,4568696 1547796310000,30311152,14424328,4559740 1547796315000,30051328,14526480,4717412 1547796320000,28713904,14756852,5824464"
benchmark2_a3 = "1547796245000,97.9215078126,1.82395761704,0.246186628155,0.00834794223224,0.0 1547796250000,93.5860742178,5.4405832606,0.752191348989,0.221151172628,0.0 1547796255000,70.7930421935,27.7059356439,0.992858703297,0.4872149089,0.0209485503603 1547796260000,78.9496836565,20.6538634485,0.212953331628,0.175144297437,0.00835526590634 1547796265000,85.2193015144,13.5590345441,0.895247342712,0.322230571768,0.00418602704173 1547796270000,84.0647738257,14.125924977,1.34000532501,0.456638858313,0.0126570139117"
benchmark2_b3 = "1547796245000,31753040,13427044,4115136 1547796250000,31294424,13428616,4572180 1547796255000,28882388,13429540,6983292 1547796260000,28871292,13429576,6994352 1547796265000,30989768,13429592,4875860 1547796270000,31635088,13429828,4230304"
# WordCount 36G36U CPU_overall
t4 = "36G36U"
benchmark1_a4 = "1547774115000,99.9167473175,0.0208135605288,0.0166510563663,0.0457880656457,0.0 1547774120000,99.941723902,0.00832500832501,0.0124880323457,0.0374630573207,0.0 1547774125000,97.7668276104,0.599151198376,0.988813204959,0.511125147858,0.134082838377 1547774130000,97.297477654,0.488966900702,1.82208504508,0.3831119917,0.00835840855901 1547774135000,97.2869089974,0.154509233457,1.99243738717,0.561967272494,0.00417710944027 1547774140000,97.9694951953,0.0584623677644,1.93864848899,0.0333939479089,0.0 1547774145000,97.6083942993,0.0583782608576,2.02435357727,0.308873862593,0.0 1547774150000,97.9109550691,0.0458521149779,2.02235009591,0.0208427200574,0.0 1547774155000,94.9396504543,3.74502491626,0.724649751986,0.590674877466,0.0 1547774160000,90.6785620159,6.59371583385,1.9751255991,0.731684793478,0.0209117576762 1547774165000,87.0657763517,7.63530722323,3.91787349475,1.35179216768,0.0292507626092 1547774170000,97.7740413346,0.112701573485,1.89195227868,0.221304813212,0.0 1547774175000,96.9360773854,0.471621886775,2.54642925432,0.0458714735484,0.0 1547774180000,94.715784371,2.04423566493,3.17729024626,0.0588065243238,0.00388319353837 1547774185000,88.7341858979,8.48620452065,2.75026503123,0.0167453313438,0.0125992188484"
benchmark1_b4 = "1547774115000,35470436,9950052,3874732 1547774120000,35469892,9949368,3875960 1547774125000,34837476,10564336,3893408 1547774130000,34696540,10701924,3896756 1547774135000,34630512,10766908,3897800 1547774140000,34550876,10845244,3899100 1547774145000,34499708,10894896,3900616 1547774150000,34437344,10955888,3901988 1547774155000,34300000,10768392,4226828 1547774160000,33551272,10993036,4750912 1547774165000,32660696,11158820,5475704 1547774170000,32614668,11210292,5470260 1547774175000,32522160,11279168,5493892 1547774180000,32385316,11279188,5630716 1547774185000,31918748,11202716,6173756"
benchmark2_a4 = "1547774070000,98.9591139978,0.0749437921559,0.104088600217,0.861853609793,0.0 1547774075000,94.9053274133,4.50778201637,0.536693356675,0.050197213622,0.0 1547774080000,81.8866030372,16.9413124114,1.12626149625,0.0416354504877,0.00418760469012 1547774085000,72.5862397486,25.7978300485,0.708049025211,0.882736596325,0.0251445813427 1547774090000,81.9551144056,17.6438784083,0.292413682438,0.108593503668,0.0 1547774095000,83.7571497269,13.6192789645,2.31748040546,0.297723043913,0.00836785915487 1547774100000,87.7047320028,8.01184269696,3.98448748143,0.286295593782,0.0126422250316"
benchmark2_b4 = "1547774070000,35465244,9948624,3881352 1547774075000,35202760,9949408,4143052 1547774080000,34067872,9950948,5276400 1547774085000,32367380,9951916,6975924 1547774090000,35189128,9951204,4154888 1547774095000,34497972,9952404,4844844 1547774100000,35193040,9951816,4150364"
# WordCount 42G42U CPU_overall
t5 = "42G42U" 
benchmark1_a5 = "1547776165000,99.9458879651,0.0291370096688,0.0249750252347,0.0,0.0 1547776170000,99.9375634765,0.0166500167798,0.0208125210722,0.0249739856482,0.0 1547776175000,98.3209954065,0.506629034962,0.879360877939,0.117234549456,0.175780131157 1547776180000,95.6245586944,3.07214144794,0.790623792066,0.495931957405,0.0167441081669 1547776185000,93.5254462896,5.19763199895,0.885417163151,0.383149282411,0.00835526590634 1547776190000,97.1672499121,2.3779437855,0.162701402912,0.292104899486,0.0 1547776195000,83.4230788749,14.1245277311,1.05100841244,1.35100891828,0.0503760632871"
benchmark1_b5 = "1547776165000,35811356,9978732,3505132 1547776170000,35810928,9978400,3505892 1547776175000,35260544,10510632,3524044 1547776180000,34761336,10797312,3736572 1547776185000,34089372,11001368,4204480 1547776190000,33895260,11001380,4398580 1547776195000,32373840,11307976,5613404"
benchmark2_a5 = "1547776095000,97.9304011698,1.81931446459,0.241958317555,0.0083260480413,0.0 1547776100000,94.5300687736,3.46492535899,1.74081938687,0.255796514921,0.00838996560114 1547776105000,72.632903836,22.608609331,4.0372145939,0.716888004801,0.00438423429348 1547776110000,81.6620569517,0.624593107847,16.0638518889,1.64949805155,0.0 1547776115000,71.8127731398,3.08337163277,24.4062390955,0.686859974046,0.0107561579004 1547776120000,75.26465813,7.67300425853,16.8576147831,0.20472282831,0.0 1547776125000,71.2639867274,14.2451789674,14.3409450856,0.140372207925,0.00951701165834 1547776130000,64.9422244693,16.7797109337,18.1432548522,0.11750198002,0.0173077647901 1547776135000,63.9465832961,16.3922294766,19.6051348254,0.0415352832536,0.0145171185803 1547776140000,68.3298054974,25.7976223046,5.53820783658,0.31649605087,0.0178683105512 1547776145000,64.2880230102,23.5285245738,12.1124926987,0.0709597173073,0.0 1547776150000,81.8442339138,15.3492864356,2.4457692195,0.339112486171,0.021597944942"
benchmark2_b5 = "1547776095000,35799592,9978432,3517196 1547776100000,35524876,9979376,3790968 1547776105000,33757904,9980520,5556796 1547776110000,33598632,9980532,5716056 1547776115000,33525936,9980536,5788748 1547776120000,33404556,9980540,5910124 1547776125000,33393196,9980468,5921556 1547776130000,32235164,9982892,7077164 1547776135000,32214044,9982948,7098228 1547776140000,32278308,9982624,7034288 1547776145000,31789244,9983244,7522732 1547776150000,35181880,9981792,4131548"
# WordCount 48G48U CPU_overall
t6 = "48G48U" 
benchmark1_a6 = "1547780250000,99.9167530346,0.0457859868622,0.033298994103,0.0,0.00416198443418 1547780255000,99.9500561855,0.0124854338337,0.0124854338337,0.0249729468405,0.0 1547780260000,97.7047398224,0.435542531143,1.76338851799,0.0125675505844,0.0837615779322 1547780265000,96.2275179918,2.1396047881,0.860297023524,0.760054600436,0.0125255961241 1547780270000,93.2117830438,4.22735418848,1.27590247637,1.27662278923,0.00833750208438 1547780275000,96.1956667978,1.24022592543,1.66457640967,0.891183927711,0.00834693943507 1547780280000,94.8598247438,3.91325519852,0.538995770984,0.662893490813,0.025030795846"
benchmark1_b6 = "1547780250000,32144392,12891484,4259344 1547780255000,32144496,12890996,4259728 1547780260000,31545940,13458824,4290456 1547780265000,31128568,13709908,4456744 1547780270000,30559452,13869200,4866568 1547780275000,30397140,13913976,4984104 1547780280000,29786372,14181320,5327528"
benchmark2_a6 = "1547780215000,98.3561917498,1.43524278235,0.175186238072,0.0333792297743,0.0 1547780220000,93.2566519754,6.05410351177,0.639242826812,0.0500016859778,0.0 1547780225000,70.1038326881,27.8154312765,1.01793839149,1.04184909355,0.0209485503603 1547780230000,79.8379491217,19.6314236952,0.154579341489,0.367690480924,0.00835736074548 1547780235000,81.3304359838,14.1384835949,0.927816819731,3.59908125108,0.00418235048097 1547780240000,84.3171001967,14.368095458,1.16761368781,0.134610236571,0.0125804209362"
benchmark2_b6 = "1547780215000,32021448,12891576,4382196 1547780220000,31462488,12891624,4941108 1547780225000,29107876,12893200,7294144 1547780230000,29098248,12893212,7303760 1547780235000,31234900,12893584,5166736 1547780240000,31863936,12894456,4536828"

plt.figure(1)
plt.suptitle(benchmark1, color="blue")
benchmark1_t = []
for i in range(1,7):
    a = locals()['benchmark1_a'+str(i)].split(" ")
    x = []
    y_a = []
    l = 0   
    for n in a:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_a.append(float('%.2f' % (float(m[2])+float(m[3]))))
    benchmark1_t.append(x[-1])
    b = locals()['benchmark1_b'+str(i)].split(" ")
    x = []
    y_b = []
    l = 0  
    for n in b:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_b.append(float('%.2f' % (float(m[2])+float(m[3]))) / float('%.2f' % (float(m[1]) + float(m[2]) + float(m[3]))) * 100)
    locals()['ax'+str(i)] = plt.subplot(2,3,i)
    locals()['ax'+str(i)].set_title(locals()['t'+str(i)])
    x_axix, y_axix = (x, y_a)
    plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x', label='CPU')
    x_axix, y_axix = (x, y_b)
    plt.plot(x_axix, y_axix, linewidth = '2', color='red', marker='o', label='RAM')
    
    ax = plt.gca()
    ax.set_ylim(0,100)
    if (i>3):
        plt.xlabel('time(sec)', fontsize=12)
    if (i==1 or i==4):
        plt.ylabel('resource usage(%)', fontsize=12)
    plt.legend()
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
# plt.show()
print benchmark1_t

benchmark2_t = []
plt.figure(2)
plt.suptitle(benchmark2, color="blue")
for i in range(1,7):
    a = locals()['benchmark2_a'+str(i)].split(" ")
    x = []
    y_a = []
    l = 0   
    for n in a:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_a.append(float('%.2f' % (float(m[2])+float(m[3]))))
    benchmark2_t.append(x[-1])
    b = locals()['benchmark2_b'+str(i)].split(" ")
    x = []
    y_b = []
    l = 0  
    for n in b:   
        l = l + 1        
        m = n.split(",")          
        x.append(5*int(l))
        y_b.append(float('%.2f' % (float(m[2])+float(m[3]))) / float('%.2f' % (float(m[1]) + float(m[2]) + float(m[3]))) * 100)
    locals()['ax'+str(i)] = plt.subplot(2,3,i)
    locals()['ax'+str(i)].set_title(locals()['t'+str(i)])
    x_axix, y_axix = (x, y_a)
    plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x', label='CPU')
    x_axix, y_axix = (x, y_b)
    plt.plot(x_axix, y_axix, linewidth = '2', color='red', marker='o', label='RAM')
    
    ax = plt.gca()
    ax.set_ylim(0,100)
    if (i>3):
        plt.xlabel('time(sec)', fontsize=12)
    if (i==1 or i==4):
        plt.ylabel('resource usage(%)', fontsize=12)
    plt.legend()
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
print benchmark2_t

plt.figure(3,figsize=(12, 6))
plt.suptitle("Configuration-performance curve", color="green")
x = []
for i in range(1,7):
    x.append(locals()['t'+str(i)])
ax1 = plt.subplot(1,2,1)
ax1.set_title(benchmark1)
y_a = benchmark1_t
x_axix, y_axix = (x, y_a)
plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x')
ax = plt.gca()
ax.set_ylim(0,100)
plt.xlabel('configuration', fontsize=12)
plt.ylabel('job running time (sec)', fontsize=12)
plt.legend()
ax1 = plt.subplot(1,2,2)
ax1.set_title(benchmark2)
y_b = benchmark2_t
x_axix, y_axix = (x, y_b)
plt.plot(x_axix, y_axix, linewidth = '2', color='black', marker='x')
ax = plt.gca()
ax.set_ylim(0,100)
plt.xlabel('configuration', fontsize=12)
plt.ylabel('job running time (sec)', fontsize=12)
plt.legend()

plt.show()