import numpy as np
import cv2
from glob import glob

def gen_events_array(events_ori, C_event, duration, event_h, event_w):
    events = np.zeros((event_h, event_w, C_event))
    C_inter = duration / C_event
    for i in range(events_ori.shape[0]):
        t, W, H, p = events_ori[i]

        p = -1 if p == 0 else p
        events[int(H), int(W), min(int(t // C_inter), C_event - 1)] += p
    return events

def vis_event(gray):
    h,w = gray.shape
    out = 255*np.ones([h,w,3])
    pos_weight = gray.copy()
    neg_weight = gray.copy()

    pos_weight[pos_weight<0]=0
    pos_weight = pos_weight*2*255

    neg_weight[neg_weight>0]=0
    neg_weight = abs(neg_weight)*2*255
    out[...,1] = out[...,1]-pos_weight-neg_weight
    out[...,0 ]-=pos_weight
    out[...,2 ]-=neg_weight
    out = out.clip(0,255)
    return out.astype(np.uint8)

if __name__=='__main__':

    event_file_list = glob('./data/*/*/*.bin')
    img_list = glob('./data/*/*/img*.png')
    img = cv2.imread(img_list[0]) 
    event_h, event_w, _ = img.shape
    C_event = 5
    for eventname in event_file_list:
        events_ori = np.fromfile(eventname, dtype=np.int64).reshape(-1, 4)
        if len(events_ori)==0:
            continue
        events_ori[:,0] = events_ori[:,0]-events_ori[:,0].min()
        events_ori[:,3] = (events_ori[:,3]-0.5)*2
        duration = events_ori[:,0].max()-events_ori[:,0].min()
        events = gen_events_array(events_ori, C_event, duration, event_h, event_w)

        events_vis = events.clip(-5,5)/10
        cv2.imwrite(eventname.replace('.bin','_vis.png'),vis_event(events_vis[...,2]))
