#!/usr/bin/env python3
from dv import AedatFile, Frame
import numpy as np
import cv2
import os, shutil
from glob import glob
from raw_tools import raw2bgr

def gen_events_array(events_ori, C_event, start_time, end_time, event_h, event_w):
    duration = end_time - start_time + 1
    events = np.zeros((event_h, event_w, C_event))
    C_inter = duration / C_event
    for i in range(events_ori.shape[0]):
        t, W, H, p, _p1, _p2 = events_ori[i]
        if t < start_time:
            continue
        elif t > end_time:
            break
        else:
            p = -1 if p == 0 else p
        events[int(H), int(W), min(int((t - start_time) // C_inter), C_event - 1)] += p
    return events


def parse_aedat(aedat_path, save_image=True, save_events=False):
    save_dir = aedat_path[:-len('.aedat4')]
    print(save_dir)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with AedatFile(aedat_path) as f:
        event_h, event_w = f['events'].size
        events = np.hstack([packet for packet in f['events'].numpy()])
        imgs = []
        for img in f['frames']:
            imgs.append(img)

        for i, img in enumerate(imgs):
            if save_events:
                start_time = img.timestamp_start_of_exposure
                end_time = img.timestamp_end_of_exposure
                events_array = gen_events_array(events, 5, start_time, end_time, event_h, event_w)
                event_thre = 5
                events_array = (events_array.clip(-event_thre, event_thre) + event_thre) / (2 * event_thre)

                # save_events
                for i in range(events_array.shape[-1]):
                    cv2.imwrite('exp_event{}.png'.format(i), (events_array[..., i:i+1] * 255).astype(np.uint8))
            
            if save_image:
                if img.image.shape[-1] == 3:
                    # save bgr
                    cv2.imwrite(os.path.join(save_dir, 'img{}.png'.format(i)), img.image)

                    

    shutil.move(aedat_path, os.path.join(save_dir, os.path.basename(aedat_path)))


if __name__ == '__main__':
    aedat_dir = './data/lux300_40ms/'
    aedat_files = glob(os.path.join(aedat_dir, '*.aedat4'))

    for aedat_file in aedat_files:
        print(aedat_file)
        parse_aedat(aedat_file, save_image=True, save_events=False)


# vim: ts=4 sw=4 sts=4 expandtab
