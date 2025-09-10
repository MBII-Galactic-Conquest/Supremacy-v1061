DEVELOPER DOCS

git bash
python pbadjust.py *.mbch, *.mbch~+
OR
python pbadjust.py (apply to all)

Apply
//PBADJUST #:#
Above your point buy builds to automatically adjust entries

X:Y

X = Amount of entries per block
Y = The gap size of entries

Each spec build has 14 possible entries.
0->14
15->29
30-44

EXAMPLE:
//PBADJUST 10:4
Will work if your latest entry is

c_att_skill_0
c_att_names_0
c_att_ranks_0
c_att_skill_1
c_att_names_1
c_att_ranks_1
c_att_skill_2
c_att_names_2
c_att_ranks_2
c_att_skill_3
c_att_names_3
c_att_ranks_3
c_att_skill_4
c_att_names_4
c_att_ranks_4
c_att_skill_5
c_att_names_5
c_att_ranks_5
c_att_skill_6
c_att_names_6
c_att_ranks_6
c_att_skill_7
c_att_names_7
c_att_ranks_7
c_att_skill_8
c_att_names_8
c_att_ranks_8
c_att_skill_9
c_att_names_9
c_att_ranks_9
c_att_skill_10
c_att_names_10
c_att_ranks_10

So let's say you have three spec builds, you would essentially run the script with the FA code looking like so:

//PBADJUST 10:4
c_att_skill_0
c_att_names_0
c_att_ranks_0
c_att_skill_1
c_att_names_1
c_att_ranks_1
c_att_skill_2
c_att_names_2
c_att_ranks_2
c_att_skill_3
c_att_names_3
c_att_ranks_3
c_att_skill_4
c_att_names_4
c_att_ranks_4
c_att_skill_5
c_att_names_5
c_att_ranks_5
c_att_skill_6
c_att_names_6
c_att_ranks_6
c_att_skill_7
c_att_names_7
c_att_ranks_7
c_att_skill_8
c_att_names_8
c_att_ranks_8
c_att_skill_9
c_att_names_9
c_att_ranks_9
c_att_skill_10
c_att_names_10
c_att_ranks_10
c_att_skill_0
c_att_names_0
c_att_ranks_0
c_att_skill_1
c_att_names_1
c_att_ranks_1
c_att_skill_2
c_att_names_2
c_att_ranks_2
c_att_skill_3
c_att_names_3
c_att_ranks_3
c_att_skill_4
c_att_names_4
c_att_ranks_4
c_att_skill_5
c_att_names_5
c_att_ranks_5
c_att_skill_6
c_att_names_6
c_att_ranks_6
c_att_skill_7
c_att_names_7
c_att_ranks_7
c_att_skill_8
c_att_names_8
c_att_ranks_8
c_att_skill_9
c_att_names_9
c_att_ranks_9
c_att_skill_10
c_att_names_10
c_att_ranks_10
c_att_skill_0
c_att_names_0
c_att_ranks_0
c_att_skill_1
c_att_names_1
c_att_ranks_1
c_att_skill_2
c_att_names_2
c_att_ranks_2
c_att_skill_3
c_att_names_3
c_att_ranks_3
c_att_skill_4
c_att_names_4
c_att_ranks_4
c_att_skill_5
c_att_names_5
c_att_ranks_5
c_att_skill_6
c_att_names_6
c_att_ranks_6
c_att_skill_7
c_att_names_7
c_att_ranks_7
c_att_skill_8
c_att_names_8
c_att_ranks_8
c_att_skill_9
c_att_names_9
c_att_ranks_9
c_att_skill_10
c_att_names_10
c_att_ranks_10

Because 10:4 implies that 0->10 is your options, but +1 as 0 is essentially a positive integer in this usecase.
Meaning that if you do //PBADJUST 10:4 your results would come out like so, placing _15 immediately after your _10th entry, because 11 + 4 = 15:

//PBADJUST 10:4
c_att_skill_0
c_att_names_0
c_att_ranks_0
c_att_skill_1
c_att_names_1
c_att_ranks_1
c_att_skill_2
c_att_names_2
c_att_ranks_2
c_att_skill_3
c_att_names_3
c_att_ranks_3
c_att_skill_4
c_att_names_4
c_att_ranks_4
c_att_skill_5
c_att_names_5
c_att_ranks_5
c_att_skill_6
c_att_names_6
c_att_ranks_6
c_att_skill_7
c_att_names_7
c_att_ranks_7
c_att_skill_8
c_att_names_8
c_att_ranks_8
c_att_skill_9
c_att_names_9
c_att_ranks_9
c_att_skill_10
c_att_names_10
c_att_ranks_10
c_att_skill_15 <--- ***
c_att_names_15
c_att_ranks_15
c_att_skill_16
c_att_names_16
c_att_ranks_16
c_att_skill_17
c_att_names_17
c_att_ranks_17
c_att_skill_18
c_att_names_18
c_att_ranks_18
c_att_skill_19
c_att_names_19
c_att_ranks_19
c_att_skill_20
c_att_names_20
c_att_ranks_20
c_att_skill_21
c_att_names_21
c_att_ranks_21
c_att_skill_22
c_att_names_22
c_att_ranks_22
c_att_skill_23
c_att_names_23
c_att_ranks_23
c_att_skill_24
c_att_names_24
c_att_ranks_24
c_att_skill_25
c_att_names_25
c_att_ranks_25
c_att_skill_30 <--- ***
c_att_names_30
c_att_ranks_30
c_att_skill_31
c_att_names_31
c_att_ranks_31
c_att_skill_32
c_att_names_32
c_att_ranks_32
c_att_skill_33
c_att_names_33
c_att_ranks_33
c_att_skill_34
c_att_names_34
c_att_ranks_34
c_att_skill_35
c_att_names_35
c_att_ranks_35
c_att_skill_36
c_att_names_36
c_att_ranks_36
c_att_skill_37
c_att_names_37
c_att_ranks_37
c_att_skill_38
c_att_names_38
c_att_ranks_38
c_att_skill_39
c_att_names_39
c_att_ranks_39
c_att_skill_40
c_att_names_40
c_att_ranks_40

-- Up to 44 <--- ***

