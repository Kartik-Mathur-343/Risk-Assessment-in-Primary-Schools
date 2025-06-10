 1. Info
    Column                          Non-Null Count  Dtype---  ------                          --------------  -----
 0   StudentID                       2000 non-null   int64
 1   TextLevel-01-SOY                2000 non-null   int64
 2   TextLevel-01-MOY                2000 non-null   int64
 3   TextLevel-01-EOY                2000 non-null   int64
 4   TextLevel-02-SOY                2000 non-null   int64
 5   TextLevel-02-MOY                2000 non-null   int64
 6   TextLevel-02-EOY                2000 non-null   int64
 7   WritingVocab-01-SOY             2000 non-null   int64
 8   HRSIW-01-SOY                    2000 non-null   int64
 9   Counting-01                     2000 non-null   int64
 10  Counting-02                     2000 non-null   int64
 11  Place Value-01                  2000 non-null   int64
 12  Place Value-02                  2000 non-null   int64
 13  Addition and Subtraction-01     2000 non-null   int64
 14  Addition and Subtraction-02     2000 non-null   int64
 15  Multiplication and Division-01  2000 non-null   int64
 16  Multiplication and Division-02  2000 non-null   int64
 17  Kinder_Age                      2000 non-null   float64
 18  Gender                          2000 non-null   object
 19  Disability_Non-disable          2000 non-null   int64
 20  Disability_Cognitive            2000 non-null   int64
 21  Disability_Physical             2000 non-null   int64
 22  Disability_Sensory              2000 non-null   int64
 23  Disability_SocialEmotional      2000 non-null   int64
 24  NCCD-Funded                     2000 non-null   int64
 25  NumSibling                      2000 non-null   int64
 26  SiblingOrder                    2000 non-null   int64
 27  01.SES                          2000 non-null   int64
 28  02.SES                          2000 non-null   int64
 29  NumAbvYear9                     2000 non-null   int64
 30  NumAbvDiploma                   2000 non-null   int64
 31  NumProf                         2000 non-null   int64
 32  Year_02                         2000 non-null   int64
 33  At_Risk_Numeracy                2000 non-null   bool
dtypes: bool(1), float64(1), int64(31), object(1)
memory usage: 517.7+ KB
None


2. DESCRIPTION
          StudentID  TextLevel-01-SOY  TextLevel-01-MOY  TextLevel-01-EOY  \
count  2.000000e+03        2000.00000       2000.000000         2000.0000
mean   5.459580e+08          10.69900         15.001500           21.1300
std    2.580928e+08           6.10082          5.489496            4.5786
min    1.006692e+08          -4.00000          0.000000            4.0000
25%    3.163839e+08           6.00000         11.000000           18.0000
50%    5.469370e+08          10.00000         14.000000           21.0000
75%    7.670611e+08          14.00000         18.000000           24.0000
max    9.998723e+08          34.00000         33.000000           34.0000
       TextLevel-02-SOY  TextLevel-02-MOY  TextLevel-02-EOY  \
count       2000.000000        2000.00000       2000.000000
mean          21.786500          24.07300         26.998500
std            5.220205           4.69134          3.765314
min            2.000000           5.00000          5.000000
25%           18.000000          21.00000         25.000000
50%           22.000000          24.00000         28.000000
75%           25.000000          28.00000         30.000000
max           36.000000          34.00000         33.000000
       WritingVocab-01-SOY  HRSIW-01-SOY  Counting-01  Counting-02  \
count          2000.000000   2000.000000  2000.000000  2000.000000
mean             22.018500     30.508000     1.758000     2.850500
std              12.679098     10.020686     0.935881     1.072719
min               0.000000     -3.000000     0.000000     0.000000
25%              13.000000     25.000000     1.000000     2.000000
50%              20.000000     32.000000     2.000000     3.000000
75%              29.000000     37.000000     2.000000     4.000000
max              95.000000     58.000000     5.000000     6.000000
       Place Value-01  Place Value-02  Addition and Subtraction-01  \
count     2000.000000     2000.000000                  2000.000000
mean         1.028500        1.681500                     1.290500
std          0.529932        0.639736                     0.935172
min          0.000000        0.000000                     0.000000
25%          1.000000        1.000000                     1.000000
50%          1.000000        2.000000                     1.000000
75%          1.000000        2.000000                     2.000000
max          4.000000        5.000000                     5.000000
       Addition and Subtraction-02  Multiplication and Division-01  \
count                  2000.000000                     2000.000000
mean                      2.257500                        1.075500
std                       1.155795                        0.837944
min                       0.000000                        0.000000
25%                       2.000000                        0.000000
50%                       2.000000                        1.000000
75%                       3.000000                        2.000000
max                       6.000000                        4.000000
       Multiplication and Division-02   Kinder_Age  Disability_Non-disable  \
count                     2000.000000  2000.000000             2000.000000
mean                         1.797500     5.276805                0.690500
std                          0.771875     0.347251                0.462403
min                          0.000000     4.504110                0.000000
25%                          2.000000     5.015753                0.000000
50%                          2.000000     5.282192                1.000000
75%                          2.000000     5.534247                1.000000
max                          5.000000     6.534247                1.000000
       Disability_Cognitive  Disability_Physical  Disability_Sensory  \
count           2000.000000          2000.000000         2000.000000
mean               0.234500             0.033500            0.005000
std                0.423792             0.179983            0.070551
min                0.000000             0.000000            0.000000
25%                0.000000             0.000000            0.000000
50%                0.000000             0.000000            0.000000
75%                0.000000             0.000000            0.000000
max                1.000000             1.000000            1.000000
       Disability_SocialEmotional  NCCD-Funded   NumSibling  SiblingOrder  \
count                 2000.000000  2000.000000  2000.000000   2000.000000
mean                     0.036500     0.089000     2.356500      1.748500
std                      0.187578     0.284815     0.993932      0.865229
min                      0.000000     0.000000     1.000000      1.000000
25%                      0.000000     0.000000     2.000000      1.000000
50%                      0.000000     0.000000     2.000000      2.000000
75%                      0.000000     0.000000     3.000000      2.000000
max                      1.000000     1.000000     7.000000      6.000000
          01.SES       02.SES  NumAbvYear9  NumAbvDiploma      NumProf  \
count  2000.0000  2000.000000  2000.000000    2000.000000  2000.000000
mean    102.9415   102.117500     1.564000       0.886500     0.766500
std       9.3859     9.150167     0.725374       0.837836     0.811977
min      78.0000    78.000000     0.000000       0.000000     0.000000
25%      95.0000    95.000000     1.000000       0.000000     0.000000
50%     101.0000   101.000000     2.000000       1.000000     1.000000
75%     113.0000   109.000000     2.000000       2.000000     1.000000
max     120.0000   120.000000     3.000000       2.000000     2.000000
           Year_02
count  2000.000000
mean   2018.640000
std       1.664568
min    2016.000000
25%    2017.000000
50%    2018.000000
75%    2020.000000
max    2021.000000


3. columns
(0, 'StudentID')
(1, 'TextLevel-01-SOY')   
(2, 'TextLevel-01-MOY')   
(3, 'TextLevel-01-EOY')   
(4, 'TextLevel-02-SOY')   
(5, 'TextLevel-02-MOY')   
(6, 'TextLevel-02-EOY')   
(7, 'WritingVocab-01-SOY')
(8, 'HRSIW-01-SOY')       
(9, 'Counting-01')
(10, 'Counting-02')
(11, 'Place Value-01')
(12, 'Place Value-02')
(13, 'Addition and Subtraction-01')
(14, 'Addition and Subtraction-02')
(15, 'Multiplication and Division-01')
(16, 'Multiplication and Division-02')
(17, 'Kinder_Age')
(18, 'Gender')
(19, 'Disability_Non-disable')
(20, 'Disability_Cognitive')
(21, 'Disability_Physical')
(22, 'Disability_Sensory')
(23, 'Disability_SocialEmotional')
(24, 'NCCD-Funded')
(25, 'NumSibling')
(26, 'SiblingOrder')
(27, '01.SES')
(28, '02.SES')
(29, 'NumAbvYear9')
(30, 'NumAbvDiploma')
(31, 'NumProf')
(32, 'Year_02')
(33, 'At_Risk_Numeracy')