
lookup_table = [
    # 2
    ['AB'], ['AC'], ['AD'], ['AE'], ['AF'], ['AG'], ['AH'],
    ['BC'], ['BD'], ['BE'], ['BF'], ['BG'], ['BH'],
    ['CD'], ['CE'], ['CF'], ['CG'], ['CH'],
    ['DE'], ['DF'], ['DG'], ['DH'],
    ['EF'], ['EG'], ['EH'],
    ['FG'], ['FH'],
    ['GH'],

    # 3
    ['ABC'], ['ABD'], ['ABE'], ['ABF'], ['ABG'], ['ABH'], ['ACD'], ['ACE'], ['ACF'], ['ACG'], ['ACH'], ['ADE'], ['ADF'], ['ADG'], ['ADH'], ['AEF'], ['AEG'], ['AEH'], ['AFG'], ['AFH'], ['AGH'],
    ['BCD'], ['BCE'], ['BCF'], ['BCG'], ['BCH'], ['BDE'], ['BDF'], ['BDG'], ['BDH'], ['BEF'], ['BEG'], ['BEH'], ['BFG'], ['BFH'], ['BGH'],
    ['CDE'], ['CDF'], ['CDG'], ['CDH'], ['CEF'], ['CEG'], ['CEH'], ['CFG'], ['CFH'], ['CGH'],
    ['DEF'], ['DEG'], ['DEH'], ['DFG'], ['DFH'], ['DGH'],
    ['EFG'], ['EFH'], ['EGH'],
    ['FGH'],

    # 4
    ['ABCD'], ['ABCE'], ['ABCF'], ['ABCG'], ['ABCH'], ['ABDE'], ['ABDF'], ['ABDG'], ['ABDH'], ['ABEF'], ['ABEG'], ['ABEH'],
    ['ABFG'], ['ABFH'], ['ABGH'],
    ['ACDE'], ['ACDF'], ['ACDG'], ['ACDH'], ['ACEF'], ['ACEG'], ['ACEH'], ['ACFG'], ['ACFH'], ['ACGH'],
    ['ADEF'], ['ADEG'], ['ADEH'], ['ADFG'], ['ADFH'], ['ADGH'],
    ['AEFG'], ['AEFH'], ['AEGH'],
    ['AFGH'],

    ['BCDE'], ['BCDF'], ['BCDG'], ['BCDH'], ['BCEF'], ['BCEG'], ['BCEH'], ['BCFG'], ['BCFH'], ['BCGH'],
    ['BDEF'], ['BDEG'], ['BDEH'], ['BDFG'], ['BDFH'], ['BDGH'],
    ['BEFG'], ['BEFH'], ['BEGH'],
    ['BFGH'],

    ['CDEF'], ['CDEG'], ['CDEH'], ['CDFG'], ['CDFH'], ['CDGH'],
    ['CEFG'], ['CEFH'], ['CEGH'],
    ['CFGH'],

    ['DEFG'], ['DEFH'], ['DEGH'],
    ['DFGH'],

    # 5
    ['ABCDE'], ['ABCDF'], ['ABCDG'], ['ABCDH'], ['ABCEF'], ['ABCEG'], ['ABCEH'], ['ABCFG'], ['ABCFH'], ['ABCGH'], ['ABDEF'], ['ABDEG'], ['ABDEH'],
    ['ABDFG'], ['ABDFH'], ['ABDGH'],
    ['ABEFG'], ['ABEFH'], ['ABEGH'],
    ['ABFGH'],

    ['ACDEF'], ['ACDEG'], ['ACDEH'], ['ACDFG'], ['ACDFH'], ['ACDGH'],
    ['ACEFG'], ['ACEFH'], ['ACEGH'],
    ['ACFGH'],

    ['ADEFG'], ['ADEFH'], ['ADEGH'],
    ['ADFGH'],

    ['AEFGH'],

    ['BCDEF'], ['BCDEG'], ['BCDEH'], ['BCDFG'], ['BCDFH'], ['BCDGH'],
    ['BCEFG'], ['BCEFH'], ['BCEGH'],
    ['BCFGH'],

    ['BDEFG'], ['BDEFH'], ['BDEGH'],
    ['BDFGH'],

    ['BEFGH'],

    ['CDEFG'], ['CDEFH'], ['CDEGH'], ['CDFGH'],
    ['CEFGH'],

    ['DEFGH'],

    # 6
    ['ABCDEF'], ['ABCDEG'], ['ABCDEH'], ['ABCDFG'], ['ABCDFH'], ['ABCDGH'],
    ['ABCEFG'], ['ABCEFH'], ['ABCEGH'], ['ABCFGH'],
    ['ABDEFG'], ['ABDEFH'], ['ABDEGH'],
    ['ABDFGH'], ['ABEFGH'],
    ['ACDEFG'], ['ACDEFH'], ['ACDEGH'], ['ACDFGH'],
    ['ACEFGH'],
    ['ADEFGH'],
    ['BCDEFG'], ['BCDEFH'], ['BCDEGH'], ['BCDFGH'],
    ['BCEFGH'],
    ['BDEFGH'],
    ['CDEFGH'],

    # 7
    ['ABCDEFG'], ['ABCDEFH'], ['ABCDEGH'], ['ABCDFGH'],
    ['ABCEFGH'],
    ['ACDEFGH'],
    ['BCDEFGH'],

    # 8
    ['ABCDEFGH']
]

def range_fixer(ranges):
    print(len(ranges))
    # 整理范围顺序 左小右大
    # right_range = []
    # for range_id in range(len(ranges)):
    #     if ranges[range_id][0]>ranges[range_id][1]:
    #         right_range.append([ranges[range_id][1],ranges[range_id][0]])
    #     else:
    #         right_range.append(ranges[range_id])

    # 比较范围
    # for range_id in range(len(right_range)):
    #     try:
    #         if right_range[range_id][1]>right_range[range_id+1][0]:
    #             print(right_range[range_id],right_range[range_id+1],'true')
    #         else:
    #             print('false')
    #     except:
    #         pass
    

range_1 = {
    'A':[1.001, 9.002],
    'B':[50.002,2.001],
    'C':[70.001, 100.002],
    'D':[130.001, 220.002],
    'E':[250.001, 310.002],
    'F':[10.001, 130.002],
    'G':[55.001, 310.002],
    'H':[150.001, 210.002]
}

range_fixer(range_1)
