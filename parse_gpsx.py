import gpxpy
import gpxpy.gpx
import pandas as pd 

def main():
    gpx_file = open('Morning_Ride.gpx', 'r')
    save_file = 'ride1.csv'
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                triple = f'{point.latitude},{point.longitude}\n'
                points.append(triple)
    
    with open(save_file, "w") as f:
        f.write('longitude,latitude\n')
        for p in points:
            f.write(p)
    
    df = pd.read_csv(save_file)
    for index, row in df.iterrows():
        row['longitude'] += 
        row['latitude'] += 
    DataFrame.to_csv(path_or_buf=None, sep=','

            


if __name__ == '__main__':
    main()