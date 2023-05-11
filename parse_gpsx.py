import gpxpy
import gpxpy.gpx
import pandas as pd 
import numpy as np
import datetime
from backports.datetime_fromisoformat import MonkeyPatch
MonkeyPatch.patch_fromisoformat()


def main():
    gpx_file = open('Morning_Ride.gpx', 'r')
    save_file = 'ride1.csv'
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                time = str(point.time).split(' ')[1]
                time = str(time).split('+')[0]
                triple = f'{point.latitude},{point.longitude},{time}\n'
                points.append(triple)
    
    with open(save_file, "w") as f:
        f.write('longitude,latitude,time\n')
        for p in points:
            f.write(p)
    
    df = pd.read_csv(save_file)
    prev_x = None
    vel = (0,0)
    noise_x = .0005
    noise_v = .0001
    for index, row in df.iterrows():
        if prev_x != None:
            vel = (row['longitude'] - prev_x[0], row['latitude'] - prev_x[1])
            delta = datetime.date.fromisoformat(row['time']) - datetime.date.fromisoformat(prev_x[2])
            vel[0] /= delta 

        df.at[index,'longitude'] = row['longitude'] + np.random.normal(0, noise_x)
        df.at[index,'latitude'] = row['latitude'] + np.random.normal(0, noise_x)
        df.at[index-1,'vel_x'] = vel[0] + np.random.normal(0, noise_v)
        df.at[index-1,'vel_y'] = vel[1] + np.random.normal(0, noise_v)
        prev_x = (row['longitude'], row['latitude'], row['time'])
    df.to_csv(f'rv_{save_file}', sep=',', index=False)

            


if __name__ == '__main__':
    main()