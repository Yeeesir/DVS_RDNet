#!/usr/bin/env python3
from glob import glob
import os
import numpy as np
from dv import AedatFile


def select_events(aedat_dir):
    f_txt = open(os.path.join(aedat_dir, 'ts.txt'), 'w')
    all_imgs_path = glob(os.path.join(aedat_dir, 'img*.png'))
    aedat_file = glob(os.path.join(aedat_dir, '*.aedat4'))[0]
    with AedatFile(aedat_file) as f:
        event_h, event_w = f['events'].size
        events = np.hstack([packet for packet in f['events'].numpy()])
        imgs = []
        for img in f['frames']:
            imgs.append(img)

    for selected_img_path in all_imgs_path:
        img_index = int(os.path.basename(selected_img_path)[len('img'):-len('.png')])
        start_ts = imgs[img_index].timestamp_start_of_exposure
        end_ts = imgs[img_index].timestamp_end_of_exposure
        f_txt.writelines('{} {} {}\n'.format(img_index, start_ts, end_ts))

        events_index = np.where(np.logical_and(events['timestamp'] >= start_ts, events['timestamp'] <= end_ts))
        selected_events = events[events_index]

        selected_events = np.hstack((selected_events['timestamp'].reshape(-1, 1), selected_events['x'].reshape(-1, 1), selected_events['y'].reshape(-1, 1), selected_events['polarity'].reshape(-1, 1)))

        # save events
        selected_events.tofile(selected_img_path.replace(os.path.basename(selected_img_path), 'events{}.bin'.format(img_index)))
    f.close()


if __name__ == '__main__':
    data_path = './data/*/'
    aedat_dirs = glob(os.path.join(data_path, 'dvSave*'))
    for aedat_dir in aedat_dirs:
        print(aedat_dir)
        select_events(aedat_dir)

