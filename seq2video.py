import argparse
import cv2
import glob
import os
import os.path as osp

parser = argparse.ArgumentParser(description='Convert image sequence to video')
parser.add_argument('--img-dir', '-d', type=str, help='image sequence directory')
parser.add_argument('--fps', '-f', type=int, default=25, help='frame rates')
parser.add_argument('--video-path', '-p', type=str, help='video path')

def main():
    args = parser.parse_args()
    paths = list(sorted(glob.glob(osp.join(args.img_dir, '*'))))
    writer = None
    for path in paths:
        im = cv2.imread(path)
        if writer is None:
            h, w, _ = im.shape
            writer = cv2.VideoWriter(args.video_path, cv2.VideoWriter_fourcc(*'mp4v'), args.fps, (w, h))
        writer.write(im)

if __name__ == '__main__':
    main()