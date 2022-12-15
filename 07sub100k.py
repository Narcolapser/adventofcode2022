# got with du * -b | sort -h
dirs = """6729	wdtm/mrnhn
13102	pcqjnl/lrrl/mrnhn/hghjzpgc/mgnq/ttmctqlc
15810	wdtm/cpcqz/lrrl/sdvhlnz/wdwgp
19112	pcqjnl/lrrl/dcfmtw/nzpdtfr/vcthd
19414	wdtm/vpm/qsmg/vbvtzmsg
20204	wdtm/vpm/dhmphrn/lrrl/gqqsg/hzfmdhw/lvdhtg/pbfhn/mjfdjrgt
21650	wdtm/cpcqz/cfhjvmh
24300	wdtm/vpm/dhmphrn/lrrl/gqqsg/hzfmdhw/lvdhtg/pbfhn
26971	pcqjnl/lrrl/sqpgr/bpnlrhsb
27241	pcqjnl/lrrl/nwjggvr/zvlhngjm/qsvwfb
27903	pcqjnl/qgpr/jzmpcc/mrnhn/gphqmvpn
30169	wdtm/vpm/dhmphrn/mrcnm/mjfdjrgt
30644	pcqjnl/qgpr/lrrl
33072	pcqjnl/lqwntmdg/rfqbmb/mnd
37015	wdtm/nvgmrpdf
49472	wdtm/gmrgsmpp/fbcv/htmwl
54771	pcqjnl/lrrl/sqpgr/zplwvj/gtd
58867	pcqjnl/lrrl/sqpgr/zplwvj
60071	wdtm/vpm/dhmphrn/lrrl/pdtm
62043	pcqjnl/lrrl/nwjggvr/zvlhngjm/fjt
62485	vllgn
66258	wdtm/vpm/nbccdd
68377	jvdqjhr.jvp
69775	pcqjnl/lrrl/wgpqg
75447	pcqjnl/lrrl/nwjggvr/bwmglvmt/lrrl/bzrs
77691	pcqjnl/lrrl/dcfmtw/nzpdtfr/qwtwps/cmf
81787	pcqjnl/lrrl/dcfmtw/nzpdtfr/qwtwps
88034	wdtm/ztp/wdtm/vnmg
88822	pcqjnl/qgpr/fhnnc
90942	sqhw/mjfdjrgt/hlgqdqb/mjfdjrgt
92130	wdtm/ztp/wdtm
94844	ppwv.zsh
96606	sqhw/dqnhzbh/cmfhw/dsbjlmrf
97889	rqpw
99557	pcqjnl/lrrl/sqpgr/jvdh"""

print(sum([int(line.split('\t')[0]) for line in dirs.split('\n')]))

# produces: 1889204 which is to high. groan. 
