F_dis = 48000
n_mfcc = 20
mfcc_frame = 170
f_min = 90
f_max = 5000
win_len = int(2*(1/f_min)*F_dis)
hop_len = int(0.01*F_dis)
